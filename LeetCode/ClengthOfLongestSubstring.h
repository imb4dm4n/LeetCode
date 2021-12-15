#pragma once
#ifndef SUBSTRING_H
#define SUBSTRING_H
// https://leetcode.com/problems/longest-substring-without-repeating-characters
#include<vector>
#include<map>
#include<iostream>
#include<string>
#include<stdlib.h>
#include<memory.h>
using namespace std;

class ClengthOfLongestSubstring
{
public:
/*思想： 在两个相同的字符之间，只能有一个唯一字符串。 因此他们之间的距离，便是这个
唯一字符串的长度。 最新的唯一字符串，起始地址为前一个出现重复的字符偏移+1 。
遍历时遇到重复的一个字符时，需要修正 《最新唯一字符串》 的起始偏移 begin_of_new_str ，
而且这个偏移必须是 之前的 begin_of_new_str 和 与当前字符相同的前一个字符偏移的 较大那个。
ie : 输入 aebacdbe
aeba -> a 重复[计算长度 aeb=3-begin_of_new_str=  3] -> ebacdb 修正 begin_of_new_str = 1
ebacdb -> b 重复[计算长度 ebacd=6-begin_of_new_str= 5] -> acdb 修正 begin_of_new_str = 2
acdb -> acdbe 结束[计算长度 7-2=5]
最终得到 5

只要遍历所有唯一字符串的长度，找到最长的即可。 
注意： 这两个相同的字符之间，内部不能还存在有两个相同的字符。*/
    static int lengthOfLongestSubstring(string s) {
        int word_map[255] = { 0 };
        memset(word_map, -1, sizeof(word_map));
        int max_len = 0;
        int index = 0, sub_len = 0;
        int begin_of_new_str = 0;// 最新子串的起始偏移
        while (index < s.length()) {
            if (word_map[s[index]] != -1) { // 字符偏移非0，曾经出现过
                begin_of_new_str = max(begin_of_new_str, word_map[s[index]] + 1);
                // 需要把 最新子串的起始偏移改为大的那个，原因就是 ebacdb 这种情况
            }
            word_map[s[index]] = index;
            sub_len = index - begin_of_new_str+1;
            max_len = max_len > sub_len ? max_len : sub_len;// 取子串中更长的那个
            index++;
        }

        return max_len;
    }
};


#endif // DEBUG