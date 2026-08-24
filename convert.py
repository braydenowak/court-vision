import pandas as pd
import json

def write_js(sheet_name, var_name, filename):
    df = pd.read_excel("NBA_2025-26_Player_Stats.xlsx", sheet_name=sheet_name)
    records = df.to_dict(orient="records")
    with open(filename, "w") as f:
        f.write(f"const {var_name} = ")
        json.dump(records, f)
        f.write(";")
    print(f"Wrote {len(records)} rows to {filename}")

write_js("Player Stats", "playerStats", "player_stats.js")
write_js("Team Stints", "teamStints", "team_stints.js")
write_js("Team Summary", "teamSummary", "team_summary.js")