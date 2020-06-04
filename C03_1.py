__author__ = 'Administrator'
"""
ADT 线性表（list）
Data
    线性表的数据对象集合为｛a1,a2,a3,...,an},每个元素的类型均为DataType。
    其中，
    除第一个元素a1外，每一个元素有且只有一个直接前驱元素，
    除了最后一个元素an外，每一个元素有且只有一个直接后继元素。
    数据元素之间的关系是一对一的关系。
"""
"""
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

# 插入操作
# 初始条件：线性表list_a存在，l<=i<=len(list_a)
# 操作结果：在list_a中第i个位置之前插入新的数据元素e，list_a的长度加1
def ListInsert(list_a,i):
    elemnet = 10
    list_a += [None]
    print(list_a)
    print(len(list_a))
    # 顺序线性表已满
    if None not in list_a:
        return "ERROR"
    # 当i不在范围内时
    if i<1 or i>len(list_a)+1:
        return "ERROR"
    # 如果插入的位置不在末尾
    if i< len(list_a):
        for k in range(len(list_a)-2,i-2,-1):
            list_a[k+1] = list_a[k]
    if i==len(list_a):
        pass
    list_a[i-1] = elemnet
    print(len(list_a))
    return list_a

# 删除操作
# 初始条件：线性表list_a存在，l<=i<=len(list_a)
# 操作结果：删除list_a的第i个元素，并用e返回其值，list_a的长度减1
def ListDelete(list_a,i):
    print(list_a)
    # 线性表为空
    if len(list_a) == 0:
        return "ERROR"
    # 删除的位置不正确
    if i<1 or i>len(list_a):
        return "error"
    e = list_a[i-1]
    if i<len(list_a):
        for k in range(i-1,len(list_a)-1):
            list_a[k] = list_a[k+1]
    if i==len(list_a):
        pass
    # list_a = list_a[:-1]
    del list_a[-1]
    print(e)
    return list_a


if __name__ == "__main__":
    list_a = [1,3,5,7,9]
    list_b = [1,1,2,3,4]
    # print(union_la_lb(list_a,list_b))
    # print(getElem(list_a,3))
    print(ListInsert(list_a,6))
    print(ListDelete(list_a,5))