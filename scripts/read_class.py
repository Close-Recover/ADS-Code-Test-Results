import os
os.chdir('C:/Users/')
import json
import pandas as pd

def extract_error_types(sarif_file):
    with open(sarif_file, 'r') as f:
        data = json.load(f)

    error_types = {}
    for run in data['runs']:
        for result in run['results']:
            error_type = result['ruleId']
            if error_type in error_types:
                error_types[error_type] += 1
            else:
                error_types[error_type] = 1

    return error_types


error_types = extract_error_types('Autoware-23.10-cpp.sarif')


df = pd.DataFrame(list(error_types.items()), columns=['Error Type', 'Count'])


df.to_excel('note_class.xlsx', index=False)
