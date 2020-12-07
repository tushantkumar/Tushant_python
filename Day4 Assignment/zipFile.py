from pathlib import Path
from zipfile import ZipFile
#rglob is recursive, glob only specified directory


zipper = ZipFile('d:\\Sify documents\\Python training\\Assignment\\Assign2.zip','w')
path = Path()
for p in path.rglob("*.py"):
    zipper.write(p)
zipper.close()

with ZipFile('d:\\Sify documents\\Python training\\Assignment\\Assign2.zip') as zp:
    print(zp.namelist())
    zp.extractall('test/')
