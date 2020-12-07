import urllib.request
import re

data = urllib.request.urlopen('http://ramakrishnavivekananda.info/')
bData = data.read()
aData = bData.decode('utf-8')
txtData = re.sub('<.*?>','',aData)
print(txtData)
with open('D:\\Sify documents\\Python training\\Assignment\\Day5 Assignment\\htmlToText.txt', 'w', encoding='utf-8') as tFile:
    tFile.write(txtData)