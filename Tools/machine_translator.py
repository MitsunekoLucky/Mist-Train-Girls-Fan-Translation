from translate import Translator
import os
import json
import re

TRANSLATOR = Translator(from_lang="ja", to_lang="en", provider='mymemory')
PATH = "../Menu Text/Decoded/"
TRANSLATED_PATH = "../Menu Text/TRY/"

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

def main():
    for filename in os.listdir(PATH):
        print("Starting file: " + filename)
        path_a = os.path.join(PATH, filename)
        path_b = os.path.join(TRANSLATED_PATH, filename)
        with open(path_a, "r", encoding = "utf8") as file_a:
            json_a = json.load(file_a)
            
        translated_data = detect_and_translate(json_a)
        
        with open(path_b, "w", encoding = "utf8") as file_b:
            json.dump(translated_data, file_b, indent=4)
            file_b.truncate()  

        print("Translate Success!")
        
def is_japanese_char(ch):
    assert(len(ch) == 1)  # only use this for single character strings
    if re.search("[\u3040-\u309f]", ch):
        return True  # is hiragana
    if re.search("[\u30a0-\u30ff]", ch):
        return True  # is katakana
    if re.search("[\u4e00-\u9faf]", ch):
        return True  # is kanji
    return False

def detect_and_translate(data):
    
    if isinstance(data, list):
        for item in data:
            detect_and_translate(item)
        
    if isinstance(data, dict):
        for key in data:
            if key in TRANSLATE_ITEM:
                jp = False
                for ch in data[key]:
                    if is_japanese_char(ch):
                        jp = True
                        break
                
                if jp:
                    translated = TRANSLATOR.translate(data[key])
                    print("Translated data: {" + data[key] + "} into {" + translated + "}")
                    data[key] = translated
                else:
                    print("Found translated item: " + data[key])
            else:
                detect_and_translate(data[key])

main()