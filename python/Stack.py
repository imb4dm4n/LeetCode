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
- https://leetcode.com/problems/longest-palindromic-subsequence/
- 516. Longest Palindromic Subsequence (Medium)
- 问题:  
输入字符串返回最长的回文子序列长度. 子序列是通过把另一个序列在不改变顺序的前提下, 删除一些字符得到的子串.
Input: s = "bbbab"
Output: 4 -> bbbb
- 思路:
replace with your idea.
    '''
    def longestPalindromeSubseq(self, s: str) -> int:

        pass
    
    '''
- https://leetcode.com/problems/validate-stack-sequences/
- 946. Validate Stack Sequences (Medium)
- 问题:  
输入两个数组 pushed popped 都是唯一的值, 若他们可以成为一个空栈的 push 和 pop 操作序列, 返回 true
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
- 思路:
剑指思路: 遍历 pop 序列, 若当前出栈x不在 栈顶, 那么从 push 队列依次入栈, 直到找到目标 x,
若在 push 找不到 y 则返回 False. 最终返回 两个输入是否为空 / Beats 78.60%
    '''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack   =   []
        while len(popped):
            x   =   popped.pop(0)
            # 若没有数据pop或者栈顶不是 x, 则从输入获取
            while (not stack or stack[-1] != x) and pushed:
                stack.append(pushed.pop(0))
            y   =   stack.pop()
            if x != y:
                return False
        return True

    '''
- https://leetcode.com/problems/simplify-path/
- 71. Simplify Path (Medium)
- 问题:  
输入一个路径字符串, 返回简化路径. 规则是:
1.以/开头; 两个文件夹之间必须有一个/分隔;
2.路径结尾没有 /; 路径之间没有.和..符号
- 大神思路: Beats / 66.29%
通过 / 分割出数组列表, 进行遍历, 添加到 stack:
a. 若stack非空且当前元素 是.. , 则 出栈
b. 若当前元素是 . .. 或者空, 则不加入
c. 其他元素则加入 stack
最终 返回 join 的结果, 注意, 任意输入最终至少返回 /
- 思路:
应该是一个栈的思路; 遍历输入的字符, 根据栈顶和当前字符做不同处理
当前字符的可能为 / . ?
a.栈为空, 则把当前字符入栈;
b.栈非空, 根据当前字符和栈顶字符做不同处理
    栈顶:
        /:
            /: 当前字符不入栈
            .: 当前字符入栈
            其他: 当前字符入栈
        .:
            /: 先出栈顶, 再判断栈顶,
            .: 出栈顶, 标记回退一个节点, 开始回退
            其他: 入栈
        其他:
            /: 入栈
            .: 入栈
            其他: 入栈
    '''
    def simplifyPath(self, path: str) -> str:
        stack   =   []
        for ele in path.split("/"):
            if stack and ele == "..":
                stack.pop()
            elif ele not in ['.', '..', '']:
                stack.append(ele)
        return '/' + '/'.join(stack)
        stack   =   []
        consequte_dot   =   0

        def backward(): 
            print("before ", ''.join(stack))
            if len(stack) > 2 and stack[-1] == '.' and stack[-2] == '.':
                stack.append('.')
                return
            while stack and stack[-1] != '/':
                stack.pop()
            if len(stack) > 1:
                stack.pop()
                while stack and stack[-1] != '/':
                    stack.pop()
            # print("back ", ''.join(stack))
        def shink_dot():
            pass

        for c in path:
            if not stack:
                stack.append(c)
                continue
            top     =   stack[-1]
            
            if top == '/':
                if c == '/':
                    continue
                else:
                    stack.append(c)
            elif top == '.':
                if c == '/':
                    stack.pop()
                    stack.append(c)
                elif c == '.':
                    backward()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        if len(stack) > 1 and stack[-1] == '/': # 去除结尾的 /
            stack.pop()
        return ''.join(stack)


    '''
