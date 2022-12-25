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


def check_list(list_a: list, list_b: list) -> bool:
    """Check list function."""
    result = True

    i = 0
    for _, data_a in enumerate(list_a):
        is_skip = False

        if len(list_b) == i:
            print("IDs are missing on JSON PATH: " + B)
            return False

        if isinstance(data_a, dict) & isinstance(list_b[i], dict):
            for name in IDs:
                if name in data_a:
                    print("ID = " + str(data_a[name]))
                    if data_a[name] is None:
                        continue

                    while data_a[name] > list_b[i][name]:
                        print("An ID is missing on JSON PATH: " + A)
                        print("Missing ID number: " + str(data_a[name]))
                        i += 1
                        if len(list_b) == i:
                            print("IDs are missing on JSON PATH: " + B)
                            return False

                    if data_a[name] < list_b[i][name]:
                        print("An ID is missing on JSON PATH: " + B)
                        print("Missing ID number: " + str(data_a[name]))
                        is_skip = True
                        result = False

        if not is_skip:
            result = result & check(data_a, list_b[i])
            i += 1

    return result


def check_dict(dict_a: dict, dict_b: dict) -> bool:
    """Check dict function."""

    result = True

    for key in dict_a:
        if not key in dict_b:
            print("TWO JSON FILE NOT COMPATIBLE, KEY NOT EXIST")
            print("{" + key + "} is not exist on json file path: " + B)
            result = result & False
        else:
            if not key in TRANSLATE_ITEM:
                iter_result = check(dict_a[key], dict_b[key])
                if not iter_result:
                    print("KEY: " + key)
                result = result & iter_result

    return result


def check_value(value_a, value_b) -> bool:
    """Check value function."""

    if value_a != value_b:
        print("TWO JSON FILE NOT COMPATIBLE, VALUE NOT THE SAME")
        print(str(value_a) + "!=" + str(value_b))
        return False
    return True


def check(value_a, value_b) -> bool:
    """Check type function."""

    if isinstance(value_a, list) & isinstance(value_b, list):
        return check_list(value_a, value_b)

    if isinstance(value_a, dict) & isinstance(value_b, dict):
        return check_dict(value_a, value_b)

    return check_value(value_a, value_b)


for filename in os.listdir(A):
    if filename in os.listdir(B):
        print("Check filename: " + filename)
        path_a = os.path.join(A, filename)
        path_b = os.path.join(B, filename)
        with open(path_a, "r", encoding = "utf8") as fA:
            with open(path_b, "r", encoding = "utf8") as fB:
                json_a = json.load(fA)
                json_b = json.load(fB)

        check(json_a, json_b)
    else:
        print("File {" + filename + "} of path {" + A + "} didn't exist on path {" + B + "}")
    
    print("CHECK SUCCESS: " + filename)




    