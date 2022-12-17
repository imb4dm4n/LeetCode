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
