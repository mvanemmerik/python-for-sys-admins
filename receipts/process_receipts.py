import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already  exist.")

# create a list of new receipts and their path
receipts =  glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0
count  = 0

for path_to_file in receipts:
    with open(path_to_file) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # "./new/receipt-1.json".split('/') => ['.', 'new', 'receipt-1.json']
    name =  path_to_file.split("/")[-1] # grab last item in list
    destination = f"./processed/{name}"
    shutil.move(path_to_file, destination)
    print(f"moved '{path_to_file}' to '{destination}'")
    count +=  1

print(f"Receipt total for {count} receipts is ${subtotal:.2f}.")

