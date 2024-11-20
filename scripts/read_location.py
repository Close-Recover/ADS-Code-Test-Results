import os
os.chdir('C:/Users/')
import json
import pandas as pd

def extract_file_paths(sarif_file):
    with open(sarif_file, 'r') as f:
        data = json.load(f)

    file_paths = {}
    for run in data['runs']:
        for result in run['results']:
            for location in result['locations']:
                file_path = location['physicalLocation']['artifactLocation']['uri']
                if file_path in file_paths:
                    file_paths[file_path] += 1
                else:
                    file_paths[file_path] = 1

    return file_paths


file_paths = extract_file_paths('apollo-7.0.0-cpp.sarif')


df = pd.DataFrame(list(file_paths.items()), columns=['File Path', 'Count'])


df.to_excel('note_location.xlsx', index=False)
