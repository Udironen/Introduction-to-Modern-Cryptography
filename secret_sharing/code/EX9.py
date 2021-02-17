from editImage import *
import random
 
WHITE = 255
BLACK = 0

def multiply_MATS(lhs,rhs):

    n,m = lhs.dim()
    mat = Matrix(n,m)

    for i in range(n):
        for j in range(m):
            mat[i,j] = lhs[i,j] and rhs[i,j]  
    return mat        

def get_dfrnt_ij(num):
    list_ij = list()
    random_nums = random.sample(range(0,4),num)
    for r in random_nums:
        list_ij.append(((r//2) % 2, r%2))
    return list_ij    


def random_2on2_mat(num, color):
    mat = Matrix(2,2,BLACK)
    rand_ij_s = get_dfrnt_ij(num)
    for ij in rand_ij_s:
        mat[ij] = color
    return mat


def encode(A, B, C):    
    print("hii")
    n,m = C.dim()
    print("hii")
    share1 = Matrix(2 * n, 2 * m, BLACK)
    share2 = Matrix(2 * n, 2 * m, BLACK)
    secret = Matrix(2 * n, 2 * m, BLACK)
    for i in range(n):
        for j in range(m):
            flag = True
            
            while(flag):
                
                if A[i,j] == WHITE:                    
                    random_2on2_A = random_2on2_mat(2,WHITE)
                else:
                    random_2on2_A = random_2on2_mat(1,WHITE)
                

                if B[i,j] == WHITE:
                    random_2on2_B = random_2on2_mat(2,WHITE)
                else:
                    random_2on2_B = random_2on2_mat(1,WHITE)
                random_2on2_C =  Matrix(2,2,BLACK)
                if C[i,j] == WHITE:
                    random_2on2_C = random_2on2_mat(1, WHITE)               
                
                if multiply_MATS(random_2on2_A, random_2on2_B) == random_2on2_C:
                    flag = False
                #for k in range(2):
                #    for t in range(2):
                #        if random_2on2_C[k,t] == WHITE:
                #            if random_2on2_A[k,t] != WHITE or random_2on2_B[k,t] != WHITE:
                #                flag = True
                #        else:
                #            if random_2on2_A[k,t] == WHITE and random_2on2_B[k,t] == WHITE:
                #                flag = True
                #print("==============================")
            print("i,j: ",i,", ",j)
            print(random_2on2_A)
            print(random_2on2_B)
            print(random_2on2_C)
            print("==============================")                   
                
           

            for t in range(2):
                for k in range(2):
                        share1[2*i + k, 2*j + t] = random_2on2_A[k,t]    
                        share2[2*i + k, 2*j + t] = random_2on2_B[k,t] 
                        secret[2*i + k, 2*j + t] = random_2on2_C[k,t]    
            
            print(share1[2*i, 2*j],",",share1[2*i, 2*j + 1])   
            print(share1[2*i + 1, 2*j],",",share1[2*i +1, 2*j +1])   
            print(share2[2*i, 2*j],",",share2[2*i, 2*j + 1])   
            print(share2[2*i + 1, 2*j],",",share2[2*i +1, 2*j + 1])
            print(secret[2*i, 2*j],",",secret[2*i, 2*j + 1])   
            print(secret[2*i + 1, 2*j],",",secret[2*i +1, 2*j + 1])   
            
            print("==============================")                         

    return [share1,share2,secret]                 


      
                
path = "C:\\Users\\USER\\Documents\\מבוא לקריפטוגרפיה מודרנית\\תרגילים להגשה\\ex9\\"

image2bitmap( path +    "dog.jpeg")
image2bitmap( path +    "pola.jpeg")
image2bitmap( path +    "inbal.jpeg")
                  
             
           


A = Matrix.load(path + "dog.bitmap")
B = Matrix.load(path + "pola.bitmap")
C = Matrix.load(path + "inbal.bitmap")

list = encode(A, B, C)

decode = multiply_MATS(list[0] , list[1])

list[0].save(path+"A_share.bitmap")
bitmap2image(path+"A_share.bitmap")

list[1].save(path+"B_share.bitmap")
bitmap2image(path+"B_share.bitmap")

list[2].save(path+"C_share.bitmap")
bitmap2image(path+"C_share.bitmap")

decode.save(path+"decode.bitmap")
bitmap2image(path+"decode.bitmap")

C.save(path+"C_test.bitmat")
bitmap2image(path+"C_test.bitmat")
