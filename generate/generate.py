import os
import json
from setting import WORKING_DIR
from testing_file import operation

input_file = os.path.join(WORKING_DIR, "input", "input_url.txt")
input_json_file = os.path.join(WORKING_DIR, "config", "input.json")


def read_config(file_path):
    with open(file_path) as fp:
        data_dict = json.load(fp)
    return data_dict


def check_urls(input_urls_path, urls):
    with open(input_urls_path) as fp:
        lines = fp.readlines()
        for line in lines:
            domain = line.split('/')
            if domain[2] in urls:
                url_input = line.strip()
                operation(url_input)
            else:
                print("\n")
                print(domain[2], "is not supported")


supported_urls = read_config(input_json_file)


check_urls(input_file, supported_urls["supported_sites"])
