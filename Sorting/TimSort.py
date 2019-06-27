#!/usr/bin/env python3 
# Python3 дээр бичигдсэн гэдгийг илтгэнэ xD
# -*- coding: utf-8 -*-

import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(15):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

def Х_хайлт(дар, утга, эхлэл, төгсгөл):
    if эхлэл == төгсгөл:
        if дар[эхлэл] > утга:
            return эхлэл
        else:
            return эхлэл + 1
    if эхлэл > төгсгөл:
        return эхлэл

    дунд = (эхлэл + төгсгөл) // 2
    if дар[дунд] < утга:
        return Х_хайлт(дар, утга, дунд + 1, төгсгөл)
    elif дар[дунд] > утга:
        return Х_хайлт(дар, утга, эхлэл, дунд - 1)
    else:
        return дунд


def ОрууланЭрэмбэлэх(дар):
    урт = len(дар)

    for гүйгч in range(1, урт):
        утга = дар[гүйгч]
        байр = Х_хайлт(дар, утга, 0, урт - 1)
        дар = дар[:байр] + [утга] + дар[байр:гүйгч] + дар[гүйгч+1:]

    return дар


def нэгтгэ(зүүн, баруун):
    if not зүүн:
        return баруун

    if not баруун:
        return зүүн

    if зүүн[0] < баруун[0]:
        return [зүүн[0]] + нэгтгэ(зүүн[1:], баруун)

    return [баруун[0]] + нэгтгэ(зүүн, баруун[1:])


def ЭрлийзЭрэмбэлэлт(дар):
    хэсэг, Эрэм_хэсэг= [], []
    урт = len(дар)
    шинэ_хэсэг = [дар[0]]
    Эрэм_дар = []

    for i in range(1, урт):
        if i == урт - 1:
            шинэ_хэсэг.append(дар[i])
            хэсэг.append(шинэ_хэсэг)
            break

        if дар[i] < дар[i - 1]:
            if not шинэ_хэсэг:
                хэсэг.append([дар[i - 1]])
                шинэ_хэсэг.append(дар[i])
            else:
                хэсэг.append(шинэ_хэсэг)
                шинэ_хэсэг = []
        else:
            шинэ_хэсэг.append(дар[i])

    for элем in хэсэг:
        Эрэм_хэсэг.append(ОрууланЭрэмбэлэх(элем))

    for элем in Эрэм_хэсэг:
        Эрэм_дар = нэгтгэ(Эрэм_дар, элем)

    return Эрэм_дар
дүүргэ()
print(дар)
print(ЭрлийзЭрэмбэлэлт(дар))
