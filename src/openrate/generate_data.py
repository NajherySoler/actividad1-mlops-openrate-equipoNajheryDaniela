import numpy as np
import pandas as pd
 
np.random.seed(42)
 
n = 10000
 
data = pd.DataFrame({
    "user_id": range(1, n + 1),
    "site": np.random.choice(["web", "app"], n),
    "campaign_type": np.random.choice(["promo", "informative", "reminder"], n),
    "device_os": np.random.choice(["Android", "iOS"], n),
    "hour_of_day": np.random.randint(0, 24, n),
    "day_of_week": np.random.choice(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], n),
    "historical_open_rate": np.round(np.random.uniform(0, 1, n), 2),
    "historical_push_count": np.random.randint(1, 100, n),
    "days_since_last_open": np.random.randint(0, 30, n),
    "segment": np.random.choice(["new", "active", "inactive"], n)
})
 
 
prob_open = (
    0.6 * data["historical_open_rate"]
    + 0.2 * (data["days_since_last_open"] < 10).astype(int)
    + 0.1 * (data["segment"] == "active").astype(int)
    + 0.1 * np.random.rand(n)
)
 
data["target_opened"] = (prob_open > 0.55).astype(int)
 
data.to_csv("data/raw/openrate_mock.csv", index=False)
 
print("Dataset mock generado en data/raw/openrate_mock.csv")
print(data.head())
 