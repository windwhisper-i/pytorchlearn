with open('C:/Users/wind/Documents/note.js', 'r', encoding = 'utf-8') as f:
    # for line in f.readlines():
    #     print(line.strip())
    # while True:

        line = f.read()
        print(line.strip())


import os

print(os.name)
# print(os.uname())
print(os.environ)


print(os.path.abspath('.'))

print(os.path.split('./note.js'))
print(os.path.splitext(os.path.split('./ss/note.js')[-1]))

import shutil
# shutil.copyfile('C:/Users/wind/Documents/note.js', 'C:/Users/wind/Documents/note2.js')
# os.rename('C:/Users/wind/Documents/note3.js', 'C:/Users/wind/Documents/note.js')

import torch

x = torch.empty(5, 3)
print(x)