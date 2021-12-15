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
/*˼�룺 ��������ͬ���ַ�֮�䣬ֻ����һ��Ψһ�ַ����� �������֮��ľ��룬�������
Ψһ�ַ����ĳ��ȡ� ���µ�Ψһ�ַ�������ʼ��ַΪǰһ�������ظ����ַ�ƫ��+1 ��
����ʱ�����ظ���һ���ַ�ʱ����Ҫ���� ������Ψһ�ַ����� ����ʼƫ�� begin_of_new_str ��
�������ƫ�Ʊ����� ֮ǰ�� begin_of_new_str �� �뵱ǰ�ַ���ͬ��ǰһ���ַ�ƫ�Ƶ� �ϴ��Ǹ���
ie : ���� aebacdbe
aeba -> a �ظ�[���㳤�� aeb=3-begin_of_new_str=  3] -> ebacdb ���� begin_of_new_str = 1
ebacdb -> b �ظ�[���㳤�� ebacd=6-begin_of_new_str= 5] -> acdb ���� begin_of_new_str = 2
acdb -> acdbe ����[���㳤�� 7-2=5]
���յõ� 5

ֻҪ��������Ψһ�ַ����ĳ��ȣ��ҵ���ļ��ɡ� 
ע�⣺ ��������ͬ���ַ�֮�䣬�ڲ����ܻ�������������ͬ���ַ���*/
    static int lengthOfLongestSubstring(string s) {
        int word_map[255] = { 0 };
        memset(word_map, -1, sizeof(word_map));
        int max_len = 0;
        int index = 0, sub_len = 0;
        int begin_of_new_str = 0;// �����Ӵ�����ʼƫ��
        while (index < s.length()) {
            if (word_map[s[index]] != -1) { // �ַ�ƫ�Ʒ�0���������ֹ�
                begin_of_new_str = max(begin_of_new_str, word_map[s[index]] + 1);
                // ��Ҫ�� �����Ӵ�����ʼƫ�Ƹ�Ϊ����Ǹ���ԭ����� ebacdb �������
            }
            word_map[s[index]] = index;
            sub_len = index - begin_of_new_str+1;
            max_len = max_len > sub_len ? max_len : sub_len;// ȡ�Ӵ��и������Ǹ�
            index++;
        }

        return max_len;
    }
};


#endif // DEBUG