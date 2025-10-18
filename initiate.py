# 1. Initialize Client and Load Data

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from agentds import BenchmarkClient
import os

# 🔑 REPLACE WITH YOUR CREDENTIALS
client = BenchmarkClient(
    api_key="adsb_5vEJ0W7mangzbDJumtZ1JkPw_1760755572",        # Get from your team dashboard
    team_name="iampratham29-team"     # Your exact team name
)



# Authenticate with the provided credentials
if client.authenticate():
    print(f"Successfully authenticated as {client.team_name}")
else:
    print("Authentication failed. Check your API key and team name.")

# Get available domains
domains = client.get_domains()
print(f"Available domains: {domains}")

# Get challenge 1 for a specific domain
domain = "Insurance"
challenge_number = 1
