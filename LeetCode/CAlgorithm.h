#include <queue>
#include <deque>
#include <vector>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    // https://leetcode.com/problems/median-of-two-sorted-arrays/
    // 4. Median of Two Sorted Arrays
    /*Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    solution: 计算两个数组大小, 得出他们的个数和, 判断是奇数个还是偶数个.
    奇数个: 在合并他们的过程中, 遇到 mid 索引直接返回
    偶数个: 在合并他们的过程中, 遇到 mid 索引 计算 mid 和 mid+1 的平均值返回.
    */
    // 合并两个数组
    typedef vector<int> * vip;
    void mergeArray(vector<int>& nums1, vector<int>& nums2, int mid, int index, double& result, bool even) {
        int tmp = 0;
        vip p = nullptr;
        if(nums1.size() > 0 && nums2.size() > 0){
            if(nums1.front() > nums2.front()) {
                p = &nums2;
                // 取nums2
                // tmp = nums2.front();
                // nums2.erase(nums2.begin());
                // if(index == mid){
                //     result = tmp;
                //     return;
                // }
                // mergeArray(nums1, nums2, mid, index+1, result, even);
            }
            else {
                p = &nums1;
                // tmp = nums1.front();
                // nums1.erase(nums1.begin());
                // if(index == mid){
                //     result = tmp;
                //     return;
                // }
                // mergeArray(nums1, nums2, mid, index+1, result, even);
            }
        }
        else if (nums1.size() >0)
            p = &nums1;
        else 
            p = &nums2;
        
        tmp = p->front();
        p->erase(p->begin());
        if(index == mid){
            if(!even){
                result = tmp;
                return;
            }
            double next = 0;
            mergeArray(nums1, nums2, mid+1, index+1, next, even);
            result = (tmp + next) / 2;
            return ;
        }
        mergeArray(nums1, nums2, mid, index+1, result, even);
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size = nums1.size() + nums2.size();
        int mid = size / 2;
        int index_1 = 0, index_2 = 0, index = 0;
        bool even_case = false;
        double result = 0;

        if(size % 2 == 0)     {
            // even case
            even_case   =   true;
            mid         -=  1;
        }
        mergeArray(nums1, nums2, mid, 0, result, even_case);
        return result;

        // while ((index_1 < nums1.size() || index_2 < nums2.size() ) &&
        //     index != mid)
        // {
        //     if(nums1[index_1] < nums2[index_2]) {
        //         if(index_1 < nums1.size()) {
        //             ++index_1;
        //         }
        //         else {
        //             ++index_2;
        //         }
        //     }
        //     else {
        //         if(index_2 < nums2.size()) {
        //             ++index_2;
        //         }
        //         else {
        //             ++index_1;
        //         }
        //     }
        //     ++index;
        //     if(index == mid) {
                
        //     }
        // }
        // if(even_case) {
        //     // the even case
        //     int mid2 = index + 1;
        //     double sum = 0;
        //     if(index < nums1.size())
        //         sum += nums1[index];
        //     else
        //         sum += nums2[index];
        //     if(mid2 < nums1.size())
        //         sum += nums1[mid2];
        //     else
        //         sum += nums2[mid2];
        //     return sum /= 2;
        // }
        // if(index < nums1.size())
        //     return nums1[index];
        // return nums2[index];
        
    }
    // https://leetcode.com/problems/number-of-digit-one/
    // 233. Number of Digit One
    /*
        Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
    */
    int countDigitOne(int n) {
        
    }
    // https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    // 34. Find First and Last Position of Element in Sorted Array
	// TODO : MAKE it fast
    /*
        从一个升序排序的数组中, 找到给定值的 起始和结束偏移. 如:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        solution: binary search target, if found target, increasing and decreasing index
        to find identical value.
        特殊情况: 1.target 不再数组中. 2. 数组只有两个数字(a.target 是左边一个; b.target 是右边一个) 3.数组只有一个数字(相同和不同的情况)
        Runtime: 21 ms, faster than 10.97% of C++ online submissions for Find First and Last Position of Element in Sorted Array.
        Memory Usage: 13.7 MB, less than 17.99% of C++ online submissions for Find First and Last Position of Element in Sorted Array.
    */
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ret{-1,-1};
        int left=0, right = nums.size()-1;
        // boundary case 1: 
        if(nums.size() == 0 || 
            (nums.size() == 1 && nums[0] != target))
            return ret;
        // boundary case 2:
        else if (nums.size() == 1 && nums[0] == target)
            return {0,0};
        
        int mid = (right - left) / 2 + left;

        while (nums[mid] != target) {
            if(nums[mid] < target)
                left = mid;
            else
                right = mid;
            mid = (right - left) / 2 + left;
            // by the end, mid will eventually hit left or right boundary
            if (mid == left || mid == right)
                break;
        }
        // boundary case : {1, 3} & search for  1 
        if ((mid - 1 >= 0) && (nums[mid - 1] == target))
            mid = mid - 1;
        // boundary case : {1, 3} & search for 3
        else if ((mid + 1 <= nums.size()) && (nums[mid + 1] == target))
            mid = mid + 1;
        if(nums[mid] != target)
            return ret;
        
        left = right = mid;

        while((left - 1) >= 0 && nums[(left - 1)] == target)
            --left;

        while((right + 1) < nums.size() && nums[(right + 1)] == target)
            ++right;
        ret[0] = left;
        ret[1] = right;
        return ret;
    }
    // https://leetcode.com/problems/regular-expression-matching/
    // 10. Regular Expression Matching
    /*
    Given an input <string s> and a <pattern p>, implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).
    思路: 正则表达式是一个状态机, 当符合限制的输入才能达到终止状态. 状态机在某些特定条件下会
    进行状态转移, 失败状态可以退出.
    
    Runtime: 1397 ms, faster than 5.01% of C++ online submissions for Regular Expression Matching.
    Memory Usage: 6.4 MB, less than 74.02% of C++ online submissions for Regular Expression Matching.
    */
    bool match_core(const char *s, const char *p)
    {
        // 输入 和 匹配串 都结束
        if (*s == NULL && *p == NULL)
            return true;
        // 匹配串提前结束
        if (*s != NULL && *p == NULL)
            return false;
        // 下一个匹配字符是 *
        if (*(p + 1) == '*')
        {
            // 分为 .* 和 [a-z]* 两种情况
            if (*s == *p || (*p == '.' && *s != NULL))
            {
                return match_core(s + 1, p + 2) ||
                       match_core(s + 1, p) ||
                       match_core(s, p + 2);
            }
            // 当前输入字符 不匹配, 则移动匹配串: 因为 * 可以表示0个 前一个字符
            // ie:  p=ab*bd; s= acb; b* 可以匹配0个b, 因此移动匹配串
            else
            {
                return match_core(s, p+2);
            }
        }
        // 下一个匹配字符不是 *
        if (*s == *p ||
            (*s != NULL && *p == '.'))
            return match_core(s + 1, p + 1);
        return false;
    }
    bool isMatch(string s, string p)
    {
        return match_core(s.c_str(), p.c_str());
    }
    // https://leetcode.com/problems/powx-n/
    // 50. Pow(x, n)
    /*Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
    Input: x = 2.00000, n = 10
    Output: 1024.00000
    */
    /*
    快速计算 次方: a^n = a^ (n/2) *  a^ (n/2)
    Runtime: 4 ms, faster than 31.47% of C++ online submissions for Pow(x, n).
    Memory Usage: 5.9 MB, less than 42.94% of C++ online submissions for Pow(x, n).
    Runtime: 3 ms, faster than 46.40% of C++ online submissions for Pow(x, n).
    Memory Usage: 5.9 MB, less than 42.94% of C++ online submissions for Pow(x, n).
    */
    double quick_pow(double x, int exponent)
    {
        if (exponent == 0)
            return 1;
        if (exponent == 1)
            return x;
        double result = 1;
        unsigned int u_exp = exponent;
        if (exponent < 0 && u_exp != 2147483648) // exponent = -2147483648 时, (unsigned int)(-exponent) 会溢出导致异常
            u_exp = (unsigned int)(-exponent);
        else
            u_exp = (unsigned int)(exponent);
        result = quick_pow(x, u_exp >> 1);
        result *= result;
        // 奇数次方, 额外乘一次
        if (exponent & 1)
            result *= x;
        if (exponent < 0)
            result = 1 / result;
        return result;
    }
    double myPow(double x, int n)
    {
        double ans = 1;
        long exponent = n;
        long absExponent = exponent < 0 ? -exponent : exponent;
        while (absExponent)
        {
            if ((absExponent & 1) == 1)
                ans *= x;
            absExponent = absExponent >> 1;
            x *= x;
        }
        return n < 0 ? 1 / ans : ans;

        // solution 1
        // if (x == 0 || x == 1)
        //     return x;
        // if (n == 0) // 任何数的 0 次方都是1
        //     return 1;
        // return quick_pow(x, n);
    }

    // https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    // 153. Find Minimum in Rotated Sorted Array
    /*给定一个升序排序的数组 [0,1,2,4,5,6,7] , 它可能被旋转了:
    4次 [4,5,6,7,0,1,2] 也可能是 7次 [0,1,2,4,5,6,7] .
    所有元素不重复, 找出最小的元素. 要求时间复杂度 O(log n)
    solution: 注意到, 1.旋转后把数组分成两个 升序排序的子数组. [4,5,6,7] [0,1,2].
    2.并且左边的数组所有元素, 一定都大于右边的数组. 如果不符合这个条件, 则说明 没旋转.
    3.通过二分查找, 从左边的数组逼近最大值, 从右边的数组逼近最小值. 直到两个 索引
    相差为1
    Runtime: 3 ms, faster than 84.25% of C++ online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 10.1 MB, less than 72.48% of C++ online submissions for Find Minimum in Rotated Sorted Array.
    */
    int findMin(vector<int> &nums)
    {
        int left = 0, right = nums.size() - 1;
        int mid = 0;
        // 1.没有被旋转 或者 只有一个元素
        if (nums[left] < nums[right] || nums.size() == 1)
            return nums[0];
        // 不断逼近 left 和 right, 直到他们的索引相差为 1
        while (left != right - 1)
        {
            mid = (left + right + 1) / 2;
            if (nums[mid] > nums[left])
            {
                // 说明 mid 在左边的升序数组, 最小值在右边, 逼近左边最大值
                left = mid;
                continue;
            }
            else
            {
                // 说明 mid 在右边的升序数组, 最小值在左边, 逼近右边最小值
                right = mid;
            }
        }
        return nums[right];
    }
    int fib(int n);
    // https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
    // 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
    /*
        给一个目标数字k, 从斐波那契数列中找出任意个数字, 和为 k, 要求使用的数字个数最少. 可以使用重复的数字. 返回最小需要个数字个数
        solution1 (wrong): 先不停的生成斐波那契数列数列, 直到找到一个数字大于等于k. 若找到==k的, 则直接返回;
        若没找到, 则从第一个小于k 的数字 t 开始, 寻找最小和计算得到 k-t 的数字个数, 若找的到
        则返回, 找不到, 则继续往 t 的前一个数字找
        solution2 : 记作需要的数字个数为 f(k). 那么找到构成 k-1 的数字个数就为 f(k-1), 而构成 1 这个数字只需要 1 个数字 1.
        那么最少数字构成k 就是 f(k) = f(k-1) + 1
     */
    /*
    从 fibs 数列中找到和为 target 的
    */
    // int findMinFibonacciNumbers_(const vector<int> &fibs, int target)
    // {
    //     if (fibs.back() == target)
    //         return 1;
    //     // 从数列的最后一个开始往前, 寻找和为k
    //     for (int i = 0; i < fibs.size(); ++i)
    //     {
    //         int count = findMinFibonacciNumbers_(fibs, target - fibs[i]);
    //         if (count > 0)
    //             return count + 1;
    //     }
    //     return 0;
    // }
    int findMinFibonacciNumbers(int k)
    {
        if (k < 2)
            return k;
        int a = 1, b = 1;
        while (b <= k)
        {
            swap(a, b);
            b += a;
        }
        return 1 + findMinFibonacciNumbers(k - a);
        // solution1  错误
        // vector<int> fibs; // 保存 斐波那契数列
        // int i = 0;
        // while (true)
        // {
        //     int num = fib(i); // 不断生成数列, 直到找到一个大于等于k的
        //     fibs.push_back(num);
        //     if (num >= k)
        //         break;
        //     ++i;
        // }
        // // 最大的为k 则直接返回
        // if (fibs.back() == k)
        //     return 1;
        // // 从数列的最后一个开始往前, 寻找和为k
        // for (i = fibs.size() - 1; i >= 0; --i)
        // {
        //     int count = findMinFibonacciNumbers_(fibs, k - fibs[i]);
        //     if (count > 0)
        //         return count + 1;
        // }
        // return 0;
    }
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