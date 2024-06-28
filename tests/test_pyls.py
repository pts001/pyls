from ..pyls import read_info
from .expected_outputs import *

# the read_info takes only keyword arguments as dict
arg_dict={
            'A': False,
            'l': False,
            'r': False,
            't': False,
            'filter': None,
            'path': False
        }

# when no arg supplied from cli
# it should lists out the top level
def test_no_args():
    assert read_info(**arg_dict)== top_level_list

# lists out the top level with hidden files
def test_args_a():
    arg_dict['A']=True
    assert read_info(**arg_dict)==top_level_hidden

# prints detailed info
def test_args_l():
    arg_dict['l']=True
    assert read_info(**arg_dict)==output_of_l

# prints detailed info in reverse
def test_args_l_r():
    arg_dict['l']=True
    arg_dict['r']=True
    assert read_info(**arg_dict)==output_of_l_r

# prints detailed info in reverse sorted by time modified
def test_args_l_r_t():
    arg_dict['l']=True
    arg_dict['r']=True
    arg_dict['t']=True
    assert read_info(**arg_dict)==output_of_l_r_t

# prints only dirs
def test_args_filter_dir():
    arg_dict['l']=True
    arg_dict['filter']='dir'
    assert read_info(**arg_dict)==output_of_filter_dir

# prints only files
def test_args_filter_file():
    arg_dict['l']=True
    arg_dict['filter']='file'
    assert read_info(**arg_dict)==output_of_filter_file

# prints details info of the path given
def test_args_path():
    arg_dict['l']=True
    arg_dict['path']='parser'
    assert read_info(**arg_dict)==output_of_path
