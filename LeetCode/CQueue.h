#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/implement-queue-using-stacks/
    // 232. Implement Queue using Stacks
    /*
        用两个栈实现一个 FIFO 队列.必须实现方法  (push, peek, pop, and empty).
        Runtime: 0 ms, faster than 100.00% of C++ online submissions for Implement Queue using Stacks.
        Memory Usage: 7 MB, less than 56.52% of C++ online submissions for Implement Queue using Stacks.

    */
    class MyQueue
    {

    public:
        MyQueue()
        {
        }
        // 把输入移动到输出
        void transfer()
        {
            while (!m_input.empty())
            {
                int tmp = m_input.back();
                m_input.pop_back();
                m_output.push_back(tmp);
            }
        }
        // Pushes element x to the back of the queue.
        void push(int x)
        {
            m_input.push_back(x);
        }
        // Removes the element from the front of the queue and returns it.
        int pop()
        {
            // stack is empty
            if (empty())
                return 0;
            if (m_output.empty())
                transfer();
            int r = m_output.back();
            m_output.pop_back();
            return r;
        }
        // Returns the element at the front of the queue.
        int peek()
        {
            // stack is empty
            if (empty())
                return 0;
            // 输出队列为空, 从输入队列转移过去
            if (m_output.empty())
            {
                transfer();
            }
            return m_output.back();
        }
        //  Returns true if the queue is empty, false otherwise.
        bool empty()
        {
            return m_input.empty() && m_output.empty();
        }

    protected:
        vector<int> m_input, // 存储输入
            m_output;        // 存储输出
    };
}