"""Json module."""
import json
import os

PATH = "../Menu Text"
FILENAME = "ArmorEvolutionItems.json"
TRANSLATE_ITEM = [
    "Description",
    "Name",
    "Greeting",
    "Profile",
    "Like",
    "DisLike",
    "CharacterSkill",
    "Pros",
    "Cons",
    "Race",
    "Constellation",
    "Hobby",
    "Title",
    "Country",
    "RecommendOffenceAttribute",
    "RecommendDefenceAttribute",
    "Phrase"
    ]
    
IDs = [
    "Id",
    "OriginMSkillId",
    "MMysteryMissionGroupId",
    "MHomeSpeechId",
    "OriginMSkillId",
    "MCharacterId",
    "MMissionId",
    "MSeriesSetId"
]

A = PATH + "/DMM/"
B = PATH + "/Nutaku Johren/"
WRITE = PATH + "/Try/"

def change_path(json_change, path_change, value):
    """Change value of json path"""
    for i in path_change[:-1]:
        json_change = json_change[i]
    json_change[path_change[-1]] = value

path_a = os.path.join(A, FILENAME)
path_b = os.path.join(B, FILENAME)
with open(path_a, "r", encoding = "utf8") as fA:
    with open(path_b, "r", encoding = "utf8") as fB:
        json_a = json.load(fA)
        json_b = json.load(fB)

path_write = os.path.join(WRITE, FILENAME)
with open(path_write, "w", encoding = "utf8") as fWRITE:
    change_path(json_a, [0, "MItem1", "Name"], "CHECK OKAY")
    json.dump(json_a, fWRITE, indent=4)
    fWRITE.truncate()     # remove remaining part

print("FORMAT SUCCESS")
