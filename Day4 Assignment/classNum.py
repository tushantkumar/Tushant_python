        
class Num:  
    def __init__(self, x, y): 
        self.x = x 
        self.y = y   

     
    def __add__(self, x, y):
       x1 = self.x + self.x
       y1 = self.y + self.y
       sum = Num (x1,y1)
       return sum     
  
    def __gt__(self, other):  # Overloading the greater than operator
        return self.x > other.x
# Returns true if value of x in the left operand is greater than that in the right one. Returns false otherwise 
   
if __name__ == '__main__':
    sum1 = Num(100, 100)
    sum2 = Num(90, 80)
    if (sum1 > sum2):
        print('sum1 is greater than sum2')  
    else:  
        print('sum1 is not greater than sum2') 

