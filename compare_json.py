import json
import pandas as pd
from deepdiff import DeepDiff
import datetime

def load_and_sort_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

source_data = load_and_sort_json('Compare1.txt')
target_data = load_and_sort_json('Compare2.txt')

diff = DeepDiff(source_data, target_data, ignore_order=True)

rows = []

if diff == {}:
    print("The JSON data in the files is the same.")
else:
    print("The JSON data in the files is different.")
    
if 'dictionary_item_added' in diff:
    for item in diff['dictionary_item_added']:
        rows.append({
            "Key": item,
            "Source Tenant": None,
            "Target Tenant": diff['dictionary_item_added'][item]
        })
    
if 'dictionary_item_removed' in diff:
    for item in diff['dictionary_item_removed']:
        rows.append({
            "Key": item,
            "Source Tenant": diff['dictionary_item_removed'][item],
            "Target Tenant": None
        })
    
if 'values_changed' in diff:
    for key, change in diff['values_changed'].items():
        rows.append({
            "Key": key,
            "Source Tenant": change['old_value'],
            "Target Tenant": change['new_value']
        })

df = pd.DataFrame(rows, columns=["Key", "Source Tenant", "Target Tenant"])

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"tenant_data_comparison_{now}.csv"
df.to_csv(output_file, index=False)
print(f"Comparison saved to '{output_file}'")

        