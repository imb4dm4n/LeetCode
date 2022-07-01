#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <map>
using namespace std;
namespace letcoode
{
    // https://leetcode.com/problems/number-of-1-bits/
    // 191. Number of 1 Bits
    /*
    给定一个整数 n, 计算 它的二进制表示中有多少个 1 .
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
    Runtime: 2 ms, faster than 61.15% of C++ online submissions for Number of 1 Bits.
    Memory Usage: 6 MB, less than 47.57% of C++ online submissions for Number of 1 Bits.
    Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of 1 Bits.
    Memory Usage: 6 MB, less than 47.57% of C++ online submissions for Number of 1 Bits.
    Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of 1 Bits.
    Memory Usage: 6 MB, less than 47.57% of C++ online submissions for Number of 1 Bits.
    */
    int hammingWeight(uint32_t n)
    {
        // -------------- solution 3 : 0ms
        int count = 0;
        while (n)
        {
            ++count;
            n = (n - 1) & n;
        }
        return count;
        // -------------- solution 2 : 0ms
        // unsigned int flag=1, count =0;
        // while (flag)
        // {
        //     if(flag&n)
        //     ++count;
        //     flag<<=1;
        // }
        // return count;

        // -------------- solution 1 : 2ms
        // int count = 0;
        // while (n)
        // {
        //     if (n & 1)
        //         ++count;
        //     n >>= 1;
        // }
        // return count;
    }
};