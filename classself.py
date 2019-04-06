class Calculator:
        def add(self,a,b):
                return a+b
        def sub(self,a,b):
                if(a>b):
                        return a-b
                else:
                        return b-a
        def mul(self,a,b):
                return a*b
        def div(self,a,b):
                return a/b
        def mod(self,a,b):
                return a%b
x=Calculator().add(4,5)
print(x)
y=Calculator().sub(6,7)
print(y)
z=Calculator().mul(3,2)
print(z)
c=Calculator().div(4,2)
print(c)
d=Calculator().mod(5,3)
print(d)
