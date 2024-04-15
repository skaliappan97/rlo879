import pandas as pd
import os
from datetime import datetime

path_to_takeout = "C:/Users/Aaron/Downloads/Takeout"
all_data = {}

for (root,dirs,files) in os.walk(os.path.join(path_to_takeout, "Fit", "All Data")):
    for filename in files:
        if "sleep" in filename:
            x = pd.read_json(os.path.join(root, filename))
            for row in x["Data Points"]:
                date = datetime.fromtimestamp(row["endTimeNanos"] // 1000000000).strftime('%Y-%m-%d')
                if date not in all_data:
                    all_data[date] = 0
                all_data[date] += row["fitValue"][0]["value"]["intVal"]

            step_df = pd.DataFrame(all_data.items(), columns=['Date', 'Total Value'])
            step_df.to_csv("./sleep.csv", index=False)
            exit()
