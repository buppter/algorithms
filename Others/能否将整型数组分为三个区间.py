"""
author: buppter
datetime: 2019/9/19 13:49

题目描述：
任意一个整型数组，判断是否可以将数组分为三个区间，每个区间中数值的和相同，区间不能为空。时间复杂度要求为O(N)

解决思路：
(1）先遍历一遍，得到到当前位置为止，数组和是多少。
（2）这样数组最后一个就是总数组的和，取出来，除以3就得该数组三等分后的值应该是多少，记为temp；如果这个值为非int值，那么肯定没法找到切分点，返回False。
（3）接下来再遍历一遍，找到第一个和三等分值temp相等的点，那么就为第一个切分点，同时要判定，这个点后如果剩下的数值小于2个的话，后面两个区间至少有一个为空，不符合题意，返回False
（4）继续往后遍历，此时遍历的时候就要把当前值减去一个temp或者判断当前值是否为2倍的temp，两种方式均可，找到的点后继续执行判定后面剩余多少个，如果直接遍历完了，那么第三个区间此时为空，不符合题意，返回False
（5）若前面全部执行下来还没有返回False，此时，最后一个值肯定是符合题意的，因为一开始就是用他来作为总和除以3得到的三等分后的值。所以就可以直接返回True了。

"""


class Solution:
    def cur_array(self, alist):
        if not alist:
            return False

        if sum(alist) % 3 != 0:
            return False

        tmp = sum(alist) // 3
        carry = 0
        count = 1
        for i in range(len(alist)):
            carry += alist[i]
            if carry == tmp * count:
                count += 1
                if count == 2 and len(alist) - 1 - i < 2:
                    return False
                elif count == 3 and len(alist) - 1 - i < 1:
                    return False
        return True
