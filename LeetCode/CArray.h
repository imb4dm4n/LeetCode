#include <vector>
#include <map>
#include <unordered_set>
#include <math.h>
using namespace std;
namespace Array
{
    /**
     * @brief 974. Subarray Sums Divisible by K
     * 
     * @param nums 
     * @param k 
     * @return int 
     */
    int subarraysDivByK(vector<int>& nums, int k) {
        int res=0,pre_sum =0;
        map<int, int> counter;  // 余数为  -(k-1),.. 0, .. k-1
        counter[0]  =   1;
        for(auto n : nums) {
            pre_sum +=  n;
            int remainder = 0;
            if(pre_sum % k  == 0) {
                // 整除的情况
            }
            else if (pre_sum < 0) {
                remainder   =   (pre_sum%k +k) %k  ;
                printf("pre_sum = %d remainder= %d\n",pre_sum, remainder);
            } 
            
            if(counter.find(remainder) != counter.end())
                res     +=  counter[remainder];
            else
                counter[remainder]  =   0;
            counter[remainder] += 1;
        }

        return res;
    }

    /**
     * @brief 1352. Product of the Last K Numbers
     * https://leetcode.com/problems/product-of-the-last-k-numbers/submissions/
     * 最后 k 个数字的乘积
     * Beats 94.1%
     */
    class ProductOfNumbers {
    
    vector<int> m_products;
    public:
        ProductOfNumbers() {
            m_products = { 1 };	// 初始化 一个1 否则第一次计算时会出问题
        }
        
        void add(int num) {
            if(num == 0)
                m_products  =   {1};
            else {
                // a*b*c*d
                m_products.push_back(
                    m_products.back() * num
                );
            }
        }
        
        int getProduct(int k) {
            if(k >= m_products.size())
                return 0;
            else {
                return m_products.back() / m_products[m_products.size() -k -1];
            }
            
        }
    };
    // https://leetcode.com/problems/container-with-most-water/
    // 11. Container With Most Water
    /*
    给一个包含n个数字的数组 height，每个值都是一个高度， 通过 x轴坐标和 y轴坐标，形成一个容器，要求保存的水最多。
    限制条件: n>2 .
    solution1: 穷举法, O(N^2) 的时间复杂度. 记录每个点之间构成的容器大小, 找到最大值. 超时- -
    solution2: 本质上, 是要找到最小高度差 和 最大距离差的两个 索引. 这样才能构成最大的容器。 试一试从最大距离差开始找: 还是超时…… 同样的测试样例.
    solution3: 本质上, 是要找到最小高度差 和 最大距离差的两个 索引. 1. 距离差最大的是最左边和最右边, 因此初始化left=0, right = size-1; 这时候
    可以假设最大为 (right - left) * min(h1, h2). 如果在left或right往内部移动, 并且构成的面积要大于之前的, 那么条件便是选择 高度 越高的索引.
    可以得到 height[left] > height[right] ? right-- : left++
    Runtime: 186 ms, faster than 8.83% of C++ online submissions for Container With Most Water.
    Memory Usage: 58.9 MB, less than 82.14% of C++ online submissions for Container With Most Water.
    Runtime: 84 ms, faster than 92.92% of C++ online submissions for Container With Most Water.
    */
    int min(int a, int b)
    {
        return a < b ? a : b;
    }
    int max(int a, int b)
    {
        return a > b ? a : b;
    }

    int maxArea(vector<int> &height)
    {
        int max_area = 0;
        int left = 0, right = height.size() - 1;
        while (left < right)
        {
            int h = min(height[right], height[left]);
            // 计算当前容器大小
            // int size = (right - left) * h;
            max_area = max((right - left) * h, max_area);
            // 若左边的高度更高, 则从右边寻找高度更高的索引
            while (height[left] <= h && left < right)
                ++left;
            while (height[right] <= h && left < right)
                --right;
        }
        return max_area;
        // for (int i = 0; i < height.size(); ++i)
        // {
        //     for (int j = height.size() - 1; j > i; --j)
        //     {
        //         // calc the size of the container
        //         int size = (j - i) * min(height[i], height[j]);
        //         max_area = max(size, max_area);
        //     }
        // }

        // solution1
        // int max_area = 0;
        // for (int i = 0; i < height.size(); ++i)
        // {
        //     for (int j = i + 1; j < height.size(); ++j)
        //     {
        //         // calc the size of the container
        //         int size = (j - i) * min(height[i], height[j]);
        //         max_area = max(size, max_area);
        //     }
        // }
        // return max_area;
    }

