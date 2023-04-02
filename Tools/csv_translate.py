import json
import os
from pathlib import Path
from json import JSONDecodeError
from csv_lib import load_dmm_json, get_story_object, TranslationMap, get_dmm_json_dir
from definitions import StoryType

OUTPUT_DIR = Path("../Scenarios_TL/")

def create_translated_json(story_type):
    translation_map = TranslationMap()

    original_json_dir = get_dmm_json_dir(story_type)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(original_json_dir):
        file = Path(file)

        #people put .bak/.zip files into the system for some reason, so ignore them
        if file.suffix != ".json":
            continue

        story_id = file.stem
        story_obj = get_story_object(story_type, story_id)
        
        #load the corresponding CSV file for this story ID if it exists
        translation_map.load_csv(story_obj)

        #load the json file for this story ID
        data = load_dmm_json(story_type, file)

        if data is None:
            continue

        file_has_translations = False
        for i, line in enumerate(data):
            group_order = line["GroupOrder"]
            view_order = line["ViewOrder"]

            csv_filename = story_obj.csv_filename()
            translated_data = translation_map.get_translated_data(story_obj, group_order, view_order)

            if translated_data is not None:
                phrase = translated_data.get("PhraseEN")
                name = translated_data["NameEN"]
                if phrase != "":
                    file_has_translations = True
                    data[i]["Phrase"] = phrase
                    data[i]["Name"] = name
        
        if file_has_translations:
            output_path = OUTPUT_DIR.joinpath(story_obj.translated_filename())
            with open(output_path, "w", encoding = "utf-8-sig") as json_file:
                json.dump(data, fp=json_file, indent=4, ensure_ascii=False)

create_translated_json(StoryType.Main)
create_translated_json(StoryType.Event)
create_translated_json(StoryType.Character)
