## Python program to print the data
d = {1: [101, "Tushant", 25000],
2: [102, "Kiran", 25000],
3: [103, "Paras", 25000],
4: [104, "Prasanjeet", 25000],
5: [105, "Dinesh", 25000],
6: [106, "Hitesh", 25000] }
print ("{:<8} {:<10} {:<15} {:<10}".format('S.No','ID','Name','Salary'))
print("******************************************")
for k, v in d.items():
    id, name, salary = v
    print ("{:<8} {:<10} {:<15} {:<10}".format(k, id, name, salary))