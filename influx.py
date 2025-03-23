import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random
from datetime import datetime
from datetime import timedelta

token = "5I91-bWybR19eHFUlLoTE09jst3FvMVjBCm66t4EEr7UO47n4NiBfLx_HbAjO7X9PC8wJA4qQjyFwdaVy4CJHA=="
org = "Arhitekture Velepodatkov"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "arhitekture-velepodatkov"

write_api = write_client.write_api(write_options=SYNCHRONOUS)

num_matches = 8  # Generate data for 3 different matches
num_players = 20000
time_steps_per_match = 15  # Simulate 100 time points per match

for match_id in range(1, num_matches + 1):
    print(f"Generating data for Match ID: {match_id}")
    for player_id in range(1, num_players + 1):
        print(f"  Generating data for Player ID: {player_id}")
        for step in range(time_steps_per_match):
            timestamp = datetime.utcnow() + timedelta(seconds=step)

            speed = random.uniform(0, 25)  # Speed in km/h
            distance_covered = random.uniform(0, 15000) # Total distance covered in meters (can reset per match if needed)
            location_x = random.uniform(0, 105) # Location on x-axis (field width)
            location_y = random.uniform(0, 68)  # Location on y-axis (field height)

            point = (
                Point("player_movement")
                .tag("match_id", match_id)
                .tag("player_id", player_id)
                .tag("team", f"Team{1 if player_id <= 11 else 2}")
                .field("speed", speed)
                .field("distance_covered", distance_covered)
                .field("location_x", location_x)
                .field("location_y", location_y)
                .time(timestamp, WritePrecision.NS)
            )
            write_api.write(bucket=bucket, org=org, record=point)
            time.sleep(0.0001) # Small delay

print("Generated and inserted player movement data for multiple matches.")