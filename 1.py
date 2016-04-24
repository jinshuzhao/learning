# -*-coding:utf-8 -*-

# ======================================
print u"=============斜三角============="
for i in range(1, 6):
    for j in range(5-i):
        print " ",
    for k in range(i):
        print "*",
    print
    
for i in range(1, 5):
    for k in range(i):
        print " ",
    for j in range(5-i):
        print "*",
    print

# ======================================
print u"=============到三角============="
for i in range(5):
    for j in range(i):
        print " ",
    for k in range(9-i*2):
        print "*",
    print

# ======================================
print u"=============棱形============="
for i in range(5):
    for j in range(4-i):
        print " ",
    for k in range(2*i+1):
        print "*",
    print

for i in range(4):
    for j in range(i+1):
        print " ",
    for k in range(7-i*2):
        print "*",
    print
