import random
import json
import os

count = int(os.getenv("FILE_COUNT") or 10)
# FILE_COUNT=25 python gen_receipts.py

words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)

