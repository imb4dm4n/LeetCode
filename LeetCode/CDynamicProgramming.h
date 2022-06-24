#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <map>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/maximum-subarray/
    // 53. Maximum Subarray
    /*
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    1 <= nums.length <= 105
    -10^4 <= nums[i] <= 10^4
    思路: 
    对于每一个数字, 我们可以选择 加入 或 不加入
        加入  :  则后序所有的数字都加入
        不加入:  
    // 类似求最长回文, 只不过这里是累加出最大的值而已.
    // 初始化矩阵, 把对角线的值填上去. 然后从下往上, 从左往右计算和,找出最大值. (超时)
    Input:
    [5,4,-1,7,8]
    Output:
    15
    Expected:
    23
    */
    int maxSubArray(vector<int> &nums)
    {
        if (nums.size() == 1)
            return nums[0];
        // ----------------------- 超时1 -----------------------
        int size_in = nums.size();
        int max_sum = nums[0];
        vector<vector<int>> matrix_sum(nums.size(), vector<int>(nums.size(), 0));
        for (int i = 0; i < size_in; ++i)
        {
            matrix_sum[i][i] = nums[i];
            max_sum = nums[i] > max_sum ? nums[i] : max_sum;
        }
        // 从下往上
        for (int y = size_in - 2; y >= 0; --y)
            // 从左往右, x 最小值为 1, y 最小值为 0
            for (int x = y + 1; x < size_in; ++x)
            {
                matrix_sum[y][x] = matrix_sum[y][x - 1] + nums[x];
                if (matrix_sum[y][x] > max_sum)
                    max_sum = matrix_sum[y][x];
            }
        return max_sum;
        // ---------------------- 超时 ----------------------
        // int max_sum = nums[0];
        // for (int i = 0; i < nums.size(); ++i)
        // {
        //     int sum = nums[i];
        //     if (sum > max_sum)
        //         max_sum = sum;
        //     for (int j = i + 1; j < nums.size(); ++j)
        //     {
        //         sum += nums[j];
        //         if (sum > max_sum)
        //             max_sum = sum;
        //     }
        // }
        // return max_sum;
        // ---------------------- 超时 ----------------------
    }
    // https://leetcode.com/problems/longest-palindromic-substring/
    // 5. Longest Palindromic Substring
    /*
        given a string s, return the longest palindromic substring in s.
        ie: input s= 'babad'  output = 'bab' 'aba'也是可以的
        寻找最长的对称字符串(回文)
        提示: 能否使用之前计算的最大回文 再找出更大的;  在判断回文的时候能否使用之前计算的结果, 达到 O(1) 的判断?
        求解一个大问题(原始字符) 可以分解为求解子问题, 把子问题的最优解叠加起来, 可以得出大问题最优解. 问题之间存在重叠, 因此应该是 动态规划
        思路:
        用 left, right 作为构造子字符串的索引. 若 substr(left, right) 是回文, 那么 substr(left+1, right-1) 必定是回文, 且 s[left] == s[right].
        为了避免重复计算, 可以观察到若 'aba' 是一个回文, 那么在它的两侧添加相同的字符, 会构成一个更长的回文.
        因为 动态规划是 从上往下分析问题, 从下往上 计算子问题, 因此 i,j 的值是从小开始递增.
        Runtime: 1830 ms, faster than 5.00% of C++ online submissions for Longest Palindromic Substring.
        Memory Usage: 47.6 MB, less than 26.57% of C++ online submissions for Longest Palindromic Substring.
    */
    string longestPalindrome(string s)
    {
        int len_str = s.length();
        if (!len_str || len_str == 1)
            return s;
        const char *S = s.c_str();
        string longest;
        longest = S[0]; // 初始化一个字符
        int max_len = 1;
        vector<vector<bool>> b_palindrome_map(len_str, vector<bool>(len_str, false));
        // 初始化, 每个字符自身就是回文
        for (int i = 0; i < len_str; ++i)
        {
            b_palindrome_map[i][i] = true;
            if (i == len_str - 1)
                break;
            b_palindrome_map[i][i + 1] = S[i] == S[i + 1]; // 初始化与邻边字符 组成的 字符串 是否为回文
            if (b_palindrome_map[i][i + 1])
            {
                // 初始化 2 个字符构成的字符串
                if (2 > max_len)
                {
                    longest = s.substr(i, 2);
                    max_len = 2;
                }
            }
        }
        // x 坐标不断减小, y 的起始坐标也在不断减小, 也就是自下而上, 从左往右的 填充 矩阵
        // 符合动态规划的 从小的问题开始解决, 并逐渐解决大的问题.
        /*
           y^
            |**???
            |***??
            |*****
            0----->x
        */
        // y 从倒数第2个字符开始, 逐渐递减
        for (int y = len_str - 2; y >= 0; --y)
            // x 从左往右扫描
            for (int x = y + 2; x < len_str; ++x)
            {
                b_palindrome_map[y][x] = (b_palindrome_map[y + 1][x - 1] && S[y] == S[x]);
                if (b_palindrome_map[y][x])
                {
                    // find the longest string
                    if ((x - y + 1) > max_len)
                    {
                        longest = s.substr(y, x - y + 1);
                        max_len = longest.length();
                    }
                }
            }
        return longest;
    }
};