- https://leetcode.com/problems/removing-stars-from-a-string/
- 2390. Removing Stars From a String (Medium)
- 问题:  
输入一个字符串, 随机选一个 * 号, 可以把它最左边的一个非 * 号字母移除, 返回最终没有*号的字符串
- 思路:
本质就是一个栈, 非 * 时字符入栈, * 时出栈顶 / Beats 81.22%
    '''
    def removeStars(self, s: str) -> str:
        stack   =   []
        for c in s:
            if c == '*':
                stack.pop()
                continue
            stack.append(c)
        return ''.join(stack)
    

    '''
- https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
- 1541. Minimum Insertions to Balance a Parentheses String (Medium)
- 问题:  
输入一个括号串, 一个 ( 需要两个 )) 匹配才是平衡的. 返回最少插入几个使得它有效.
Input: s = "(()))"
Output: 1
- 思路:
对于一个 ( 则 )) 的需求量增加2 :need_right += 2,
对于遇到一个 ) 则 need_right -= 1 ,
若 need_right < 0 说明了 ) 太多了, 需要增加左括号 need_left += 1, 同时修正 need_right 变量
    '''

    '''
- https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
- 921. Minimum Add to Make Parentheses Valid (Medium)
- 问题:  
一个有效的括号字符串必须满足其中条件:1.空串 2.可以写成 AB 其中A和B都是有效的 3.写成 (A) , A也是有效的.
输入一个字符串, 可以在任意位置插入 括号, 返回最少需要的括号使得它有效
- 思路:
不能直接统计左右括号的个数, 然后计算差值, 因为他们的位置信息丢失了. ie: )))((( 这种就是无效的 但是个数是匹配的.
因此需要把有效的括号串都剔除掉, 然后返回 左括号和右括号的个数的和.
用 stack_l_bracket 保存 ( , 遇到右括号并且栈非空则出栈, 若栈为空, 则增加 need_left 变量, 最终返回  need_left +  栈的大小 / Beats 11.17%
- 思路2:
不用栈 直接统计数量. need_right 表示需要右括号的数量, need_left 表示左括号需求量. / Beats 93.6%
    '''
    def minAddToMakeValid(self, s: str) -> int:
        # Beats 93.6%
        need_right, need_left   =0,0
        for c in s:
            if c == '(':
                need_right   +=  1 # 需要右括号
            else:
                need_right   -=  1 # 提供了一个右括号因此需求 - 1
                if need_right ==  -1:
                    need_left   +=  1
                    need_right  =   0
        return need_left    +   need_right


        # Beats 11.17%
        stack_l_bracket     =   []
        need_left       =   0
        for c in s:
            if c == '(':
                stack_l_bracket.append(c)
            else:
                if len(stack_l_bracket) == 0:
                    need_left   +=  1
                else:
                    stack_l_bracket.pop()
        return need_left + len(stack_l_bracket)


    '''
- https://leetcode.com/problems/valid-parentheses/
- 20. Valid Parentheses (Easy)
- 问题:  
输入一个字符串包含 (),[],{} 判断它是否有效. 即括号的完整性
- 思路: stack
遇到左括号就入栈, 遇到右括号则出栈, 若栈为空或栈顶非对应的左括号则返回 False. 最终返回 栈是否为空 Beats 39.98%
- 大神
    '''
    def isValid(self, s: str) -> bool:
        if len(s) % 2: # 奇数 Beats 39.98% ...
            return False
        map_brack   =   {'(':')', '{':'}','[':']'}
        stack   =   []
        for c in s:
            if c in map_brack:
                stack.append(c)
            elif not stack or map_brack[stack.pop()] != c:
                return False
        return len(stack) == 0

        stack   =   [] 
        map_brack   =   {'}':'{', ']': '[', ')':'('} 
        for c in s:
            if c in map_brack.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                if map_brack[c] != stack.pop():
                    return False
        return not stack

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
