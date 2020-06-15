import json
from glob import glob
import os

path = 'crops'
#paths = [os.path.abspath(p) for p in glob(os.path.join(path, '*.jpg'))]
paths = glob(os.path.join(path, '*.jpg'))
print(paths)
l = []
for p in paths:
    l.append({'path': p,
              'annotation': ''})
with open('data.json', 'w') as f:
    json.dump(l, f)