    // https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    // 26. Remove Duplicates from Sorted Array
    /*
    给一个升序的带有重复节点的数组，移除重复数字，保持顺序不变，
    返回唯一的数字个数.
    solution:    1. 因为本身就是升序的，所以只要找到非重复节点，往非重复节点的索引写数据即可。
    Runtime: 8 ms, faster than 92.79% of C++ online submissions for Remove Duplicates from Sorted Array.
    Memory Usage: 18.3 MB, less than 92.93% of C++ online submissions for Remove Duplicates from Sorted Array.
    大神思路：
    int count = 0;
    for(int i = 1; i < n; i++){
        if(A[i] == A[i-1]) count++;
        else A[i-count] = A[i];
    }
    return n-count;
    */
    int removeDuplicates(vector<int> &nums)
    {
        if (nums.size() == 0)
            return 0;
        int prev = nums[0];
        int unique_index = 0;
        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i] == prev)
            {
                // duplication number found
                continue;
            }
            nums[++unique_index] = nums[i];
            prev = nums[i];
        }
        return unique_index + 1;
    }

    // https://leetcode.com/problems/contains-duplicate/
    // 217. Contains Duplicate
    /*Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. -10^9 <= nums[i] <= 10^9
    solution1: Runtime: 123 ms, faster than 50.78% of C++ online submissions for Contains Duplicate.
    Memory Usage: 52 MB, less than 39.48% of C++ online submissions for Contains Duplicate.
    solution2: use a unorder_set (which is implemented by hash map, has O(N) time complecity), copy original vector to it and compare their size.
    Runtime: 123 ms, faster than 50.78% of C++ online submissions for Contains Duplicate.
    Memory Usage: 55.2 MB, less than 6.41% of C++ online submissions for Contains Duplicate.
     */
    bool containsDuplicate(vector<int> &nums)
    {
        return nums.size() != unordered_set<int>(nums.begin(), nums.end()).size();
        // solution1:
        // std::map<int, int> map_num;
        // for(auto it : nums) {
        //     if(map_num.find(it) == map_num.end()) {
        //         map_num[it] = it;
        //     }
        //     else {
        //         return true;
        //     }
        // }
        // return false;
    }

    // https://leetcode.com/problems/search-in-rotated-sorted-array/
    // 33. Search in Rotated Sorted Array
    /*
    在一个可能被旋转的升序数组中，找到一个数字，要求 O(logN)复杂度。 返回目标的索引
    All values of nums are unique.
    solution:
    [4  5  6  1  2  3 ] -> rot = 3
    [4  5  6  1  2  3  4  5  6] realmid = ((low + high ) / 2 + rot) % n
    realmid 是扩展后的数组, 从 low 到 high 的中间索引. 而这个索引大于原始的数组大小, 因此需要 mod N
    */
    int search(vector<int> &nums, int target)
    {
        if (nums.size() == 0)
            return -1;
        int low = 0, hi = nums.size() - 1;
        // 寻找最小值的索引, 也是旋转发生的索引. 因为它是绕一个点旋转
        // 这个点一定是在最小值的索引处发生的
        while (low < hi)
        {
            int mid = (low + hi) / 2;
            if (nums[mid] > nums[hi])
                // 中间节点大于最后一个节点，说明 存在旋转,
                low = mid + 1;
            else
                // 不存在旋转， 把范围缩小
                hi = mid;
        }
        // low == hi 是最小值的索引，也是旋转发生的索引
        int rot = low;
        low = 0, hi = nums.size() - 1;
        while (low <= hi)
        {
            int mid = (low + hi) / 2;
            int realmid = (mid + rot) % nums.size();
            if (nums[realmid] == target)
                return realmid;
            if (nums[realmid] < target)
                low = mid + 1;
            else
                hi = mid - 1;
        }
        return -1;
    }

};