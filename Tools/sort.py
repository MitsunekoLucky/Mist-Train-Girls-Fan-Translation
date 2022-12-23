"""Json module."""
import json
import os
import operator

IDs = [
    "Id",
    "OriginMSkillId",
    "MMysteryMissionGroupId",
    "MHomeSpeechId",
    "OriginMSkillId",
    "MMissionId"
]
PATH = "../Menu Text/"
FILE = "MWorldViewModel.json"

def recursive_sort(data):
    """sort"""
    if isinstance(data, list):
        for id_item in IDs:
            if id_item in data:
                data.sort(key=operator.itemgetter(id_item))
        for item in data:
            recursive_sort(item)
    if isinstance(data, dict):
        for key in data:
            recursive_sort(data[key])

    
def sort(sort_path):
    """sort"""
    final_path = PATH + sort_path
    path_a = os.path.join(final_path, FILE)
    with open(path_a, "r+", encoding = "utf8") as file_a:
        data = json.load(file_a)
        recursive_sort(data)
        file_a.seek(0)
        json.dump(data, file_a, indent=4)
        file_a.truncate()


sort("Nutaku Johren/")
sort("DMM/")
