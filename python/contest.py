import sys

'''
任意一个数都可以表示为
2^a + 2^b + 2^c + ...
39 = 0x27
0010 0111 + 1 = 40 
0010 1000 - 2^3  = 32
0010 0000 - 2^5  = 0
=0
--------
54 = 0x36
0011 0110 + 2
0011 1000 + 8 
0100 0000 - 2^6 
Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.

-----------
把从右往左第一个1左边的0变成1
或者说让 1 慢慢的变成 0 即可.
... 可以减去一个数
'''
def minOperations(n: int) -> int:
    def power_of_2(num:int):
        '''
        若一个数是 2 的 n 次方, 返回True
        '''
        if (num-1) & num == 0:
            return True
        return False

    def make_1_to_0(num:int):
        '''
        把输入的 num 的1变成0
        18-> 0001 0010
        0001 0110 -》 加法
        0010 0100 -> 用减法
        应该是这样, 输入的数字 num 如果连续的1比较多, 那么用加法,
        如果输入的 num 低位 只有 1个1, 那么用减法
        '''
        # print("make {} to zero ".format(num))
        if num&1:
            return 1
        # 找到从右往左第一个1的位置, 返回 2^pos
        pos = 0
        while not num&1:
            num     //=   2
            pos += 1
        # print("pos = {} num = {} {} ".format(pos, num, (num//2)&1))
        if not (num//2)&1:
            # 后面还有1 那么用加法
            while  num&1:
                num     //=   2
                pos += 1
            # print("用加法 ")
            return 2 ** pos
        else:
            # 用减法
            # print("用减法 ")
            return - (2 ** pos)
    count = 1

    while not power_of_2(n):
        x   =  make_1_to_0(n)
        # print("x={} n={} n+x = {}".format(x,n,n+x))
        n +=    x
        count +=    1
    
    return count
    square  =   int(n**0.5)
    low,high    =   square **2, (square+1) **2
    distance    =   min((n-low), (high-n))
    print("low {} high {} distance {}".format(low, high, distance))


# r=minOperations(39)
# print("r={}".format(r))

r=minOperations(54)
print("r={}".format(r))