# 1. Initialize Client and Load Data

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from agentds import BenchmarkClient

# 🔑 REPLACE WITH YOUR CREDENTIALS
client = BenchmarkClient(
    api_key="adsb_5vEJ0W7mangzbDJumtZ1JkPw_1760755572",        # Get from your team dashboard
    team_name="iampratham29-team"     # Your exact team name
)

# Load data from PVC paths
print("📂 Loading Commerce Challenge 1 data...")

# Load training and test data
train_sales = pd.read_csv("sales_history_train.csv")
# test_sales = pd.read_csv("sales_history_test.csv")

print(f"✅ Data loaded:")
print(f"   Train sales: {train_sales.shape}")
# print(f"   Test sales: {test_sales.shape}")
print(f"   Features: {list(train_sales.columns)}")