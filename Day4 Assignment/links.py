import re
with open('D:\\Sify documents\\Python training\\Assignment\\Day4 Assignment\\links.txt') as myFile:
    for line in myFile.readlines():
        links = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', line)
        print(links)