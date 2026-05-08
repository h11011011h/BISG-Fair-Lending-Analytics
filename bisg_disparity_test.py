import pandas as pd
import numpy as np

def calculate_bisg_probability(surname_prob, geo_prob):
    """
    Simplified Bayesian calculation:
    P(Race|S, G) = [P(Race|S) * P(Race|G)] / Sum(P(Race_i|S) * P(Race_i|G))
    """
    numerator = surname_prob * geo_prob
    # In a full model, we would divide by the sum of probabilities for all races.
    # Here we simplify to show the interaction.
    return round(numerator / (numerator + (1 - surname_prob) * (1 - geo_prob)), 4)

def run_fair_lending_audit():
    print("--- Initializing Fair Lending Analysis (FPD Model) ---")
    
    # 1. Mock Data Generation
    # Imagine these are features from your First Payment Default (FPD) model
    data = {
        'applicant_id': range(1, 101),
        'surname_white_prob': np.random.uniform(0.1, 0.9, 100),
        'geo_white_prob': np.random.uniform(0.1, 0.9, 100),
        'is_approved': np.random.choice([0, 1], size=100, p=[0.3, 0.7])
    }
    
    df = pd.DataFrame(data)

    # 2. BISG Imputation
    # We assign a White/Non-White proxy based on the combined Bayesian probability
    df['bisg_white_prob'] = df.apply(
        lambda x: calculate_bisg_probability(x['surname_white_prob'], x['geo_white_prob']), axis=1
    )
    
    # Thresholding: If prob > 0.5, proxy as 'White', else 'Non-White'
    df['proxy_race'] = np.where(df['bisg_white_prob'] > 0.5, 'White', 'Non-White')

    # 3. Disparity Testing (Adverse Impact Ratio)
    approval_stats = df.groupby('proxy_race')['is_approved'].mean()
    
    white_approval = approval_stats.get('White', 0)
    non_white_approval = approval_stats.get('Non-White', 0)
    
    # Adverse Impact Ratio (AIR)
    air = non_white_approval / white_approval if white_approval > 0 else 0

    print(f"\nResults by Proxied Group:")
    print(f"White Approval Rate: {white_approval:.2%}")
    print(f"Non-White Approval Rate: {non_white_approval:.2%}")
    print(f"Adverse Impact Ratio (AIR): {air:.2f}")

    # 4. Regulatory Threshold (Four-Fifths Rule)
    if air < 0.80:
        print("\n[ALERT] Potential Disparate Impact detected.")
        print("Action Required: Search for Less Discriminatory Alternatives (LDA).")
    else:
        print("\n[PASS] No immediate evidence of disparate impact based on BISG proxy.")

if __name__ == "__main__":
    run_fair_lending_audit()