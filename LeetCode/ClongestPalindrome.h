#pragma once
#include <iostream>
#include <string>
using std::string;
class ClongestPalindrome
{
	// 偶数个字符串， 直接往中间添加一个字符，变成奇数的，最后再去掉？ 或者说模拟一个
	// 判断一个字符串是不是回文
	bool is_palindrome(string s, int middle, int left_begin) {

	}
	static string longestPalindrome(string s) {

		int middle = s.length() / 2;// 记录中间字符的偏移。 每往左|右边 移动一次， 最长的回文长度就会减一。
		int sub_len;// 记录每个对称点 对应的字符串的 长度的一半
		int left_begin = 0;

	}
};

