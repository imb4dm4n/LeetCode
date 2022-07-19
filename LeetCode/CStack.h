#include <queue>
#include <deque>
#include <vector>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/min-stack/
    // 155. Min Stack
    /*Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    思路: 入栈的时候，保存入栈的最小值。 不过可以发现，若最小值出栈了，那么次小的值，就不知道了。

    为了解决这个问题，需要再每次入栈时，用一个辅助的栈保存最小值的状态。 每一次入栈都对应着一个最小值，只有这样，当出栈时，才可以得到前一个状态的最小值。
    Runtime: 25 ms, faster than 84.38% of C++ online submissions for Min Stack.
    Memory Usage: 16.5 MB, less than 31.27% of C++ online submissions for Min Stack.
    */
    class MinStack
    {
    private:
        vector<int> m_stack;
        vector<int> m_aux;

    public:
        MinStack()
        {
        }

        void push(int val)
        {
            m_stack.push_back(val);
            if (m_aux.empty())
            {
                // init the stack and auxiliraity stack
                m_aux.push_back(val);
                return;
            }
            // None empty case:
            int cur_min = m_aux.back();
            if (val < cur_min)
                // push new min to aux stack
                m_aux.push_back(val);
            else
                // maintain the min num of the stack
                m_aux.push_back(cur_min);
        }

        void pop()
        {
            if (m_stack.empty())
                return;
            m_aux.pop_back();
            m_stack.pop_back();
        }

        int top()
        {
            return m_stack.back();
        }

        int getMin()
        {
            return m_aux.back();
        }
    };
}