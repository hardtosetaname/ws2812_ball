import socket
import struct
import time

HOST = '192.168.4.1'  # The remote host
PORT = 2666  # The same port as used by the server
count = 0
zero = [38,41,82,84,133,22,59,60,108,111,110,39]
one = [38,41,82,84,133]
two = [22,39,38,41,82,83,60,108,111,110,133]
three = [22,39,38,41,82,83,60,84,111,110,133]
four = [22,59,60,83,82,38,41,84,133]
five = [22,39,38,59,82,83,60,84,111,110,133]
six = [22,39,38,59,82,83,60,84,108,111,110,133]
seven = [22,39,38,41,82,84,133]
eight = [22,39,38,59,82,83,60,84,108,111,110,133,41]
nine = [22,39,38,59,82,83,60,84,111,110,133,41]
numbers = {0:zero,1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}

smile = [58,41,113,133,151,152,153]

st1 = [0,1,2,3,4,5,6,7]
st2 = [8,9,10,11,12,13,14,15,16,17,18,19,20,21]
st3 = [22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
st4 = [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
st5 = [60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83]
st6 = [84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109]
st7 = [110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133]
st8 = [134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153]
st9 = [154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171]
st10 = [172,173,174,175,176,177,178,179,180,181,182,183,184,185]
st11 = [186,187,188,189,190,191,192,193]
sts = {1:st1,2:st2,3:st3,4:st4,5:st5,6:st6,7:st7,8:st8,9:st9,10:st10,11:st11}
def All_off():
    for i in range(0, 194):
        ss = struct.pack("BBBB", i, 0, 0, 0)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)

def Fill_coler(r, g, b):
    for i in range(0, 194):
        ss = struct.pack("BBBB", i, r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)

def Circle(r, g, b):
    for ii in range(0,len(st1)):
        ss = struct.pack("BBBB", st1[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st2)):
        ss = struct.pack("BBBB", st2[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st3)):
        ss = struct.pack("BBBB", st3[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st4)):
        ss = struct.pack("BBBB", st4[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st5)):
        ss = struct.pack("BBBB", st5[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st6)):
        ss = struct.pack("BBBB", st6[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st7)):
        ss = struct.pack("BBBB", st7[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st8)):
        ss = struct.pack("BBBB", st8[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st9)):
        ss = struct.pack("BBBB", st9[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st10)):
        ss = struct.pack("BBBB", st10[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st11)):
        ss = struct.pack("BBBB", st11[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    r = 0
    g = 0
    b = 0
    for ii in range(0,len(st1)):
        ss = struct.pack("BBBB", st1[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st2)):
        ss = struct.pack("BBBB", st2[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st3)):
        ss = struct.pack("BBBB", st3[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st4)):
        ss = struct.pack("BBBB", st4[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st5)):
        ss = struct.pack("BBBB", st5[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st6)):
        ss = struct.pack("BBBB", st6[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st7)):
        ss = struct.pack("BBBB", st7[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st8)):
        ss = struct.pack("BBBB", st8[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st9)):
        ss = struct.pack("BBBB", st9[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st10)):
        ss = struct.pack("BBBB", st10[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)
    for ii in range(0,len(st11)):
        ss = struct.pack("BBBB", st11[ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)
    time.sleep(0.5)

def Breath():
    a = 10
    b = 60
    c = 110
    d = 2
    e = 2
    f = 2
    x = 0

    while x < 3:
        a = a + d
        b = b + e
        c = c + f
        Fill_coler(a, b, c)
        time.sleep(0.05)
        if a > 150:
            d = -2
            x += 1
        elif a <= 0:
            d = 2
        if b > 150:
            e = -2
        elif b <= 0:
            e = 2
        if c > 150:
            f = -2
        elif c <= 0:
            f = 2

def show_numbers(i, r, g, b):
    for ii in range(0,len(numbers[i])):
        #print(numbers[i][ii], r, g, b)
        ss = struct.pack("BBBB", numbers[i][ii], r, g, b)
        s.sendall(ss)
    ss = struct.pack("BBBB", 194, 1, 0, 0)
    s.sendall(ss)

def show_smile():
    a1 = 10
    b1 = 60
    c1 = 110
    d1 = 2
    e1 = 2
    f1 = 2
    x1 = 0

    while x1 < 3:
        a1 = a1 + d1
        b1 = b1 + e1
        c1 = c1 + f1
        for iii in range(0, len(smile)):
            ss = struct.pack("BBBB", smile[iii], a1, b1, c1)
            s.sendall(ss)
        ss = struct.pack("BBBB", 194, 1, 0, 0)
        s.sendall(ss)
        time.sleep(0.05)
        if a1 > 150:
            d1 = -2
            x1 += 1
        elif a1 <= 0:
            d1 = 2
        if b1 > 150:
            e1 = -2
        elif b1 <= 0:
            e1 = 2
        if c1 > 150:
            f1 = -2
        elif c1 <= 0:
            f1 = 2



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    All_off()
    time.sleep(1)
    a = 0
    b = 1
    x = 0
    while x < 3:
        Fill_coler(a, a, a)
        time.sleep(0.02)
        a += b
        if a > 120:
            b = -1
        if a <= 0:
            b = 1
            x += 1
    All_off()
    time.sleep(1)
    a = 10
    b = 60
    c = 110
    d = 50
    e = 50
    f = -50
    for pp in range(9, -1, -1):
        show_numbers(pp, a, b, c)
        time.sleep(1)
        show_numbers(pp, 0, 0, 0)
        time.sleep(0.5)
        a = a + d
        b = b + e
        c = c + f
        if a > 110:
            d = -50
            a = 110
        elif a <= 0:
            d = 50
            a = 0
        if b > 110:
            e = -50
            b = 110
        elif b <= 0:
            e = 50
            b = 0
        if c > 110:
            f = -50
            c = 110
        elif c <= 0:
            f = 50
            c = 0
    show_smile()
    Breath()
    Circle(50, 0, 0)

    All_off()







    while count < 10:
        count += 1
        data = s.recv(1024)
        print(data)
        print(str(type(data)))
        print(str(type(count)))
        # data=data+data
        data = data + bytes(count)
        s.sendall(data)

print('Received', repr(data))
