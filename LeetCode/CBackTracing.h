#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <map>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
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