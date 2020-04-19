from random import choice
from math import gcd
import random
import base64
import time
import os
global head_A, fin_A, Head_B, fin_B
head_A = 2**11
fin_A = 2**12


# 生成小素数表
def prime():
    list_A = []
    i = 2
    for i in range(2, 1000):
        j = 2
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            list_A.append(i)
    return list_A

# 产生奇数


def jishu(A, B):
    while (1):
        num = random.randint(A, B)
        while (num % 2 != 0):
            return num

# 用小素数试除


def shichu(list1, num):
    #index = 0
    for member in list1:
        if num % member == 0:
            # print(str(num)+"%"+str(member)+"="+"0")
            return shichu(list1, num + 2)
        else:
            #print(str(num) + "%" + str(member) + "=" + str(num%member))
            continue
    return num

# MILLER_RABIN


def Miller(num):  # Miller Rabin算法
    number = num - 1
    s = 0
    while True:
        if number % 2 == 0:
            s += 1
            number = int(number / 2)
        else:
            t = number
            break
    rand = random.randint(2, num - 2)  # rand(1<=rand<=n-1)python3.X包括左右的数
    b = squMul(rand, num, t)
    if b % num == 1 or b % num == num - 1:
        return 1
    for i in range(0, s - 1):  # range不包括右边
        b = (b * b) % num
        if b == num - 1:
            return 1
    return 0


def create_pq(list1, head, fin):
    js = jishu(head_A, fin_A)
    print("产生奇数：" + str(js))
    print("-------小素数试除--------")
    js = shichu(list1, js)
    print("-------Miller—Rabin检验5次--------")
    for x in range(5):
        if Miller(js) == 0:
            print("是合数，重新产生奇数")
            js = create_pq(list1, head, fin)
    return js

# 辗转相除法


def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = exgcd(b, a % b)
        return g, y, x - a // b * y
# 模重复平方算法


def ModSqu(b, n, m):  # b^m mod n
    box = str(bin(n)).replace("0b", "")
    s = 1
    length = len(box)
    for index, value in enumerate(box):
        if int(box[length - index - 1]) == 1:
            s = (s * b) % m
        b = (b * b) % m
    return s
# 平方乘算法


def squMul(s, n, e):  # s^e mod n
    b = str(bin(e)).replace("0b", "")
    n1 = []
    for i in range(0, len(b)):
        n1.append(b[i])
    y = 1
    for i in range(0, len(n1)):
        y = (y * y) % n
        if int(n1[i]) == 1:
            y = (y * s) % n
    return y


def squMul_C2(s, n, e, m):  # m*s^e mod n
    b = str(bin(e)).replace("0b", "")
    n1 = []
    for i in range(0, len(b)):
        n1.append(b[i])
    y = 1
    for i in range(0, len(n1)):
        y = (y * y) % n
        if int(n1[i]) == 1:
            y = (y * s) % n
    y = (y * m) % n
    return y


def primitiveRoots(primeNum):
    possible_set = {num for num in range(1, primeNum) if gcd(num, primeNum)}
    root_list = [base for base in range(1, primeNum) if
                 possible_set == {pow(base, power, primeNum) for power in range(1, primeNum)}]
    return root_list


'''
def ElGamal_encrypt(y,k,p,message):
    with open((os.path.join(message)),'r') as f:
        data = f.readlines()
        for line in data :
            odom = line.split()
            num = map(int,odom)
            lst = (list(num))
    Len = len(lst)
    for i in range(0,Len):
       list[i]= squMul_C2(y,p,k,list[i])#C1 = g^k mod p
          #squMul(y,k,p)/message #c2 = my^k mod p
    print(lst)
    with open((os.path.join('enfile_copy.txt')),'w') as f:
        for j in range(0,Len):
            f.write(str(lst[j]))
            f.write((''))
'''


def file_encrypt():
    global Newfile
    filename = input("请输入欲转换文件名：")
    Newfile = ToBase64( 
        f"E:/code/Elg/file_data/{filename}",   #这里要用绝对路径
        f'E:/code/Elg/file_data/{filename}_base64.txt')  # 文件转换为base64
    go = False
    time.sleep(5)
    # print(Newfile)
    return Newfile


def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()
        print("Complete!")
        return fout.name


if __name__ == "__main__":
    # print("-------生成1~1000所有小素数--------")
    list1 = prime()
    # print(list(list1))
    # print("-------------------------------产生p：----------------------------------")
    p = create_pq(list1, head_A, fin_A)
    # print("确实是素数，成功获得素数P:"+str(p))
    # print("--------接下来生成p的原根g------")
    #print('Primitive Roots of ' + str(p) + " are: ")
    roots = primitiveRoots(p)
    print(roots)
    g = choice(roots)
    #print("----随机抽取一个 p 的本原根 g="+str(g))
    x = random.randint(1, p - 1)
    #print("----在 [1~p-1] 中随机抽取 x="+str(x))
    y = ModSqu(g, p, x)
    #print("----获取 y = g^x (mod p)="+str(y))
    print(
        "----公钥获取完毕！！\n公钥为{g=" +
        str(g) +
        ",y=" +
        str(y) +
        ",p=" +
        str(p) +
        "}")

    # print("[开始进行加密]")
    k = random.randint(1, p)
    print("----在 [1~p] 中随机抽取 k=" + str(k))

    # coding=UTF-8
    filename = 'public_key.txt'
    with open(filename, 'w') as file_object:
        file_object.write(
            "g = " +
            str(g) +
            "\ny = " +
            str(y) +
            "\np = " +
            str(p))

    filename = 'private_key.txt'
    with open(filename, 'w') as file_object:
        file_object.write(
            "g = " +
            str(g) +
            "\nx = " +
            str(x) +
            "\np = " +
            str(p))
    print("密钥文件已写入")

    while True:  # 相当于主程序了。。。
        print("\n这是一个加解密文件程序，请按照提示输入！\n")
        print("请选择：\n1.加密文件  2.解密文件 3.退出")
        select = input()
        if select == str(1):
            Newfile = file_encrypt()
            break
            # elif select == 2:
            # file_decrypt()
            break
        else:
            break

    print("现在进行加密,计算出c1")
    C1 = ModSqu(g, p, k)
    print('c1=' + str(C1))
    Newfile
    # 读取加密文档
    with open((os.path.join(Newfile)), 'r') as f:
        data = f.readlines()
        for line in data:
            odom = line.split()
            num = map(int, odom)
            lst = (list(num))
    Len = len(lst)
    for i in range(0, Len):
        list[i] = squMul_C2(y, p, k, list[i])  # C1 = g^k mod p
        # squMul(y,k,p)/message #c2 = my^k mod p
    print(lst)
    with open((os.path.join('enfile_copy.txt')), 'w') as f:
        for j in range(0, Len):
            f.write(str(lst[j]))
            f.write((''))
