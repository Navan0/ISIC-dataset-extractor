import json
import os
from pprint import pprint
path, dirs, files = next(os.walk(path-to-dataset"))
file_count = int(len(files)/2)
for i in range(file_count):
    print(str(i))
    with open('path-to-dataset/ISIC_0000'+str('%03d' % i)+'.json') as json_file:
        data = json.load(json_file)
    name = str(data['meta']['clinical']['diagnosis'])
    os.rename('path-to-dataset/ISIC_0000'+str('%03d' % i)+'.jpg','path-to-save-directory/'+str(name)+str(i)+'.jpg')
