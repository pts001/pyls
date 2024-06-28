import os
import json

# base path of the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# file path of the json file which contains information of a directory
JSON_FILE_PATH = os.path.join(BASE_DIR, "structure.json") 

# reads json file and returns python object
def read_json(json_file: str)-> dict:
    with open(json_file) as f:
        json_data=json.load(f)
    return json_data

def read_info(**kwargs: dict)-> str:
    json_data = read_json(JSON_FILE_PATH)
    contents=json_data["contents"]
    if kwargs["A"]==False:
        # by default it removes filenames starts with "."
        # when -A argument given, it doesn't remove the hidden files from output
        contents=[content for content in contents if not content["name"].startswith(".")]
    # returns only the names if no argument given
    name_list=[content["name"] for content in contents]
    content_names=" ".join(name_list)
    return content_names