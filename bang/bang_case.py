# @Time:2021/6/23 4:16
# @Author:testDa
# @File:bang_case.py
# @Reason: python语法

from collections import Iterable
class BangCase():

    # ------迭代-------

    # 判断一个对象是否可以迭代
    def can_iterable(self,obj):
        return isinstance(obj,Iterable)

    # 迭代时需要下标，可以用enumerate函数
    def inerable_enumerate(self):
        for i, value in enumerate(range(10)):
            print('index-->{0},value-->{1}'.format(i,value))

    # -------高阶函数------
    # map():传入两个参数，第一个是一个函数，第二个是Iterator，map可以调用传入的函数与Iterator重新生成一个Iterator对象

    # 计算平方
    def square(self,num):
        return num*num

    def map_case1(self,iter):
        return map(self.square,iter)

    # 不只计算，map()还可根据函数本身执行对应属性，比如把Iterator中的值转换为字符串
    def map_case2(self,iter):
        return map(str,iter)

    # reduce(): reduce函数的效果 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

    # filler():作为一个过滤函数使用，可调用自定义的函数对一个列表元素进行筛选
    # 获取列表中的奇数 根据返回true或者false筛选
    def is_odd(self,num):
        return num%2==1

    def filler_case(self,iter):
        return filter(self.is_odd,iter)

    # sorted():对列表元素排序 key为可选参数，可根据key值进行对应排序 如abs绝对值
    def sorted_case(self,iter,key=None):
        return sorted(iter,key=key)

if __name__ == '__main__':
    bangCase = BangCase()
    print(list(bangCase.sorted_case([3,2,1],abs)))