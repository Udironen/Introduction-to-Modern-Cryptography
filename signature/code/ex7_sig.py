import sys
import hashlib
from random import seed
from random import randint
Nb = 256
NB = Nb//8 
ONE_TIME_SIG_LEN = NB*Nb 
VK_LEN = NB*Nb*2 
SIG_LEN = (2*VK_LEN + ONE_TIME_SIG_LEN) * Nb 

def str_pop(l,n):
    return l[:n],l[n:]

def bits(x):
    bits = []
    for y in x:
        for i in range(8):
            y, b = divmod(y,2)
            bits.append(b)
    return bits
            
def SHA(x):
    return hashlib.sha256(x).digest()

def init_vk(vk_bytes):
    vk = []
    while vk_bytes:
        k0, vk_bytes = str_pop(vk_bytes, NB)
        k1, vk_bytes = str_pop(vk_bytes, NB)
        vk.append((k0, k1))
    return vk

def one_time_ver(vk, msg, sig):
    msg = SHA(msg)
    for b, keys in zip(bits(msg), vk):
        key, sig = str_pop(sig, NB)
        if keys[b] != SHA(key):
            return False
    return True

def ver(vk, msg, sig):
    if len(sig) != SIG_LEN:
        return False
    msg = SHA(msg)
    for b in bits(msg):
        vk0_bytes, sig = str_pop(sig, VK_LEN)
        vk1_bytes, sig = str_pop(sig, VK_LEN)
        vk_sig, sig = str_pop(sig, ONE_TIME_SIG_LEN)
        if not one_time_ver(vk, vk0_bytes + vk1_bytes, vk_sig):
            return False
        vk = init_vk((vk0_bytes, vk1_bytes)[b])
    return True
    
def main(msg, vk_file, sig_file):
    vk = init_vk(open(vk_file,'rb').read())
    sig = open(sig_file,'rb').read()
    print(ver(vk, msg.encode(), sig))   

def init_sk(sk_bytes):
    sk = []
    while sk_bytes:
        k0, sk_bytes = str_pop(sk_bytes, NB)
        k1, sk_bytes = str_pop(sk_bytes, NB)
        sk.append((k0, k1))
    return sk



def gen_sk_vk(prefix,sk):
    key = str(prefix).encode() 
    for i in range(256):
        for j in range(2):
            key+=sk[i][j]
    key = SHA(key) 
    seed(key)
    sk_new=bytes([])
    vk=sk_new
    for i in range(256):
        for j in range(2):
            num=randint(0,(2**64)-1)
            num = SHA(str(num).encode())
            sk_new+=num
            vk+=SHA(num) 
    return sk_new,vk

def write_msg_to_file(msg,sk,file):     
    for i,b in zip(range(256),bits(msg)):
        file.write(sk[i][b])

def gen_sk0_sk1_msg(prefix,sk):
    sk_0, vk_0 = gen_sk_vk(prefix<<1,sk)
    sk_1, vk_1 = gen_sk_vk((prefix<<1)+1,sk)
    msg = vk_0 + vk_1
    return sk_0, sk_1, msg

def gen_sig(sig):
    file = open(f"{sig}.sig", "wb")
    sk = init_sk(open('sk1', "rb").read())
    sig = bits(SHA(sig.encode()))
    prefix=0
    sk_0, sk_1, msg = gen_sk0_sk1_msg(prefix,sk)
    file.write(msg)
    write_msg_to_file(SHA(msg),sk,file)
    for i in range(255):
        prefix = prefix<<1
        if sig[i]==0:
            sk_new = sk_0
        else:
            prefix += 1
            sk_new = sk_1
        sk_0, sk_1, msg = gen_sk0_sk1_msg(prefix,sk)
        file.write(msg)        
        write_msg_to_file(SHA(msg),init_sk(sk_new),file)
        
    file.close()

    
vk2 = init_vk(open("vk2",'rb').read())
siga = open("a.sig",'rb').read()
sigb = open("b.sig",'rb').read()
sigc = open("c.sig",'rb').read()
sigd = open("d.sig",'rb').read()
sige = open("e.sig",'rb').read()
array_sig = [siga,sigb,sigc,sigd,sige]
sk2 = []
for i in range(256):
    sk2.append([-1,-1])

for sig in array_sig:
    message, sig = str_pop(sig, 2*VK_LEN)
    sig_message, sig = str_pop(sig, ONE_TIME_SIG_LEN)
    for i, b, keys in zip(range(256),bits(SHA(message)),vk2):
        key, sig_message = str_pop(sig_message, NB)
        sk2[i][b]=key

end = False
cnt = 0
while(not end):
    end = True
    sk = (str(cnt)).encode()
    sk += bytes(32 - len(sk))
    sk_new = (ONE_TIME_SIG_LEN//32)*sk    
    vk_new = (2*(VK_LEN//32))*SHA(sk)    
    for b, keys in zip(bits(SHA(vk_new)), sk2): 
        if keys[b]==-1:
            cnt += 1
            end = False
            break

gen_sig("Udi")
main("Udi", 'vk1', 'Udi.sig')
gen_sig("Ronen")
main("Ronen", 'vk1', 'Ronen.sig')

file = open("313452542.sig", "wb")
file.write(vk_new)
for b, keys in zip(bits(SHA(vk_new)), sk2):
    file.write(bytes(keys[b]))
for i in range(255):
    file.write(vk_new)
    file.write(sk_new)
file.close()
msg = "313452542"
main(msg, 'vk2', '313452542.sig')

