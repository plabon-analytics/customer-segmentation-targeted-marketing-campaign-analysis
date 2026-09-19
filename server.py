"""Local demo server for the static dashboard and Claude interpretation endpoint."""

import json
import os
import urllib.error
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-latest")
PORT = int(os.getenv("PORT", "8000"))
MAX_BODY_BYTES = 32_000


def fallback_interpretation(segment, profile):
    """Return a useful, clearly non-AI response when Claude is unavailable."""
    return {
        "status": "fallback",
        "message": (
            f"{segment['name']} is the deterministic nearest-centroid match "
            f"for this profile. Prioritise the segment playbook: "
            f"{segment['strategyHeading']}. {segment['action']}"
        ),
        "reason": "Anthropic is not configured or could not be reached.",
    }


def anthropic_interpretation(segment, profile):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return fallback_interpretation(segment, profile)

    prompt = (
        "Interpret this deterministic customer segmentation result for a marketing "
        "operator. Do not invent facts, do not change the matched segment, and do "
        "not claim certainty beyond the supplied confidence. Return concise plain "
        "text with exactly three labeled parts: Interpretation, Recommended next "
        "step, and Caveat. Use the segment context and profile values below.\n\n"
        f"Profile: {json.dumps(profile, sort_keys=True)}\n"
        f"Deterministic match: {json.dumps(segment, sort_keys=True)}"
    )
    payload = json.dumps(
        {
            "model": MODEL,
            "max_tokens": 350,
            "temperature": 0.2,
            "system": "You are a careful CRM strategist. Ground every statement in the supplied data.",
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
        text = "\n".join(
            block.get("text", "") for block in data.get("content", []) if block.get("type") == "text"
        ).strip()
        if not text:
            raise ValueError("Anthropic returned no text content")
        return {"status": "ai", "model": MODEL, "message": text}
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
        fallback = fallback_interpretation(segment, profile)
        fallback["reason"] = f"Anthropic request unavailable: {type(exc).__name__}."
        return fallback


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/api/interpret":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("content-length", "0"))
            if length <= 0 or length > MAX_BODY_BYTES:
                raise ValueError("Request body must be between 1 and 32000 bytes")
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            segment = body["segment"]
            profile = body["profile"]
            if not isinstance(segment, dict) or not isinstance(profile, dict):
                raise ValueError("segment and profile must be objects")
            result = anthropic_interpretation(segment, profile)
            self._json_response(200, result)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            self._json_response(400, {"status": "error", "message": str(exc)})

    def _json_response(self, status, payload):
        encoded = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


if __name__ == "__main__":
    print(f"Serving dashboard at http://localhost:{PORT}/docs/live-tools.html")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
