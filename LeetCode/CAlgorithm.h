#include <queue>
#include <deque>
#include <vector>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
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