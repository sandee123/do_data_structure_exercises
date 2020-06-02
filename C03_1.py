__author__ = 'Administrator'
"""
ADT 线性表（list）
Data
    线性表的数据对象集合为｛a1,a2,a3,...,an},每个元素的类型均为DataType。
    其中，
    除第一个元素a1外，每一个元素有且只有一个直接前驱元素，
    除了最后一个元素an外，每一个元素有且只有一个直接后继元素。
    数据元素之间的关系是一对一的关系。

假设一个数据占用C个存储单元，那么线性表中（LOC表示获得存储位置的函数）：
LOC(Ai+1) = LOC(Ai) + C
所以对于第i个数据元素Ai的存储位置可以由A1推算得出：
LOC(Ai) = LOC(A1) + (i-1)*C
每个线性表位置的存入或者去除数据，时间复杂度都是O(1)。随机存取结构。

"""
# 两个线性表集合A和B的并集操作，
# 即，将所有在线性表Lb中但不在La中的数据元素插入到La中
def union_la_lb(list_a,list_b):
    for i in range(len(list_b)):
        if list_b[i] not in list_a:
            list_a.append(list_b[i])
    return list_a

# 获得元素操作,return list_a[i]
# 即，将线性表list_a中第i个位置元素值返回
def getElem(list_a,i):
    element = ""
    if (len(list_a)==0 or i<1 or i>len(list_a)):
        return (False,"ERROR")
    element = list_a[i-1]
    return (True, element)

if __name__ == "__main__":
    list_a = [1,3,5,7,9]
    list_b = [1,1,2,3,4]
    print(union_la_lb(list_a,list_b))
    print(getElem(list_a,3))