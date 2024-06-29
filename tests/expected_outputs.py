top_level_list = "LICENSE README.md ast go.mod lexer main.go parser token"
top_level_hidden = ".gitignore LICENSE README.md ast go.mod lexer main.go parser token"

output_of_l = """
drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x   83 Nov 14 11:27 README.md
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x   60 Nov 14 13:51 go.mod
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r--   74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r-- 4096 Nov 14 14:57 token""".strip()

output_of_l_r = """
-rw-r--r-- 4096 Nov 14 14:57 token
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r--   74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 14 15:21 lexer
drwxr-xr-x   60 Nov 14 13:51 go.mod
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x   83 Nov 14 11:27 README.md
drwxr-xr-x 1071 Nov 14 11:27 LICENSE""".strip()

output_of_l_t = """
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 4096 Nov 14 14:57 token
-rw-r--r--   74 Nov 14 13:57 main.go
drwxr-xr-x   60 Nov 14 13:51 go.mod
drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x   83 Nov 14 11:27 README.md""".strip()

output_of_filter_dir= """
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 4096 Nov 14 14:57 token""".strip()

output_of_filter_file="""
-rw-r--r--   74 Nov 14 13:57 main.go
drwxr-xr-x   60 Nov 14 13:51 go.mod
drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x   83 Nov 14 11:27 README.md""".strip()

output_of_path = """
drwxr-xr-x  533 Nov 14 16:03 go.mod
-rw-r--r-- 1622 Nov 17 12:05 parser.go
drwxr-xr-x 1342 Nov 17 12:51 parser_test.go""".strip()

excepted_file_path = "-rw-r--r-- 1622 Nov 17 12:05 parser/parser.go"
excepted_path_error="error: cannot access 'non_existent_path': No such file or directory"
excepted_filter_error = "error: 'folder' is not a valid filter criteria. Available filters are 'dir' and 'file'"