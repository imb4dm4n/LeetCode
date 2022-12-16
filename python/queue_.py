'''
队列算法
'''

class MyQueue:
    '''
- https://leetcode.com/problems/implement-queue-using-stacks/
- 232. Implement Queue using Stacks(easy)
- 问题:  
通过两个栈实现一个 FIFO 先进先出的队列, 实现常见方法
- 思路:
一个栈 stack_save 存储输入, 另一个栈 stack_output 存储输出.
push 时直接入栈到 stack_save
pop 时, 若 stack_output 为空, 从 stack_save pop 到stack_output, 然后再 pop.
peek 和前一步一样, 不过是不要pop而已
Beats 98.54%
    '''
    
    def __init__(self):
        self.stack_output, self.stack_save  =[],[]
        

    def push(self, x: int) -> None:
        self.stack_output.append(x)

    def _transfer(self):
        if self.stack_output.__len__() == 0:
            while self.stack_save.__len__() > 0:
                self.stack_output.append(
                    self.stack_save.pop(0)
                )

    def pop(self) -> int:
        if self.empty():
            return None 
        self._transfer()
        return self.stack_output.pop(0)

    def peek(self) -> int:
        if self.empty():
            return None
        self._transfer()
        return self.stack_output[0]
        

    def empty(self) -> bool:
        return self.stack_output.__len__() == 0 and \
            self.stack_save.__len__() == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()