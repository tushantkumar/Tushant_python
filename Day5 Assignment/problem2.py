import re

con = ''

with open('D:\\Sify documents\\Python training\\Assignment\\Day5 Assignment\\sampleProblem2.html', 'r') as htmFile:
    con = htmFile.read()

con = re.sub('>', ' ', con)
links = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', con)
for link in links:
    print(link)