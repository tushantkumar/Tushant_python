class Program:
    def __init__(self, file_name):
        self.t = open(file_name, 'r')

    def check(self):
        ...

    def close(self):
        if self.t:
            self.t.close()
            self.t = None


import contextlib
with contextlib.closing(Program('D:\\Sify documents\\Python training\\Assignment\\Day4 Assignment\\links.txt')) as program:
    program.check()