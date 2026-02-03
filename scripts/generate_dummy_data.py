"""
Docstring for citi_bike_analysis.scripts.generate_dummy_data
Generate Dummy Data to Test Pipeline
Save everything to
"""

import pandas as pd
import os

# create directory
os.makedirs("../data/test", exist_ok=True)

# dummy data #1
data1 = {
    "ride_id": ["A1", "A2"],
    "rideable_type": ["electric_bike", "classic_bike"],
    "started_at": ["2023-01-01 10:00:00", "2023-01-01 11:00:00"],
    "ended_at": ["2023-01-01 10:15:00", "2023-01-01 11:20:00"],
    "start_station_name": ["Central Park", "Broadway"],
    "start_station_id": ["101", "102"],
    "end_station_name": ["Times Square", "Wall St"],
    "end_station_id": ["201", "202"],
    "start_lat": [40.78, 40.75],
    "start_lng": [-73.96, -73.98],
    "end_lat": [40.75, 40.70],
    "end_lng": [-73.98, -74.00],
    "member_casual": ["member", "casual"],
}

# dummy data #2 with na values
data2 = {
    "ride_id": ["B1", "B2"],
    "rideable_type": ["electric_bike", "electric_bike"],
    "started_at": ["2023-02-01 09:00:00", "2023-02-02 08:00:00"],
    "ended_at": ["2023-02-01 09:10:00", "2023-02-02 08:05:00"],
    "start_station_name": ["Pier 1", None],  # Missing station
    "start_station_id": ["301", None],
    "end_station_name": ["Ferry Terminal", "Pier 1"],
    "end_station_id": ["401", "301"],
    "start_lat": [40.70, 40.71],
    "start_lng": [-74.01, -74.02],
    "end_lat": [40.72, 40.70],
    "end_lng": [-74.00, -74.01],
    "member_casual": ["casual", "member"],
}

pd.DataFrame(data1).to_csv("../data/test/test_data_1.csv", index=False)
pd.DataFrame(data2).to_csv("../data/test/test_data_2.csv", index=False)

print("Dummy data created in ../data/test")
