import json
import csv
import os
from pathlib import Path
from definitions import StoryType, MainStory, CharacterStory, EventStory

CSV_FIELDNAMES = ["StoryID","GroupOrder","ViewOrder","NameJP","PhraseJP","NameEN","PhraseEN"]

DIR_CHARACTER = Path("../Scenarios/DMM/Character Story/")
DIR_EVENT = Path("../Scenarios/DMM/Event story/")
DIR_MAIN = Path("../Scenarios/DMM/Main story/")
DIR_CSV_TL = Path("../Scenarios_CSV/")

def get_dmm_json_dir(story_type):
    match story_type:
        case StoryType.Event:
            return DIR_EVENT
        case StoryType.Character:
            return DIR_CHARACTER
        case StoryType.Main:
            return DIR_MAIN

def load_dmm_json(story_type, filename):
    filepath = get_dmm_json_dir(story_type).joinpath(filename)

    with open(filepath, "r", encoding = "utf-8-sig") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Error: {e} (in file: {filepath})")
            return
    
    if "MSceneDetailViewModel" in data:
        data = data["MSceneDetailViewModel"]
    elif "r" in data:
        data = data["r"]["MSceneDetailViewModel"]

    return data

def get_story_object(story_type, filename):
    obj = None
    match story_type:
        case StoryType.Event:
            obj = EventStory(filename)
        case StoryType.Character:
            obj = CharacterStory(filename)
        case StoryType.CharacterHScene:
            obj = CharacterStory(filename)
        case StoryType.Main:
            obj = MainStory(filename)
    return obj

class TranslationMap:
    def __init__(self):
        self.map = {}
    
    def load_csv(self, story):
        filename = story.csv_filename()
        filepath = DIR_CSV_TL.joinpath(filename)

        if not filepath.exists():
            print(f"Translation csv ({filepath}) doesn't exist.")
            return
        
        if filename not in self.map:
            self.map[filename] = {}
        else:
            # if it already exists we don't need to load it again
            return

        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=CSV_FIELDNAMES)

            #skip the header
            next(reader)

            for row in reader:
                story_id = row["StoryID"]
                group_order = row["GroupOrder"]
                view_order = row["ViewOrder"]
                translation_key = self.make_translation_key(story_id, group_order, view_order)
                
                self.map[filename][translation_key] = row
    
    def insert_dmm_json(self, story, data):
        story_id = str(story)
        filename = story.csv_filename()

        if filename not in self.map:
            self.map[filename] = {}

        for line in data:
            group_order = line["GroupOrder"]
            view_order = line["ViewOrder"]
            name_jp = line["Name"]
            phrase_jp = line["Phrase"]

            translation_key = self.make_translation_key(story_id, group_order, view_order)
   
            # update the translation data only if it doesn't exist
            self.map[filename][translation_key] = self.map[filename].get(translation_key, {
                "StoryID": story_id,
                "GroupOrder": group_order,
                "ViewOrder": view_order,
                "NameJP": name_jp,
                "PhraseJP": phrase_jp,
                "NameEN": "",
                "PhraseEN": "",
            })

    def save_all_csv(self):
        for csv_file in self.map:
            csv_path = DIR_CSV_TL.joinpath(csv_file)
            data = self.map[csv_file]
            os.makedirs(csv_path.parent, exist_ok=True)

            with open(csv_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)

                writer.writeheader()
                for key in sorted(data):
                    writer.writerow(data[key])
    
    def make_translation_key(self, story_id, group_order, view_order):
        return f"{str(story_id)}_{str(group_order).zfill(5)}_{str(view_order).zfill(5)}"

    def get_translated_data(self, story_obj, group_order, view_order):
        csv_filename = story_obj.csv_filename()
        story_id = str(story_obj)
        translation_key = self.make_translation_key(story_id, group_order, view_order)
        
        return self.map[csv_filename].get(translation_key)

# def get_translation_map(file):
#     translation_map = {}

#     if Path(file).exists:
#         with open(file, newline='') as csvfile:
#             reader = csv.DictReader(csvfile, fieldnames=CSV_FIELDNAMES)

#             #skip the header
#             next(reader)

#             for row in reader:
#                 story_id = row["StoryID"]
#                 group_order = row["GroupOrder"]
#                 view_order = row["ViewOrder"]
#                 translation_key = make_translation_key(story_id, group_order, view_order)
                
#                 translation_map[translation_key] = row
#     else:
#         print(f"Translation map ({file}) doesn't exist. Creating from scratch")

#     return translation_map

# map = TranslationMap()
# map.load_csv(CharacterStory("215240107"))