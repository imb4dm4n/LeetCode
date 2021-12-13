#pragma once
//https://leetcode.com/problems/two-sum/
#include<vector>
#include<map>
#include<iostream>
using namespace std;
class CTwoSum
{
public:
        static vector<int> twoSum(vector<int>& nums, int target) {
            std::vector<int> subs,ret ;
            int max = nums[0];
            int i;
            for ( i= 0; i < nums.size(); ++i) {
                if (nums[i] > max)
                    max = nums[i];
                subs.push_back(target - nums[i]);
            }
            //int* numMap= new int[max];
            std::map<int, int> num_map;
            /*for (int i = 0; i < max; ++i) {

                numMap[i] = 0;
            }*/
            for (int i = 0; i < nums.size(); ++i) {

                num_map[nums[i]] += 1;
                //numMap[nums[i]] += 1;
            }
            int x=0;
            for (i = 0; i < subs.size(); ++i) {
                std::cout << "sub " << i << " = " << subs[i] << std::endl;
                //if (numMap[subs[i]] == 1 && nums[i] != subs[i]) { // 找到一个
                if (num_map[subs[i]] == 1 && nums[i] != subs[i]) { // 找到一个
                    ret.push_back(i);//第一个数的偏移
                    x =  subs[i];
                    //std::cout << "x = " << x << " i= "<<i << std::endl;
                    break;
                }
                else if (num_map[subs[i]] > 1 ) { // 找到一个
                    ret.push_back(i);//第一个数的偏移
                    x = subs[i];
                    //std::cout << "x = " << x << " i= "<<i << std::endl;
                    break;
                }
                //else if (numMap[subs[i]] == 2) {// 相同的两个数
                //    ret.push_back(i);
                //}
            }
            for (int j = 0; j < nums.size(); ++j) {
                if (nums[j] == x && j != i) {
                    //std::cout << "j = " << j << std::endl;
                    ret.push_back(j);
                    break;
                }
            }
        //std::map<int, int> map_num, map_sub;
        //std::vector<int> ret;
        //for (int i = 0; i < nums.size(); ++i) {
        //    map_sub[target - nums[i]] = i;// 每个差对应的原始减数
        //    map_num[nums[i]] = i; // 原始数值map
        //}
        //for (auto i: map_sub) {
        //    auto r = map_num.find(i.first);
        //    std::cout << "find i first " << i.first <<" second " << i.second << std::endl;
        //    if (r != map_num.end() && r->second != map_num[i.first]) {
        //        ret.push_back(i.second);
        //        ret.push_back(map_num[i.first]);
        //        break;
        //    }
        //}
        /*int j = 0;
        std::vector<int> subs,ret;
        for (auto i : nums) {
            map_num[i] = j++;
            if ((target - i) != i) {
                subs.push_back(target - i);
                map_sub[target - i] = i;
            }
        }
        for (auto i = map_sub.begin(), e = map_sub.end(); i != e; ++i) {
            if (map_num.find(i->first) != map_num.end()) {
                ret.push_back(map_num[i->second]);
                ret.push_back(map_num[i->first] );
                break;
            }
        }*/
        /*j = 0;
        for (auto i : subs) {
            if (map_num.find(i) != map_num.end()) {
                ret.push_back(j);
                ret.push_back(map_num[i]);
                std::cout << " j = " << j << " t= " << map_num[i] <<"i="<<i << std::endl;
                break;
            }
            ++j;
        }*/
        return ret;
    }
};

