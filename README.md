# Customer Segmentation & Targeted Marketing Campaign Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-darkblue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange)
![Method](https://img.shields.io/badge/Method-K--Means%20Clustering-purple)
![RFM](https://img.shields.io/badge/Framework-RFM%20Analysis-teal)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

> Analyzed **2,240 customers** across **29 behavioral features** to solve a real
> marketing problem: campaigns achieving as low as **1.4% acceptance** because
> every customer was treated the same.
>
> Using RFM scoring and K-Means clustering, four behaviorally distinct customer
> segments were identified — including a segment with **$931 average spend and
> 0.0% campaign response across 6 consecutive rounds**. A high-value group the
> business had been reaching out to for 6 campaigns and getting nothing back from
> — not because they are low value, but because the campaign format was wrong.
>
> The result: a data-backed budget reallocation framework replacing one uniform
> campaign approach with four targeted strategies — each justified by behavioral
> evidence, each designed to improve conversion rates and ROI.

---

## Table of Contents

- [Business Problem](#business-problem)
- [Decision Goal](#decision-goal)
- [Analytical Questions](#analytical-questions)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Customer Segments](#customer-segments)
- [The Critical Finding](#the-critical-finding)
- [Business Recommendations](#business-recommendations)
- [Technologies Used](#technologies-used)
- [How To Run](#how-to-run)
- [Project Learnings](#project-learnings)
- [Author](#author)

---

## Business Problem

Many companies use uniform marketing strategies across all customers,
ignoring differences in purchasing behavior and campaign responsiveness.
This results in inefficient budget allocation — marketing resources are
spent on low-response customers while high-potential customers are
under-targeted.

The consequence is predictable and measurable:

- Campaign acceptance rates between **1% and 15%** across 6 rounds
- **1,640 out of 2,240** customers have never responded to a single campaign
- The worst campaign achieved only **1.4% acceptance** — meaning 99 in every
  100 customers contacted returned nothing
- Budget was allocated equally across customers with a **35x difference**
  in campaign response rate and a **10x difference** in average spend

This is not a messaging problem. It is a targeting problem.

---

## Decision Goal

Segment customers based on purchasing behavior, spending patterns,
and campaign engagement — and determine how marketing budget and
campaign strategies should be allocated across these segments to
maximize conversion rates and return on investment.

---

## Analytical Questions

This project was structured to answer six specific business questions:

1. How do customers differ in recency, frequency, and monetary value?
2. How should customers be grouped to enable more effective and targeted
   marketing strategies?
3. Which customer segments respond best to marketing campaigns?
4. Which segments are high-value and which are at risk of disengaging?
5. What specific marketing action should be taken for each segment?
6. Is there a mismatch between customer value and campaign engagement?

---

## Dataset

- **Source:** Customer Personality Analysis — Kaggle
- **Size:** 2,240 customers × 29 features
- **Coverage:** Demographics, spending by product category, purchase
  channel behavior, and complete campaign response history across 6 campaigns

| Feature Group | Columns | Business Purpose |
|---|---|---|
| Customer Profile | Year_Birth, Education, Income, Marital_Status | Who the customer is |
| Spending Behavior | MntWines, MntMeatProducts, MntFruits, MntFishProducts, MntSweetProducts, MntGoldProds | How much they spend |
| Purchase Behavior | NumWebPurchases, NumStorePurchases, NumCatalogPurchases, NumDealsPurchases | How and where they buy |
| Customer Activity | Recency, Dt_Customer | How recently and how long |
| Campaign Engagement | AcceptedCmp1–5, Response | How they respond to marketing |

---

## Project Structure

```
customer-segmentation-analysis/
│
├── notebooks/
│   └── customer_segmentation_analysis.ipynb
│
├── data/
│   └── marketing_campaign.csv
│
├── outputs/
│   └── charts/
│       ├── demographical_analysis.png
│       ├── spending_distribution.png
│       ├── purchase_channel_behavior.png
│       ├── campaign_engagement.png
│       ├── correlation_heatmap.png
│       ├── key_relationships_from_correlation_analysis.png
│       ├── outlier_detection_boxplots.png
│       ├── rfm_feature_distributions.png
│       ├── rfm_score_analysis.png
│       ├── elbow_method_finding_optimal_k.png
│       ├── silhouette_score_cluster_quality.png
│       ├── customer_segments_pca_visualization.png
│       ├── number_of_customers_per_cluster.png
│       ├── campaign_response_rate_per_segment.png
│       └── budget_allocation_evidence.png
│
├── requirements.txt
└── README.md
```

---

## Methodology

This project followed a deliberate business-first analytical framework —
the problem and decision goal were defined before a single line of code
was written.

```
Step 1 → Business Problem Definition
         Define the problem, decision goal, and 6 analytical
         questions before touching any data

Step 2 → Exploratory Data Analysis
         7 analytical dimensions explored across demographics,
         spending, channels, campaigns, correlations,
         key relationships, and outlier detection

Step 3 → Data Cleaning
         Missing values handled, impossible ages removed,
         extreme income outliers identified and dropped,
         invalid categorical entries cleaned —
         every decision justified by an EDA finding

Step 4 → Feature Engineering
         6 new behavioral features built from raw columns:
         Age, Customer Tenure, Total Spend, Total Purchases,
         Total Campaigns Accepted, Has Children

Step 5 → RFM Analysis
         Quartile-based scoring on 5 behavioral dimensions
         Every customer scored 1 to 4 per dimension
         Chosen because several features are skewed or contain
         many repeated values — quartile scoring ranks customers
         relative to one another, creating fair comparable scores

Step 6 → K-Means Clustering
         Elbow Method and Silhouette Score used together
         K=4 selected — balancing statistical quality
         with business actionability
         PCA used to visualize clusters in 2 dimensions

Step 7 → Segment Profiling and Naming
         Behavioral and demographic profiling per cluster
         4 customer personas identified, named, and validated
         against actual campaign response rates

Step 8 → Business Recommendations
         Targeted strategy per segment
         Budget reallocation framework defined
         Every recommendation traced to a specific data point
```

---

## Cluster Visualization

The K-Means model identified four customer groups using RFM-based
behavioral scores. PCA was used only for visualization, reducing the
cluster features into two dimensions so the segment separation can be
inspected visually.

![Customer Segments PCA Visualization](<outputs/charts/Customer Segments — PCA Visualization.png>)

---

## Key Findings

**Finding 1 — Campaign Performance Is Critically Low**
All 6 campaigns achieved acceptance rates between 1% and 15%.
1,640 out of 2,240 customers have never responded to a single campaign
across all 6 rounds of outreach. The uniform approach is systematically
failing — this is the data proof the business problem is real.

**Finding 2 — Four Distinct Behavioral Segments Exist**
K-Means clustering on RFM behavioral scores identified 4 natural customer
groups of roughly equal size — each with fundamentally different spending,
frequency, income, and engagement profiles that cannot be revealed by
demographic analysis alone.

**Finding 3 — A 35x Response Rate Gap Exists Across Segments**
Champions respond at 35.3%. At-Risk Dormants respond at 3.9%.
The same campaign budget is currently spent on both groups equally —
despite a 10x difference in average spend and a 35x difference in
campaign response rate.

![Campaign Response Rate Per Segment (%)](<outputs/charts/Campaign Response Rate Per Segment (%).png>)

**Finding 4 — The Second Most Valuable Segment Is Completely Unreachable**
High Value Disengaged customers spend $931 on average and make 21 purchases
but have accepted zero campaigns across all 6 rounds. They buy entirely
through self-directed behavior. Current campaign formats have definitively
failed to reach this segment across 6 consecutive attempts.

**Finding 5 — Demographics Cannot Explain Campaign Behavior**
Champions and High Value Disengaged are demographically near-identical —
similar age (59.3 vs 59.1), similar income ($69,631 vs $65,277), similar
tenure (380 vs 375 days). Yet their campaign response rates are 35.3% vs 0.0%.
Behavioral segmentation is the only approach that reveals this critical
difference. Demographic targeting would have grouped them together —
producing completely wrong campaign recommendations for both.

**Finding 6 — Budget Conscious Actives Are The Highest Growth Opportunity**
The most recently active segment at 24.06 days recency — responding at 14.2%
despite being the lowest income group ($34,741). Financial constraints are
suppressing spend, not lack of interest. The right value-aligned offer has
direct and measurable conversion potential.

---

## Customer Segments

| Segment | Customers | Avg Spend | Avg Purchases | Avg Income | Response Rate |
|---|---|---|---|---|---|
| Champions | 657 (29.8%) | $1,179 | 21.3 | $69,631 | 35.3% |
| High Value Disengaged | 482 (21.9%) | $931 | 20.9 | $65,277 | 0.0% |
| Budget Conscious Actives | 548 (24.8%) | $108 | 8.2 | $34,741 | 14.2% |
| At-Risk Dormants | 518 (23.5%) | $109 | 8.3 | $35,347 | 3.9% |

### Champions
Highest performing segment on every measurable dimension — spend, frequency,
income, and campaign response. Majority child-free (51%) with more disposable
income available. Average income of $69,631 and 380-day customer tenure confirm
long-term, high-value relationships. Dominant spend categories are wines ($616
average) and meat products ($328 average).

### High Value Disengaged
The most strategically significant finding in the project. $931 average spend
and 21 purchases entirely through self-directed behavior — zero campaign response
across all 6 rounds. High income ($65,277) customers who buy actively but are
completely unreachable through current campaign formats. Represents the most
significant budget waste and the most significant untapped opportunity
simultaneously. Requires a fundamentally different engagement approach —
not more of the same campaigns.

### Budget Conscious Actives
Most recently active segment at 24.06 days recency. Responding to campaigns at
14.2% despite the lowest income ($34,741) and 86% family households. Financial
constraints are suppressing spend — not interest in the business. Highest growth
potential with the right value-aligned, family-oriented offer. A frequency reward
program aligns naturally with their 8.2 average purchase count.

### At-Risk Dormants
Last purchased 75.31 days ago on average — approaching the 90-day threshold
beyond which re-engagement becomes significantly harder and more expensive.
Low spend ($109), low frequency (8.3 purchases), near-zero campaign response
(3.9%), and 88% family households limiting disposable income. Without targeted
low-cost intervention, these customers are on a clear path toward permanent churn.

---

## The Critical Finding

> Champions and High Value Disengaged customers are demographically
> near-identical — same age bracket, similar income, similar tenure.
> Yet one group responds to campaigns at 35.3% and the other at 0.0%.
> Demographic targeting would have grouped them together and given
> them the same campaign. Behavioral segmentation separated them —
> revealing the most important strategic distinction in the entire dataset.

This single finding is the analytical justification for behavioral
segmentation over demographic targeting in this project.

---

## Business Recommendations

### Champions → Retain and Reward

- Launch a tiered loyalty program with points per purchase,
  early access to new products, and exclusive member events
- Campaign offers should lead with premium wine and meat bundles —
  the two dominant spend categories at $616 and $328 respectively
- Deliver simultaneously across web, store, and catalog —
  Champions actively use all three channels
- Monitor recency monthly — trigger personalized re-engagement
  immediately if any Champion exceeds 60 days without a purchase
- **Goal:** Retain the highest-value customer relationships
  and deepen loyalty before churn risk grows

### High Value Disengaged → Stop Wasting. Start Testing.

- Immediately stop standard campaign spend on this segment —
  6 rounds of confirmed 0.0% response is conclusive evidence
  the current format does not work here
- Redirect freed budget to Champions and Budget Conscious Actives
  where response behavior is stronger
- Test behavior-triggered offers at the point of purchase —
  in-store point-of-sale promotions and web behavioral nudges
  triggered when a customer makes a purchase
- **Goal:** Find the channel that actually reaches these customers
  and stop confirmed budget waste on the current approach

### Budget Conscious Actives → Unlock Constrained Potential

- Design campaigns around family value — 86% have children,
  making accessible pricing the primary conversion mechanism
- Family-sized product bundles, multi-buy deals, and limited-time
  discounts make higher spend financially viable for this group
- Deliver through low-cost digital and web-exclusive channels only
- Launch a frequency reward program aligned with their
  natural 8.2 average purchase count
- **Goal:** Convert active engagement into higher spend
  through budget-aligned offers that respect financial reality

### At-Risk Dormants → One Attempt Then Reallocate

- Send one single low-cost email re-engagement campaign —
  a simple, family-relevant, accessible offer
- If they respond — move them into Budget Conscious Active
  strategies going forward
- If they do not respond — formally classify as churned
  and stop all campaign spend on this segment immediately
- Redirect freed budget to Champions and Budget Conscious Actives
- **Goal:** Recover what is recoverable cheaply and redirect
  budget to segments with stronger observed response behavior

### Budget Priority Framework

| Priority | Segment | Reason |
|---|---|---|
| 1 | Champions | 35.3% response — highest observed response and spend |
| 2 | Budget Conscious Actives | 14.2% response — clear growth potential |
| 3 | High Value Disengaged | New channel approach testing required |
| 4 | At-Risk Dormants | Minimal spend only — one attempt maximum |

### Budget Allocation Evidence

Response rate shows who is most likely to convert; average spend shows
the potential value behind that response. Together, these two metrics
support the recommended campaign budget priority.

![Budget Allocation Evidence](<outputs/charts/Budget Allocation Evidence.png>)

---

## Technologies Used

| Library | Version | Purpose |
|---|---|---|
| Python | 3.11 | Core programming language |
| Pandas | 2.x | Data loading, cleaning, manipulation |
| NumPy | 1.x | Numerical operations and array handling |
| Matplotlib | 3.x | Base plotting engine and figure control |
| Seaborn | 0.x | Statistical visualizations |
| Scikit-learn | 1.x | K-Means clustering, PCA, Silhouette Score |
| Datetime | Built-in | Date parsing and tenure calculation |

> Run `pip show pandas scikit-learn seaborn matplotlib numpy`
> in your environment to confirm exact installed versions
> before reproducing results.

---

## How To Run

**1. Clone the repository**
```bash
git clone https://github.com/plabon-analytics/customer-segmentation-targeted-marketing-campaign-analysis.git
cd customer-segmentation-targeted-marketing-campaign-analysis
```

**2. Install required libraries**
```bash
pip install -r requirements.txt
```

**3. Add the dataset**
```
Place marketing_campaign.csv inside the data/ folder.
Dataset available at Kaggle — search "Customer Personality Analysis"
Direct link: https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis
```

**4. Launch Jupyter Notebook**
```bash
jupyter notebook notebooks/customer_segmentation_analysis.ipynb
```

**5. Run all cells in order**
```
Sections 1 through 11 — run sequentially top to bottom.
All outputs, charts, and segment assignments generate automatically.
Do not skip sections — each one builds on the previous.
```

---

## Project Learnings

This project was built following a deliberate business-first methodology.
The problem, decision goal, and analytical questions were defined before
a single line of code was written — ensuring every chart, model, and
interpretation served a specific business purpose.

Key analytical decisions and the reasoning behind each:

**RFM Scoring chosen over Feature Scaling**
All five behavioral features are right-skewed or contain many repeated
values. Quartile-based RFM scoring was chosen because it ranks customers
relative to one another — creating fair, comparable 1-to-4 scores across
all dimensions. Equal-interval scoring would risk placing too many customers
into the same low-value bands, making segmentation less useful.

**K=4 chosen over K=2 (which had the highest Silhouette Score)**
The Silhouette Score peaked at K=2 (0.3739) — but two segments are too
broad for a differentiated campaign strategy. Analytics exists to serve
business decisions, not mathematical perfection. K=4 (Silhouette 0.2764)
was chosen because it produces four meaningfully distinct, independently
actionable customer groups. The Elbow Method confirmed a clear bend at
K=4 to K=5.

**Behavioral segmentation chosen over demographic segmentation**
Champions and High Value Disengaged are demographically near-identical but
their campaign response rates are 35.3% vs 0.0%. Demographic targeting
would have grouped them together — producing completely wrong recommendations
for both groups. Behavioral features reveal what customers actually do.
Demographic features only describe who they are.

**Customer Tenure excluded from K-Means clustering**
Tenure was built from the enrollment date using the most recent enrollment
date in the dataset as a reference point — an assumption, not a recorded
last activity date. Recency covers active engagement more reliably as a
directly recorded behavioral fact. Tenure was retained for segment profiling
context only.

**Every cleaning decision traced to an EDA finding**
No data was removed or imputed randomly. The extreme income outlier
($666,000 earning, near-zero spend) was removed because it would pull
an entire K-Means cluster toward a profile representing nobody else.
Impossible ages (120+) were removed as confirmed data entry errors.
Invalid marital status entries were removed because they cannot be
recoded into meaningful categories without fabricating data.

---

## Author

**Plabon Roy**
Data Analytics | Customer Behavior & Segmentation

Passionate about business-first analytical thinking — defining the
problem before touching the data, and connecting every chart and
model to a decision that actually matters to the business.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/plabon-roy-analytics/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/plabon-analytics)

---

*This project was built as a complete end-to-end portfolio piece
demonstrating the full analytics workflow — from business problem
definition through data cleaning, feature engineering, RFM analysis,
K-Means clustering, segment profiling, and actionable business
recommendations. Every decision in the project is documented,
justified, and traceable back to the business problem it was
built to solve.*
