import math
import random


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
def pair(n):
    
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

# Exercise 12: 

def sign(nombre):
    if nombre > 0:
        return "positif"
    elif nombre == 0:
        return "nul"
    else : 
        return "negatif"
    
# Exercise 13: 

def est_bissextile(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return "bissextile"
    else:
        return "non bissextile"
    
# Exercise 14:

def somme_carre():
    S = 0 
    for i in range(1, 11):
        S += i**2 
    return S

# Exercise 15: 

def somme_puissance1(x):
    S = 0 
    for k in range(4, x+1):
        S += 3**k
    return S

# Exercise 16:

def somme_puissance2(m,n):
    S = 0 
    for z in range(1, n+1):
        S += m**n
    return S

# Exercise 17:
def mult_7(n):
    count = 0 
    for i in range(1, n+1):
        if i % 7 == 0 :
            count += 1
    return count

def mult_7(n): #pas 3 5
    count = 0 
    for i in range(1, n+1):
        if i % 7 == 0 and i % 3 != 0 and i % 5 != 0 :
            count += 1
    return count

# Exercise 18:

def parfait(num):
    sum = 0 
    for i in range(1, num): 
        if num % i == 0 :
            sum += i 
    return sum == num

# Exercise 19: 

def factorielle(n):
    fact = 1
    for i in range(1,n+1):
        fact =  fact*i 
    return fact

# Exercise 20: 
def suite_u(n):
    U = 4
    for i in range(n):
        U = 2 - U/2
    return U 

def suite_f(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    F0, F1 = 0,1 
    for i in range(2,n+1):
        F0, F1 = F1, F0+F1
    return F1

# Exercise 21: 

def algorithme():
    a = 1
    while a < 10: 
        print(a)
        a += 2

# Exercise 22:

k = 0 
while k**2 < 1000:
    k = k + 1
    print(k)

# Exercise 23:

def somme_impairs(n):
    k = 1 
    S = 0 
    while k < n: 
        S += k 
        k += 2 
    return S 

# Exercise 24: 

def na(P):
    mon = 1000
    ans = 0 
    while mon <= P:
        mon *= 1.02 
        ans += 1 
    return ans

# Exercise 25: 

def plus_gd_carre(n):
    return math.floor(math.sqrt(n)) ** 2 # Renvoie la partie entiere de le plus grand entire inferieur a la racine carre 

# Exercise 26:

def comptage(n):
    k = 1 
    count = 0 
    while k**k <= n: 
        count += 1 
        k += 1 
    return count

# Exercise 27 : 
def somme_diff_abs(n):
    S = 0 
    for i in range(1, n+1):
        for j in range(n, n+1):
            S += abs(i - j)
    return S 

# Exercise 28: 

def nb_chiffres(n):
    count = 0 
    while n > 0: 
        n //= 10
        count += 1 
    return count


# Exercise 29: 

def carre_parfait(n):
    racine = math.sqrt(n)
    return racine == int(racine)

def somme_carre(n):
    somme = 0 
    for i in range(1, n+1):
        if carre_parfait(i):
            somme += i 
    return somme

# Exercise 30: 

def pile_or_face():
    return "pile" if random.randint(0,1) == 0 else "face"

# Exercise 31: 

def lancer_de_de()
    return random.randint(1, 6)

# Exercise 32:

def tirage_monopoly():
    return lancer_de_de() + lancer_de_de()

# Exercise 33: 

def simulation(n):
    count = 0 
    for _ in range(n):
        if lancer_de_de() == 0:
            count += 1
    return count/n

# Exercise 34:

def lancer_six():
    count = 0 
    while lancer_de_de() != 6: 
        count += 1 
    return count + 1

# Exercise 35:

def syracuse(n,a):
    if a % 2 == 0: 
        return a // 2
    else:
        return 3*a + 1
    
def vol(a):
    vol_syracuse = [a]
    while a != 1: 
        a = syracuse(len(vol_syracuse), a)
        vol_syracuse.append(a)
    return vol_syracuse

def temp_de_vol(a):
    return len(vol(a)) - 1

def altitude_max(a):
    return max(vol(a))

