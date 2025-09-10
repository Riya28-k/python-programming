add = lambda num:num+4  
print(add(5))

square=lambda num:num**2
print(square(5))

multiply = lambda x,y:x*y
print(multiply(5,60))

divide=lambda x,y:x/y
print(divide(1584,13))

checkeven =lambda x:True if x%2==0 else False
print(checkeven(10))
print(checkeven(147))

calc =lambda x,y:(x+y, x*y)
print(calc(5,61))

bodmas = lambda x,y,z: (x*y/z)+(x+y)
print(bodmas(6,48,3))

# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))

