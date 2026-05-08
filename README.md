# BISG Fair Lending Analytics for Fintech

## Overview
This repository contains tools and documentation for implementing **Bayesian Improved Surname Geocoding (BISG)** within a Fintech credit risk environment. 

In non-mortgage lending, **Regulation B** generally prohibits lenders from requesting a borrower's race. This project provides a standardized "proxy" methodology to perform Fair Lending Analytics, ensuring that automated underwriting models (such as those predicting **First Payment Default - FPD**) do not have a disparate impact on protected classes (Greenwald et al., 2024).

---

## How BISG Works
BISG combines two publicly available data points using **Bayes' Theorem** to calculate a single probability of a borrower’s race or ethnicity:

1.  **Surname Analysis**: Utilizing Census Bureau data to determine racial probability based on last names.
2.  **Geocoding**: Utilizing ZIP codes or Census Tracts to determine the racial composition of the borrower's neighborhood.

### Mathematical Framework
The algorithm calculates the probability ($P$) that an individual belongs to a racial group ($R_i$) given their surname ($S$) and location ($L$):

$$P(R_i | S, L) = \frac{P(R_i | S) \cdot P(L | R_i)}{\sum_{j=1}^{n} P(R_j | S) \cdot P(L | R_j)}$$

---

## Practical Analytics: The FPD Use Case
When evaluating a **First Payment Default (FPD)** model, the workflow follows these steps:

### 1. Imputation
The borrower list is run through the BISG tool. Each individual is assigned a probability (e.g., "Customer A has an 85% probability of being African American").

### 2. Disparity Testing
Analysts compare key metrics—such as **Approval Rates** or **Interest Rates**—across proxied groups. 
*   **Example**: If an FPD model denies 40% of borrowers proxied as Black but only 10% of those proxied as White, a potential disparate impact is identified.

### 3. Search for Less Discriminatory Alternatives (LDA)
If a disparity is found, the company must:
*   Validate the **"legitimate business necessity"** of the model.
*   Search for an **LDA**: A different version of the model (e.g., removing "inquiry velocity" or "bank account age") that achieves similar predictive power with less impact on protected groups (Sargeant, 2024).

---

## Known Limitations & Risks
While BISG is the industry standard, current research highlights critical gaps:

*   **Accuracy Gaps**: BISG is highly accurate for White and Asian populations but significantly less accurate for Black and Hispanic borrowers, particularly in diverse urban areas (Greenwald et al., 2024).
*   **Downward Bias**: Recent studies indicate that using BISG can bias measured racial disparities downward by **up to 43%** (Greenwald et al., 2024; Harvard Business School, 2023). This can potentially mask existing discrimination in loan approvals.
*   **Location Fixed Effects**: Including location data in both the proxy and the regression analysis can "discard" much of the predictive power, leading to illusory accuracy improvements (Harvard Business School, 2023).

---

## References

Greenwald, D., Howell, S. T., Li, C., & Yimfor, E. (2024). Regulatory arbitrage or random errors? Implications of race prediction algorithms in fair lending analysis. *Journal of Financial Economics*, *157*. https://doi.org/10.1016/j.jfineco.2024.103848
*Cited by: 2*

Harvard Business School. (2023). *The limits of algorithmic measures of race in studies of outcome disparities*. SSRN. https://ssrn.com/abstract=4426161

Kallus, N., Mao, X., & Zhou, A. (2022). Assessing algorithmic fairness with unobserved protected class labels. *Management Science*.

Sargeant, H. (2024). The arity of disparity: Updating disparate impact for modern fair lending. *University of Chicago: Becker Friedman Institute for Economics*. https://bfi.uchicago.edu/wp-content/uploads/2024/02/BFI_WP_2024-18.pdf