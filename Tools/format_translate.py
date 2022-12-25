"""Json module."""
import json
import os

PATH = "../Menu Text"
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
    "Phrase",
    "ConditionDescription"
    ]
IDs = [
    "Id",
    "OriginMSkillId",
    "MMysteryMissionGroupId",
    "MHomeSpeechId",
    "OriginMSkillId",
    "MMissionId"
]

A = PATH + "/DMM/"
B = PATH + "/Nutaku Johren/"
WRITE = PATH + "/Translated/"

untranslated: int = 0

def format_list(list_a: list, list_b: list):
    """Format list function."""
    i = 0
    for _, data_a in enumerate(list_a):
        is_skip = False

        if len(list_b) == i:
            return

        if isinstance(data_a, dict) & isinstance(list_b[i], dict):
            for name in IDs:
                if name in data_a:
                    print("ID = " + str(data_a[name]))
                    if data_a[name] is None:
                        continue

                    while data_a[name] > list_b[i][name]:
                        i += 1
                        if len(list_b) == i:
                            return

                    if data_a[name] < list_b[i][name]:
                        is_skip = True

        if not is_skip:
            check_format(data_a, list_b[i])
            i += 1
        else:
            format_missing(data_a)


def format_missing(data_a):
    """Format missing function."""

    global untranslated
    if isinstance(data_a, list):
        for _, data_a in enumerate(data_a):
            format_missing(data_a)

    if isinstance(data_a, dict):
        for key in data_a:
            if key in TRANSLATE_ITEM:
                untranslated += 1
                data_a[key] = "UNTRANSLATED___" + str(data_a[key])
            else:
                format_missing(data_a[key])


def format_dict(dict_a: dict, dict_b: dict):
    """Format dict function."""

    for key in dict_a:
        if key in dict_b:
            if key in TRANSLATE_ITEM:
                dict_a[key] = dict_b[key]
            else:
                check_format(dict_a[key], dict_b[key])
        else:
            format_missing(dict_a[key])


def check_format(data_a, data_b):
    """Format function."""
    if isinstance(data_a, list) & isinstance(data_b, list):
        format_list(data_a, data_b)
        return False

    if isinstance(data_a, dict) & isinstance(data_b, dict):
        format_dict(data_a, data_b)
        return False

    return True

for filename in os.listdir(A):

    path_a = os.path.join(A, filename)

    if filename in os.listdir(B):
        print("Check and format filename: " + filename)
        path_b = os.path.join(B, filename)
        with open(path_a, "r", encoding = "utf8") as fA:
            with open(path_b, "r", encoding = "utf8") as fB:
                json_a = json.load(fA)
                json_b = json.load(fB)

        path_write = os.path.join(WRITE, filename)
        with open(path_write, "w", encoding = "utf8") as fWRITE:
            path = []
            check_format(json_a, json_b)
            json.dump(json_a, fWRITE, indent=4)
            fWRITE.truncate()     # remove remaining part

        print("FORMAT SUCCESS")

    else:
        print("File {" + filename + "} of path {" + A + "} didn't exist on path {" + B + "}")
        filename = "unedited___" + filename
        path_write = os.path.join(WRITE, filename)

        with open(path_write, "w", encoding = "utf8") as fWRITE:
            with open(path_a, "r", encoding = "utf8") as fA:
                json_a = json.load(fA)
                json.dump(json_a, fWRITE, indent=4)
                fWRITE.truncate()

        print("Created file: " + filename)

    print("Total untranslated: " + str(untranslated))