# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:45:25 2022

@author: HP
"""

myfile = open("E:/road_pathole/training/1/1.txt")
for line in myfile:
    print(line)
myfile.close()

# # myfile = open("1.txt")
# # for line in myfile:
# #     print(line.strip())
# # myfile.close()

# from pathlib import Path

# path_to_file = '1.txt'
# path = Path(path_to_file)

# if path.is_file():
#     print(f'The file {path_to_file} exists')
# else:
#     print(f'The file {path_to_file} does not exist')