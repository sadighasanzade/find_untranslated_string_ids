#locate your translation files and python script in the same directory

import os
from tokenize import String
path = os.path

key = "<string"

def get_id_from_line(line : str) -> str:
    list = line.split("name=")
    id_container = list[1]
    id_container.replace(" ","")
    return id_container.split('"')[1]


def check_id_from_second_file(id: str):
    second_file.seek(0)
    full_id = '"' + id + '"'
    for line in second_file.readlines():
        full_id.replace(" ","")
        line.replace(" ","")
        if full_id in line:
            return False

    return True

first = input("input the name of first file with extension . for ex main.txt :  ")
second = input("input the name of first file with extension . for ex second.txt :  ")

main_file = open(first, 'r')
second_file = open(second, 'r')
result = open("result.txt", 'w')

counter = 1
for line in main_file.readlines():
    if key in line:
        id = get_id_from_line(line)
        print("checking id : " + id)
        if(check_id_from_second_file(id)):
            result.write(id + "\n")
    counter +=1

print("operation finished ! check result.txt ")



