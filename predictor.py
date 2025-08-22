import pandas as pd
import os

def predict_colleges(rank, caste_gender, branch):
    base_dir = "data"
    csv_path = os.path.join(base_dir, "TSEAMCET_2021_LAST_RANKS.csv")

    # Load CSV
    df = pd.read_csv(csv_path)

    # Filter by branch
    df_branch = df[df["BRANCH"] == branch]

    # Only colleges where rank <= cutoff in that category
    df_eligible = df_branch[df_branch[caste_gender].notna()]
    df_eligible = df_eligible[df_eligible[caste_gender] >= rank]

    # Pick important columns to display
    df_result = df_eligible[["INSTITUTE NAME", caste_gender, "BRANCH NAME", "TUITION FEE", "AFFILIATED"]]

    # Sort by cutoff rank (best options first)
    df_result = df_result.sort_values(by=caste_gender, ascending=True)

    # Return top 10
    return df_result.head(10)
