# Exercise 6: 
def est_isocele(a,b,c):
    
    return a == b or a == c or b == c 

def est_rectangle(a,b,c):

    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

# Exercise 7:
def petit(a,b):

    return a if a < b else b 

# Exercise 8: 
def absolue(x):

    return abs(x)

# Exercise 9: 
def entier(x):
    
    return x == int(x)

# Exercise 10:
def panir(n):
    
    return n%2 == 0

# Exercise 11: 

def inter1(x):

    return -2 < x < 3

def inter2(x):

    return x <= -3 or x > 5

def inter3(x):

    return (-5 < x <= -3) or (0 <= x <= 2)

def inter4(x):

    return (x > 0 and x != 1) or (x < 0 and x != -1)

