import math
import random
def comp_DL(g, p, N):
    a,b = get_a_b(g, p, N)
    x = (a+b) %(p-1)
    return x

def get_a_b(g, p, N):
    sqp2 = 2 * math.sqrt(p)
    map = {}
    i=0
    while i < sqp2 :
        i += 1
        a = random.randint(0, p-1)
        A = pow(g, a, p)
        B = fastlinearcongruence(A, N, p)
        b = map.get(B,-1)
        if b == -1:           
            map.update({A: a})
        else:
            print("number of iterations: ", i, "is it smaller than sqrt(p)? ", i < math.sqrt(p))
            return a,b
    return -1,-1
            

def get_B(p, A, N):
    return 0

def fastlinearcongruence(powx, divmodx, N):  
 x, y, z = egcditer(powx, N)  
 answer = (y*divmodx)%N  

 if x > 1:  
    powx//=x  
    divmodx//=x  
    N//=x       
    x, y, z = egcditer(powx, N)   
    answer = (y*divmodx)%N  
   
 answer = (y*divmodx)%N   
 return answer 
 
def egcditer(a, b):  
  s = 0  
  r = b  
  old_s = 1  
  old_r = a  
  quotient = 0 
 
  while r!= 0:  
    quotient = old_r // r  
    old_r, r = r, old_r - quotient * r  
    old_s, s = s, old_s - quotient * s  
    
  if b != 0:  
    bezout_t = quotient = (old_r - old_s * a) // b     
  else:  
    bezout_t = 0  
    
  return old_r, old_s, bezout_t


p = 461733370363
g = 2
N = 313452542
##x = comp_DL(g, p, N)
##file1 = open(r"C:\Users\USER\Documents\מבוא לקריפטוגרפיה מודרנית\תרגילים להגשה\ex5\313452542.txt",'w')
##print(x,file=file1)
##file1.close()
##print("my computation: ", x, " does x < p-1 ? ", x < p-1)
test = pow(g,129193404153,p)

print("pow(g,x,p) = ", test, " is it true? ", test == N  )

## 129193404153