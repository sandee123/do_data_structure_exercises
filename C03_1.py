__author__ = 'Administrator'
"""
ADT 线性表（list）
Data
    线性表的数据对象集合为｛a1,a2,a3,...,an},每个袁术的类型均为DataType。
    其中，
    除第一个元素a1外，每一个元素有且只有一个直接前驱元素，
    除了最后一个元素an外，每一个元素有且只有一个直接后继元素。
    数据元素之间的关系是一对一的关系。
"""
# 两个线性表集合A和B的并集操作，
# 即，将所有在线性表Lb中但不在La中的数据元素插入到La中
def union_la_lb(list_a,list_b):
    for i in range(len(list_b)):
        if list_b[i] not in list_a:
            list_a.append(list_b[i])
    return list_a

if __name__ == "__main__":
    list_a = [1,3,5,7,9]
    list_b = [1,1,2,3,4]
    print(union_la_lb(list_a,list_b))