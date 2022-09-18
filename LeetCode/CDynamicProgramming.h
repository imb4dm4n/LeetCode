#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <map>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/unique-paths/
    // 62. Unique Paths
    /*
        在一个 m 行 n 列的矩阵中, 左上角放置一个机器人, 每次只能移动一格, 方向只能是向右或向下,
        问移动到右下角有多少种唯一的路径解法.
        思路1: 相当于 pos_x, pos_y 每次只能有一个去+1, 直到 pos_x 和 pos_y 的值分别为n和m.
        暴力穷举法, 当前坐标可以向右 或 向下移动时, 产生两个递归路径, 递归直到 pos_x和pos_y
        分别为n和m, count解法+1
        思路2: 前一种解法, 存在大量的重复计算, 比如经过坐标(3,3)到达target的方法个数是固定的，但是从初始坐标
        移动到(3,3)的方法有多个, 每一个方法都会再次计算 (3,3) 到 target 的解法个数, 是多余的计算.
        
    */
    enum direction {
        right,
        down,
    };
    /*
        pos_x 对于n的坐标
        pos_y 对于m的坐标
        dir   移动方向
        count 解法个数
    */
    bool enter_next(int pos_x, int pos_y, int n, int m, direction dir, int& count)
    {
        if(pos_x == (n-1) && 
            pos_y == (m-1)) {
                count += 1;
                return true;
        }
        if(dir == right && pos_x < (n-1)) {
            // 向右移动
            enter_next(pos_x + 1, pos_y, n, m, right, count) ||
            enter_next(pos_x + 1, pos_y, n, m, down, count);
        }
        else if(dir == down && pos_y < (m-1)) {
            // 若下一个函数调用已经移动到终点了, 那么如下两个函数调用, 将会重复计算一次结果, 因此结果需要除以2
            // 或者通过 || 的方式, 遇到终止时直接返回了
            // 向下移动
            enter_next(pos_x, pos_y + 1, n, m, right, count)  ||
            enter_next(pos_x, pos_y + 1, n, m, down, count);
        }
        return false;
    }
    /*
        leetCode 思路1: 每移动一步, 都会构成新的唯一路径. 当移动的坐标超过m或n时, 返回0表示无法到达目标,
        当坐标是 (m-1, n-1)时, 返回1.
    */
    int uniquePaths_(int m, int n, int i=0, int j=0) {
        if(i == m || n == j)    return 0;
        if(i == m-1 && j == n - 1)  return 1;
        return uniquePaths_(m, n, i+1, j) +      //  因为到达下一层遍历的时候, (i+1, j) 坐标会扩展为 (i+2,j) 和 (i+1, j+1) 的两个遍历
        uniquePaths_(m, n, i, j+1);
    }
    /*
        leetCode 思路2: 基于思路1, 可以发现, 会重复的计算相同坐标到目标节点(m-1, n-1)的走法个数, 因此用一个 二维数组, 保存每个坐标到目标节点的走法个数.
        减少冗余计算.
        Runtime: 2 ms, faster than 50.06% of C++ online submissions for Unique Paths.
        Memory Usage: 6.6 MB, less than 27.04% of C++ online submissions for Unique Paths.
    */
    int dfs(vector<vector<int>>& dp, int i, int j) {
        if (i == size(dp) || j == size(dp[0]))    return 0;

        if (i == size(dp) - 1 && j == size(dp[0]) - 1)  return 1;

        if (dp[i][j])    return dp[i][j];        //  若结果已经存在,则直接返回

        return dp[i][j] =                       // 保存计算过的节点
            dfs(dp, i + 1, j) +      //  因为到达下一层遍历的时候, (i+1, j) 坐标会扩展为 (i+2,j) 和 (i+1, j+1) 的两个遍历
            dfs(dp, i, j + 1);
    }
    int uniquePaths(int m, int n, int i=0, int j=0) {
        vector<vector<int>> dp(m, vector<int>(n));
        return dfs(dp, 0, 0);
    }
    /*
        思路3: 保存(0,0) -> (i, j) 的走法个数
    */
    int uniquePaths2(int m, int n) {
        // 因为在第一行, 所有的走法都是1, 因此初始化 vector<int>(n, 1)
        // vector<vector<int>> dp(m, vector<int>(n, 1));
        // for(int i=1; i<m; ++i)
        // // 需要一行一行的计算, 因为下一行会依赖上一行的计算结果
        //     for(int j=1; j<n; ++j) {
        //         dp[i][j]    =   dp[i-1][j] + dp[i][j-1];
        //     }
        // return dp[m-1][n-1];
        // -------- 进一步优化
        // -------- 因为计算某一行实际上仅仅依赖前一行, 可以复用一维数组
        vector<int> dp(n, 1);
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                dp[j] += dp[j-1];   
        return dp[n-1];
    }
    int uniquePaths1(int m, int n) {
        int count = 0;
        enter_next(0, 0, n, m, right, count) ||
        enter_next(0, 0, n, m, down, count);
        return count;
    }
    // https://leetcode.com/problems/decode-ways/
    // 91. Decode Ways
    /*
        把字母编码成数字: a-1,b-2,c-3,..z-26; 问 输入一个数字, 有多少种解码方法: 11223,-> (1,1,2,2,3), (1,1,2,23),(1,1,22,3),(11,22,3)....
        以0开头的不能被解码 06 是无法解码的; 
        "226"-> 2,26;  2,2,6;  22,6
        思路1: 从前往后, 递归的计算. 11223 -> 1,1223; 和 11,223 然后分别对他们继续做运算 1,223; 12,23; 
        继续 (1,223)的 223->(2,23; 2,2,3; 22,3) 发现和问题 (11,223)的 223 重叠.
        定义 f(i) 为解码从 0-i 个字符的可能, f(0) = 1; f(1) = f(0) + g(0,1)
        先判断当前字符是否符合解码标准, 符合则返回 1 + 值
        思路2: 从后往前计算. right = size - 1;  
        223:    ->  1 * ( 1*(1) + 1*1) + 1*1 = 3 
        思路3: 从后往前解码.
        10321 : 1,3, 2,1;   1,3,21,  2 种
        a = f(i - 1)    a 表示 从i - 1 到结束字符，有几种解法
        b = f(i)        b 表示 从 i 到结束字符，有几种解法

        i = 4
        b=f(4) = 1
        a=f(3) = f(i) * f(i-1) = 1 * 2 = 2

        i = 3
        b = f(3) = 2
        a = f(2) = f(3) * f(2) = 2 * 1 = 2

        i = 2 
        b = f(2) = 2 
        a = f(1) = f(2) * f(1) = 2	// 无效输入沿用解法个数

        i = 1
        b = f(1) = 2
        a = f(0) = 1 * f(1) = 2
        思路3: f(i) = f(i+1) + f(i+2) * g(i, i+1)
        Runtime: 0 ms, faster than 100.00% of C++ online submissions for Decode Ways.
        Memory Usage: 6.2 MB, less than 75.34% of C++ online submissions for Decode Ways.
    */
    // int try_decode(const char* pstr, int index, int size,int& count)
    // {
    //     // 
    //     if(index >= size)
    //         return 1;
    //     if (*pstr == '0' )
    //         return 0 ;
    //     else if (*(pstr + index) == '0')
    //         return try_decode(pstr, index+1, size, count);
    //     int res= try_decode(pstr, index+1, size, count) ;
    //     if(index < size - 1)
    //         return res +    
    //             (
    //             ((*(pstr+index) < '3')
    //             && (*(pstr + index + 1) < '7')
    //             ) ? (try_decode(pstr, index+2, size, count)) :0);
    //     return res;
    // }
    int numDecodings(string s) {
        // 数组保存 从结尾 到 对应字符 f(i) 的解码个数
        int n = s.size();
        int cur =0,p = 1, pp = 1;   // cur 表示第i到结尾的解码个数, 
            // p 表示 第 i+1到结尾的解码个数, pp 表示第 i+2到结尾的解码个数
        for(int i=n-1; i >= 0; --i) {
            int cur = s[i]=='0' ? 0 : p;
            if(i<n-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) cur+=pp;
            pp = p;
            p = cur;
        }
        return cur;
        // vector<int> ways(n + 1);
        // ways[n]   =   1;
        // for(int i=n-1; i >= 0; --i) {
        //     if(s[i] == '0'){
        //         ways[i] =   0;
        //         continue;
        //     }
        //     ways[i] = ways[i+1];    // f(i) = f(i+1) + f(i+2) * g(i, i+1) 这一步是 f(i) = f(i+1)
        //     if((i < n - 1) && (s[i] == '1' || s[i] == '2' && s[i+1] < '7')) {
        //         // 这一步是 f(i) = f(i+2) * g(i, i+1)
        //         ways[i] += ways[i+2];
        //     }
        // }
        // return n == 0 ? 0 :ways[0];
        // const char * pstr = s.c_str();
        // int len = s.size(), index = 0, count = 0;
        // return try_decode(pstr, 0, len, count);
        // int a = 0, b = 0;
        // index = len - 2;
        // if(*(pstr + len -1) != '0') // 最后一个字符不为 0 
        //     b = 1;
        // while(index >= 0 ) {
        //     char c = *(pstr + index);
        //     if(c !='0' && c < '3')
        //         a = 2 * b;
        //     else if (b == 0 && c !='0')
        //         a = 1;
        //     else // c == 0 或 c > '3' 都是沿用前一个的解法个数 
        //         a = b; 
        //     b = a;
        //     -- index;
        // }
        // return a;
        // return try_decode(pstr, 0, len, count);
        // return count;
        // while(index < len) {
        //     // 开始构造解码可能
            
        // }
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