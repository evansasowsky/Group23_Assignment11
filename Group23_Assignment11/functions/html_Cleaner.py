#string html cleaner
import re

def unhtml(string):
    # replace <tag>...</tag>, possibly more than once
    done = False
    while not done:
        temp = re.sub(r'<([^/]\S*)[^>]*>[\s\S]*?</\1>', '', string)
        done = temp == string
        string = temp
    # replace remaining standalone tags, if any
    string = re.sub(r'<[^>]*>', '', string)
    string = re.sub(r'\s{2,}', ' ', string)
    return string.strip()

def cleanup(element):
    if isinstance(element, list):
        for i, item in enumerate(element):
            element[i] = cleanup(item)
    elif isinstance(element, dict):
        for key in element.keys():
            element[key] = cleanup(element[key])
    elif isinstance(element, str):
        element = unhtml(element)

    return element
