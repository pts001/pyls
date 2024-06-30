
# Pyls

A python-cli tool that prints file structure from json file in linux console style.



## Installation

Install Pyls with pip

1. Clone the repo..
2. Install the package using 'pip'.
For exampleIf the project filder is in '/home' directory then. run the following command
```bash
  $pip install /home/user/pyls
```
3. Once installed sucessfully, set-up an enviornment variable where you will put the  input json file.
Example commands-
```bash
  $export DIR_STRUCTURE_FILE=/home/pritam/structure_file.json
```

## Usage/Examples

```shell
1. $pyls
```

Only outputs the top level directories and file names.

Example Output- 
```shell
LICENSE README.md ast go.mod lexer main.go parser token
```
```shell
2. $pyls -A
```
Prints all the files and directories (including
files starting with ’.’)

Example Output - 
```$shell
.gitignore LICENSE README.md ast go.mod lexer main.go parser token
```

```shell
3. $pyls -l
```
Prints detailed info of files and directories

Example Output - 

```shell
-rw-r--r-- 1071 Nov 14 11:27 LICENSE
-rw-r--r-- 83 Nov 14 11:27 README.md
drwxr-xr-x 4096 Nov 14 15:58 ast
-rw-r--r-- 60 Nov 14 13:51 go.mod
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 17 12:51 parser
drwxr-xr-x 4096 Nov 14 14:57 token

```

```shell
4. $pyls -l -r
```
Reverses the outputs

```shell
5. $pyls -l -t
```
Sorts the output by time modified, latest first

```shell
6. $pyls -l -filter={dir/filter}
```
The output can be filtered by directories or files. Two choices are - "filter", "dir".

```shell
7. $pyls -l {path_to_directory/file}
```
The path arg can be used to get content of any specific directory.


Note - The multiple arguments can be chained together to get desired output.