import os
import re
import json
import argparse
from datetime import datetime

# file path of the json file which contains information of a directory
JSON_FILE_PATH = os.environ["DIR_STRUCTURE_FILE"]

# reads json file and returns python object
def read_json(json_file: str)-> dict:
    with open(json_file) as f:
        json_data=json.load(f)
    return json_data

# handles path
def handle_path(dir_: dict, search_key: str)-> dict:
    if search_key in [".", "./"]:
        return dir_
    search_key=re.sub("^./","",search_key)
    dir_name=search_key.split("/")
    if len(dir_name)>1:
        full_path=""
        # recursively finds target dir/file if nested path is given
        for dir_nam in dir_name:
            dir_=handle_path(dir_,dir_nam)
            # returns None if valid path not found
            if dir_ is None:
                return
            full_path+=f'/{dir_["name"]}'
            if full_path.strip("/") == search_key:
                dir_["name"]=search_key
                return dir_
    if dir_["name"]==search_key:
        # returns dir/filename from current dir given as input path
        return dir_
    if "contents" in dir_.keys():
        # finds sub-dir/file under current dir given as input path
        for sub_dir in dir_["contents"]:
            if sub_dir["name"]==search_key:
                return sub_dir

# converts file size to human readable formats
# i.e-bytes to KB,MB and GB
def convert_file_size(size):
    if size>=1024:
        size_kb = round(size/1024,1)
        if size_kb>=1024:
            size_mb = round(size_kb/1024,1)
            if size_mb>=1024:
                size_gb = round(size_mb/1024,1)
                return f"{size_gb}G"
            return f"{size_mb}M"
        return f"{size_kb}K"
    return size

def read_info(**kwargs: dict)-> str:
    json_data = read_json(JSON_FILE_PATH)
    contents=json_data["contents"]
    if kwargs["path"]:
        # handles target path if arg supplied from cli
        contents=handle_path(json_data, kwargs["path"])
        if contents is None:
            # returns error message on incorrect path
            return f"error: cannot access '{kwargs['path']}': No such file or directory"
        contents=contents["contents"] if "contents" in contents.keys() else [contents]
    if kwargs["A"]==False:
        # by default it removes filenames starts with "."
        # when -A argument given, it doesn't remove the hidden files from output
        contents=[content for content in contents if not content["name"].startswith(".")]
    if kwargs["filter"]:
        if kwargs["filter"]=="dir":
            # returns only directories
            contents=[content for content in contents if "contents" in content.keys()]
        elif kwargs["filter"]=="file":
            # returns only files
            contents=[content for content in contents if "contents" not in content.keys()]
        else:
            # returns custom error message on wrong filter
            return f"error: '{kwargs['filter']}' is not a valid filter criteria. Available filters are 'dir' and 'file'"
    if kwargs["t"]:
        # sort the output rows by modifed time, latest first
        contents=sorted(contents, key=lambda sort_key: sort_key["time_modified"], reverse=True)
    if kwargs["r"]:
        # reverses the output rows
        contents=contents[::-1]
    if kwargs["l"]:
        info_table=""
        for content in contents:
            # coverts the epoch time into human readable date-time form
            datetime_obj = datetime.fromtimestamp(content["time_modified"])
            str_time=datetime.strftime(datetime_obj,"%b %d %H:%M")
            content_size=convert_file_size(content["size"])
            row=f'{content["permissions"]} {content_size: >4} {str_time} {content["name"]}'                    
            info_table+=f"{row}\n"
        return info_table.strip()
    # returns only the names if no argument given
    name_list=[content["name"] for content in contents]
    content_names=" ".join(name_list)
    return content_names

def main():
    parser = argparse.ArgumentParser()
    # parse arguments from cli
    # all optional argument's values are False by default
    # becomes True if supplied from cli 
    parser.add_argument("--filter", help="Filters outputs by dir or file")
    parser.add_argument("-r", help="Reverses the output", action='store_true')
    parser.add_argument("-l", help="Prints detail info of the files/dirs", action='store_true')
    parser.add_argument("-t", help="Sorts the output in by time modified", action='store_true')
    parser.add_argument("-A", help="Lists all the files/dirs of a current dir",action='store_true')
    # path is a positional argument, having default value False
    parser.add_argument("path", default=False, nargs="?", help="Prints subdirs/files under given path")
    # coverts all the argument values into dict
    kwargs=parser.parse_args().__dict__
    print(read_info(**kwargs))
    
if __name__=="__main__":
    main()

