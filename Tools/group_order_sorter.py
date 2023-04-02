from pathlib import Path
import os
import json

JOHREN_PATH = Path("../Scenarios/Johren/Character Story")

def load_json(filename):
    with open(filename, "r", encoding = "utf-8-sig") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Error: {e} (in file: {filename})")
            return
    
    if "MSceneDetailViewModel" in data:
        data = data["MSceneDetailViewModel"]
    elif "r" in data:
        data = data["r"]["MSceneDetailViewModel"]

def custom_sort(item):
    return item["GroupOrder"]

for file in os.listdir(JOHREN_PATH):
    filename = JOHREN_PATH.joinpath(file)

    with open(filename, "r", encoding = "utf-8-sig") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Error: {e} (in file: {filename})")
            continue
    
    data["r"]["MSceneDetailViewModel"] = sorted(data["r"]["MSceneDetailViewModel"], key=custom_sort)

    with open(filename, "w", encoding = "utf-8-sig") as json_file:
        json.dump(data, fp=json_file, indent=4, ensure_ascii=False)
