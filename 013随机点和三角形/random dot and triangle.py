# -*- coding: utf-8 -*-
import random
from collections import deque


q = deque()
i = 0
while i < 1000:
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)
    z = [x, y]
    if z not in q:
        q.append(z)
        i += 1


# Generate three random dots, and the three dots can make a triangle
def three_dot():
    a = random.choice(q)
    b = random.choice(q)
    c = random.choice(q)
    if a[0] == b[0] == c[0] or a[1] == b[1] == c[1]:
        return three_dot()
    else:
        return [a, b, c]


# Calculate 'k' and 'a' in an equations
def equations(dot1, dot2):
    k = (dot1[1] - dot2[1])/(dot1[0] - dot2[0])
    a = dot1[1] - k*dot1[0]
    return k, a


dots = three_dot()
dots = sorted(dots, key=lambda item: item[1])  # make sure dots[0] has smallest 'y'
print("The triangle's three dots are {0}, {1} and {2}".format(dots[0], dots[1], dots[2]))
k1, a1 = equations(dots[0], dots[1])
k2, a2 = equations(dots[0], dots[2])
k3, a3 = equations(dots[1], dots[2])


def sort_dots(lists):
    global k1, a1, k2, a2, k3, a3
    global dots
    inside_list = []
    if dots[1][0] <= dots[0][0] <= dots[2][0] or dots[1][0] >= dots[0][0] >= dots[2][0]:
        for i in lists:
            if k3*i[0] + a3 > i[1] > k1*i[0] + a1 and i[1] > k2*i[0] + a2:
                inside_list.append(i)
    if abs(k1) > abs(k2):
        m = k1
        k1 = k2
        k2 = m
        n = a1
        a1 = a2
        a2 = n
    if k1 > 0:
        if k3 > 0:
            for i in lists:
                if k2 * i[0] + a2 > i[1] > k1 * i[0] + a1 and i[1] > k3 * i[0] + a3:
                    inside_list.append(i)
        else:
            for i in lists:
                if k2 * i[0] + a2 > i[1] > k1 * i[0] + a1 and i[1] < k3 * i[0] + a3:
                    inside_list.append(i)
    else:
        if k3 >= 0:
            for i in lists:
                if k2 * i[0] + a2 > i[1] > k1 * i[0] + a1 and i[1] < k3 * i[0] + a3:
                    inside_list.append(i)
        else:
            for i in lists:
                if k2 * i[0] + a2 > i[1] > k1 * i[0] + a1 and i[1] > k3 * i[0] + a3:
                    inside_list.append(i)
    return inside_list


answer = sort_dots(q)
print('The following dots is inside the triangle, and the num is {0}'.format(len(answer)))
print(answer)
