import os
import sys
from .expected_outputs import *

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
sys.path.append(os.path.join(BASE_PATH,'src'))

from pyls import read_info

# the read_info takes only keyword arguments as dict
def get_arg_dict(inp_dict:dict)->dict:
    arg_dict={
                'A': False,
                'l': False,
                'r': False,
                't': False,
                'filter': None,
                'path': False
            }
    arg_dict.update(inp_dict)
    return arg_dict

# when no arg supplied from cli
# it should lists out the top level
def test_no_args():
    input_dict=get_arg_dict({})
    assert read_info(**input_dict)== top_level_list

# lists out the top level with hidden files
def test_args_a():
    input_dict=get_arg_dict({'A':True})
    assert read_info(**input_dict)==top_level_hidden

# prints detailed info
def test_args_l():
    input_dict=get_arg_dict({'l':True})
    assert read_info(**input_dict)==output_of_l

# # prints detailed info in reverse
def test_args_l_r():
    input_dict=get_arg_dict({'l':True, 'r':True})
    assert read_info(**input_dict)==output_of_l_r

# # prints detailed info sorted by time modified (latest first)
def test_args_l_t():
    input_dict=get_arg_dict({'l':True,'t':True})
    assert read_info(**input_dict)==output_of_l_t

# # prints only dirs, sorted by time modified
def test_args_filter_dir():
    input_dict=get_arg_dict({'l':True,'t':True,'filter':'dir'})
    assert read_info(**input_dict)==output_of_filter_dir

# # prints only files, sorted by time modified
def test_args_filter_file():
    input_dict=get_arg_dict({'l':True,'t':True,'filter':'file'})
    assert read_info(**input_dict)==output_of_filter_file

# prints details info of the path given
# sorted by time modified and reversed output
def test_args_path():
    input_dict=get_arg_dict({'l':True,'t':True,'r':True, 'path':'parser'})
    assert read_info(**input_dict)==output_of_path

# if the path is a file, it prints the file itself
def test_args_file_path():
    input_dict=get_arg_dict({'l':True, 'path':'parser/parser.go'})
    assert read_info(**input_dict)==excepted_file_path

# print error massage if given filter other than 'dir/file'
def test_filter_error():
    input_dict=get_arg_dict({'filter':'folder'})
    assert read_info(**input_dict)==excepted_filter_error

def test_path_error():
    input_dict=get_arg_dict({'path':'non_existent_path'})
    assert read_info(**input_dict)==excepted_path_error




