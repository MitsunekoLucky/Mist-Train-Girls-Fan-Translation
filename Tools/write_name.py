import os

PATH = "../Scenarios/DMM/Event story"
with open("file_list_story.txt", "a", encoding = "utf8") as file:
    for filename in os.listdir(PATH):
        file.write(filename)
        file.write("\n")