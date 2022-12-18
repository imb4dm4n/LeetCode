'''
使用到栈相关的算法
'''
from typing import List

class Solution:
    '''
- replace with url
- replace with problem title
- 问题:  
replace with problem description
- 思路:
replace with your idea.
    '''

    '''
- https://leetcode.com/problems/daily-temperatures/
- 739. Daily Temperatures(medium)
- 问题:  
输入一组温度, 返回数组, 每一个表示在 第 i 天需要等待多少天才能得到更温暖的温度.
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
73->74 等待1天
74->75 等待1天
75->76 等待4天 ...
- 大神思路:
用一个递减的栈存储 气温和对应索引, 若栈非空, 用当前的气温对比栈顶, 若高于栈顶, 那么就可以计算一次 气温升高时间间隔.
Beats 57.29%
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 思路2 根据前一轮计算结果
        ret     =   [0] * temperatures.__len__()
        stack   =   []  # (id, temp)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackId, stackTemp  =   stack.pop()
                ret[stackId]    =   i   -   stackId
            stack.append((i,temp))
        
        return  ret
    '''
- https://leetcode.com/problems/evaluate-reverse-polish-notation/
- 150. Evaluate Reverse Polish Notation (medium)
- 问题:  
输入一个表达式, 计算它的结果: 
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
- 思路:
用一个栈存储数字结果, 遍历输入的字符, 遇到操作符时, 把栈顶两个数pop出来, 
根据运算符计算结果写会到栈顶. 结束时返回栈顶的值.
Beats 90.29%
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stack   =   []
        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def mul(a,b):
            return a*b
        def div(a,b):
            return int(a/b)
        operands    =   {'+':add, '-':sub, '*':mul, '/':div}
        for tok in tokens:
            if tok in operands.keys():
                # eval the operand
                b   =   stack.pop(-1)
                a   =   stack.pop(-1)
                stack.append(
                    operands[tok](a,b)
                )
            
            else:
                # transform string into number
                try:
                    stack.append(int(tok))
                except Exception as e:
                    print(e)

        return stack[0]
