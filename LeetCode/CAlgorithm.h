#include <queue>
#include <deque>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/fibonacci-number/
    // 509. Fibonacci Number
    /*
        算法实现 计算 斐波那契数列 的第n项
        solution1 : 递归实现 f(n) = f(n-1) + f(n-2)
        Runtime: 11 ms, faster than 37.66% of C++ online submissions for Fibonacci Number.
        Memory Usage: 5.9 MB, less than 42.35% of C++ online submissions for Fibonacci Number.
        solution2 : 自下而上的计算.
        Runtime: 0 ms, faster than 100.00% of C++ online submissions for Fibonacci Number.
        Memory Usage: 5.9 MB, less than 42.35% of C++ online submissions for Fibonacci Number.

    */
    int fib(int n)
    {
        // solution 2
        int cache[2] = {0, 1};
        if (n < 2 && n >= 0)
            return cache[n];
        int fib_1 = 0, fib_2 = 1, fib_n;
        for (int i = 2; i <= n; ++i)
        {
            fib_n = fib_1 + fib_2;
            fib_1 = fib_2;
            fib_2 = fib_n;
        }
        return fib_n;

        // solution 1
        // if (n <= 0)
        //     return 0;
        // if (n == 1)
        //     return 1;
        // return fib(n - 1) + fib(n - 2);
    }
};