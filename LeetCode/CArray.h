#include<vector>
#include<map>
using namespace std;
namespace Array
{

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
        if(nums.size() == 0)
            return 0;
        int prev=nums[0];
        int unique_index=0;
        for(int i=1; i<nums.size();++i) {
            if(nums[i] == prev) {
                // duplication number found
                continue;
            }
            nums[++unique_index] = nums[i];
            prev = nums[i];
        }
        return unique_index+1;
    }

};