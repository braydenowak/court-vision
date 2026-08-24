import pandas as pd
import json

df = pd.read_excel("NBA_2025-26_Player_Stats.xlsx", sheet_name="Player Stats")
records = df.to_dict(orient="records")
with open("player_stats.json", "w") as f:
    json.dump(records, f)
print(f"Wrote {len(records)} players")

df = pd.read_excel("NBA_2025-26_Player_Stats.xlsx", sheet_name="Team Stints")
records = df.to_dict(orient="records")
with open("team_stints.json", "w") as f:
    json.dump(records, f)
print(f"Wrote {len(records)} team stints")

df = pd.read_excel("NBA_2025-26_Player_Stats.xlsx", sheet_name="Team Summary")
records = df.to_dict(orient="records")
with open("team_summary.json", "w") as f:
    json.dump(records, f)
print(f"Wrote {len(records)} team summaries")