import os
import glob
import json
import shutil
import re
import math

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already  exist.")

# create a list of new receipts and their path
# receipts =  glob.glob('./new/receipt-[0-9]*.json')

# even numbered receipts only using a regular expression
receipts = [f for  f in glob.iglob('./new/receipt-[0-9]*.json') if  re.match('./new/receipt-[0-9]*[24680].json',f)]

subtotal = 0.0
count  = 0

for path_to_file in receipts:
    with open(path_to_file) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # "./new/receipt-1.json".split('/') => ['.', 'new', 'receipt-1.json']
    # name =  path_to_file.split("/")[-1] # grab last item in list
   
    # destination = f"./processed/{name}"
    # replace the 'new' with 'processed'
    destination = path_to_file.replace('new', 'processed')
    shutil.move(path_to_file, destination)
    print(f"moved '{path_to_file}' to '{destination}'")
    count +=  1

print(f"Receipt total for {count} receipts is ${subtotal:.2f}.")
print(f"Receipt total for {count} receipts is ${math.ceil(subtotal)}. -ceil")
print(f"Receipt total for {count} receipts is ${math.floor(subtotal)}. -floor")
print(f"Receipt total for {count} receipts is ${round(subtotal, 2)}. -round")

receipt_average = subtotal/count
print(f"Average: ${round(receipt_average, 2)}. -round")
