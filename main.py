#print('Hello world')
#print( 'welcome to AI and Data science trainings, stay committed ')
#import pandas as pd
#df = pd.read_csv('filee.csv')
#print(df.to_string())
import math
def calculator(x,y,z):
    print( "the summation of your numbers is", x + y + z)
    print( "the multiplication of your numbers is", x * y * z)
    print( "the division f your numbers is", x / y / z)
    return 0
calculator(4,3,9)   

def distanceCalculation(x1,x2,y1,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("distance is", distance)
    #return distance


print("enter x1,y1,x2,y2 respectively")
a =int(input())
b = int(input())
c = int(input())
d = int(input())
distanceCalculation(a,b,c,d)