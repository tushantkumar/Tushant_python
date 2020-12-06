import re

with open('D:\\Sify documents\\Python training\\Assignment\\Day4 Assignment\\regex.html') as myFile:
    with open("D:\\Sify documents\\Python training\\Assignment\\Day4 Assignment\\myRegexFile.txt", "w") as writeFile:    
        path = re.compile(r'<[^>]+>')
        for line in myFile.readlines():
            res = re.sub(path,'',line)
            writeFile.writelines(res)
            print(res)

