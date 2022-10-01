'''
动态规划问题
'''

class Solution:
    '''
    # https://leetcode.com/problems/decode-ways/
    # 91. Decode Ways
    问题: 假设有映射方式: A-Z 映射为 1-26.
    输入一串数字, 返回可能的解码方式. 如输入 226, 返回 3. 因为226可以解码为(2,2,6); (22,6); (2,26)
    思路1: 从前往后计算
    思路2: 动态规划, 从后往前计算
    Runtime: 89 ms, faster than 5.21% of Python3 online submissions for Decode Ways.
    Memory Usage: 13.8 MB, less than 80.35% of Python3 online submissions for Decode Ways.
    '''
    def numDecodings(self, s: str) -> int:
        cur, p, pp  =   0,1,1
        pc          =   ''  # 保存前一个字符
        for c in range(1, s.__len__()+1):
            # print(f"index={c} char={s[-c]} p= {p} pp= {pp}")
            if s[-c] == '0':
                cur     =   0
            else:
                cur     =   p
            # 若当前字符是1, 则前一个字符必须非空才能加上 pp
            # 若当前字符是2, 则前一个字符必须小于 7 才能加pp
            if  s[-c] == '1' and \
                pc != '' or \
                s[-c] == '2' and \
                pc !='' and \
                pc <'7':
                cur +=  pp
            pc      =   s[-c]
            pp      =   p
            p       =   cur
            # print(f"cur={cur}")
            
        return  cur
