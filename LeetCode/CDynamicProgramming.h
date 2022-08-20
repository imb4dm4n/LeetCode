#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <map>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/decode-ways/
    // 91. Decode Ways
    /*
        把字母编码成数字: a-1,b-2,c-3,..z-26; 问 输入一个数字, 有多少种解码方法: 11223,-> (1,1,2,2,3), (1,1,2,23),(1,1,22,3),(11,22,3)....
        以0开头的不能被解码 06 是无法解码的; 
    */
    int numDecodings(string s) {
        const char * pstr = s.c_str();
        int len = s.size(), index = 0, count = 0;
        if(*pstr == '0')
            return 0;
        while(index < len) {
            // 开始构造解码可能
            
        }
    }    // https://leetcode.com/problems/climbing-stairs/
    // 70. Climbing Stairs
    /*
        青蛙跳台阶, 台阶 n 层, 一次可以选择跳1阶或2阶. 问有多少种跳法.
        Runtime: 0 ms, faster than 100.00% of C++ online submissions for Climbing Stairs.
        Memory Usage: 5.8 MB, less than 97.34% of C++ online submissions for Climbing Stairs.
    */
    // int climbStair(int n, map<int,int>& methods) {
    //     if(methods.find(n) != methods.end()) 
    //         return methods[n];
        
    //     int count1 = climbStairs(n - 1);        // 第一次跳 1 阶 + 剩下的 (n-1) 阶跳法
    //     methods[n - 1] = count1;
        
    //     int count2 = climbStairs(n - 2);        // 第一次跳 2 阶 + 剩下的 (n-2) 阶跳法
    //     methods[n - 2] = count2;
        
    //     return  count2 + count1;
    // }
    int climbStairs(int n) {
        int a = 1,    //  a 表示 1个台阶有多少跳法, 当 台阶数量超过 2 的时候, 例如 3, 则 a 表示 (3-1) 个台阶的跳法
            b = 2;    //  b 表示 2个台阶有多少跳法, 当 台阶数量超过 2 的时候, 例如 3, 则 b 表示 3 个台阶的跳法
        if(n < 3)
            return n;
        for(int i=3; i < n; ++i) {
            b = a + b;      //  第 i 个台阶的跳法 是 第 (i-1) 个台阶的跳法 + 第 (i-2) 个台阶的跳法
            a = b - a;      // 更新 i-1 个台阶的跳法
        }
        return b;
        // map<int,int> methods;
        // methods[1]=1;
        // methods[2]=2;
        // return climbStair(n, methods);
    }
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
        加入  :  则后序所有的数字都加入, 否则选择的数组就不是连续的了
        不加入:  则从后面的数字开始选择
    Runtime: 171 ms, faster than 40.40% of C++ online submissions for Maximum Subarray.
    Memory Usage: 83.5 MB, less than 5.90% of C++ online submissions for Maximum Subarray.
    // 类似求最长回文, 只不过这里是累加出最大的值而已.
    // 初始化矩阵, 把对角线的值填上去. 然后从下往上, 从左往右计算和,找出最大值. (超时)
    Input:
    [5,4,-1,7,8]
    Output:
    15
    Expected:
    23
    */
    /*
     @param  nums        输入数据
     @param  index       当前选择的数字
     @param  sums        保存每个数字是否被选中时, 得到的最大和
     @param  pick_cur    是否选择当前数字
     @returns  int       最大的和
    */
    const int boundary = -0xffffff;
    int dp_find_max_sub_array(const vector<int> &nums, int index, vector<vector<int>> &sums, bool pick_cur)
    {
        if (index >= nums.size())
            return pick_cur ? 0 : boundary; // 边界, 若选择边界, 则返回0, 因为边界是不存在的值,返回0 不改变和的结果; 不选择边界, 则边界被作为 单一值返回 来比较. ie 输入[-2, -1]
        // 读取重叠的子问题解
        if (sums[pick_cur][index] != boundary)
            return sums[pick_cur][index];
        // 需要当前节点, 则返回 当前节点 + 后序能找到的最大值, 并保存子问题的结果
        if (pick_cur)
            return sums[pick_cur][index] = max(0, nums[index] + dp_find_max_sub_array(nums, index + 1, sums, true));
        // 不一定需要当前节点, 返回 当前节点 + 后序节点能找到的最大值;  或 不需要当前节点
        return sums[pick_cur][index] = max(
                   nums[index] + dp_find_max_sub_array(nums, index + 1, sums, true),
                   dp_find_max_sub_array(nums, index + 1, sums, false));
    }
    int maxSubArray(vector<int> &nums)
    {
        if (nums.size() == 1)
            return nums[0];
        vector<vector<int>> sums(2, vector<int>(nums.size(), boundary));
        return dp_find_max_sub_array(nums, 0, sums, false);
        // ----------------------- 超时1 -----------------------
        // int size_in = nums.size();
        // int max_sum = nums[0];
        // vector<vector<int>> matrix_sum(nums.size(), vector<int>(nums.size(), 0));
        // for (int i = 0; i < size_in; ++i)
        // {
        //     matrix_sum[i][i] = nums[i];
        //     max_sum = nums[i] > max_sum ? nums[i] : max_sum;
        // }
        // // 从下往上
        // for (int y = size_in - 2; y >= 0; --y)
        //     // 从左往右, x 最小值为 1, y 最小值为 0
        //     for (int x = y + 1; x < size_in; ++x)
        //     {
        //         matrix_sum[y][x] = matrix_sum[y][x - 1] + nums[x];
        //         if (matrix_sum[y][x] > max_sum)
        //             max_sum = matrix_sum[y][x];
        //     }
        // return max_sum;
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
        思路2:
        简单的暴力查找. 从任意一个字符作为中点, 开始寻找回文. 记录最长的回文起始偏移.
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