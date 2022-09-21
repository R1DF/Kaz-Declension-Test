import json
import os

# Getting file WITH UTF-8 (otherwise it won't work)
with open(os.getcwd() + "\\data.json", encoding="utf-8") as f:
    json_data = json.load(f)
