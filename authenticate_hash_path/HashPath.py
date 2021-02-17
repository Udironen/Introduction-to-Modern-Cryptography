from hashlib import sha256


def find_name_index(my_name,vec_of_names):
    for i in range(len(vec_of_names)):
        if vec_of_names[i] == my_name +"\n":
            return i
    return -1

def comp_path(num_of_names,index):
    path = []
    left = 0
    right = num_of_names - 1
    middle = (right + left) // 2
    while((left < middle) & (middle < right)):
        if index > middle:
            path.append(True)
            left = middle
        else:
            path.append(False)
            right = middle
        middle = (right + left) // 2
    return path

NAME = "Udi Ronen"

file1 = open(r"C:\Users\USER\Documents\מבוא לקריפטוגרפיה מודרנית\תרגילים להגשה\ex3\students.txt",'r')
names = file1.readlines()
file1.close
index = find_name_index(NAME ,names)
num_of_names = len(names)
hash_path = comp_path(num_of_names,index)
hash_bytes = []

file2 = open(r"C:\Users\USER\Documents\מבוא לקריפטוגרפיה מודרנית\תרגילים להגשה\ex3\Udi Ronen.txt",'w')


for i in range(num_of_names):
    names[i] = sha256(names[i].rstrip().encode('ascii'))

while len(names) > 1 :
    for i in range(0,len(names),2):
        arr_bytes = bytearray(names[i].digest())
        arr_bytes.extend(names[i+1].digest())
        hash_bytes.append(sha256(arr_bytes))        
        if (i == index or i+1 == index):
            tmp_index = len(hash_bytes) - 1
            file2.write(arr_bytes.hex())
            if(len(names)>2):
                file2.write("\n")
    index = tmp_index
    names = hash_bytes.copy()
    hash_bytes.clear()
        
file2.close()
testOmer = open(r"C:\Users\USER\Documents\מבוא לקריפטוגרפיה מודרנית\תרגילים להגשה\ex3\Omer Paneth.txt",'r')
testUdi = open(r"C:\Users\USER\Documents\מבוא לקריפטוגרפיה מודרנית\תרגילים להגשה\ex3\Udi Ronen.txt",'r')
omer = testOmer.readlines()
udi = testUdi.readlines()
if len(udi)==len(omer):
    if udi[len(udi)-1] == omer[len(omer)-1]:
        print("success!")
    else:
        print("error in root")
else:
    print("error in num of rows")

    