import json
import csv
import os
from pathlib import Path
from csv_lib import load_dmm_json, get_story_object, TranslationMap, get_dmm_json_dir
from definitions import StoryType

def update_translation_csv(story_type):
    translation_map = TranslationMap()

    directory = get_dmm_json_dir(story_type)
    
    # Go through every json file in the source directory
    for file in os.listdir(directory):
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

        #insert the json file into the translation mapping if it parsed properly
        if data is not None:
            translation_map.insert_dmm_json(story_obj, data)
    
    translation_map.save_all_csv()

update_translation_csv(StoryType.Main)
update_translation_csv(StoryType.Event)
update_translation_csv(StoryType.Character)