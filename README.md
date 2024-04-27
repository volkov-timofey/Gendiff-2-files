### Hexlet tests and linter status:
[![Actions Status](https://github.com/volkov-timofey/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/volkov-timofey/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/19bec2a97ef9152e7cd8/maintainability)](https://codeclimate.com/github/volkov-timofey/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/19bec2a97ef9152e7cd8/test_coverage)](https://codeclimate.com/github/volkov-timofey/python-project-50/test_coverage)



# Visual difference 2 files *.json, *.yaml, *.yml

This script that runs in the terminal. 100% Python.

### Installation
Make sure you are running at least Python 3.10.0

Clone the repository and install manually:

```bash
$ git clone https://github.com/volkov-timofey/Gendiff-2-files.git
$ cd Gendiff-2-files
$ make full # build, publish in pip, package-install
```

### Start script
To start the script, run either:
```bash
$ gendiff file_name1 file_name2 -f format_name
```
Formatter:
- stylish - introduced changes in 2 files;
- plain - plain formatter for visual changes in files;
- json - formatter valid json.


Сall for help:


```bash
$ gendiff -h
```
