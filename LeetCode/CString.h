#include <vector>
#include <map>
#include <unordered_set>
#include <math.h>
#include <string>
using namespace std;
namespace CString
{
    // https://leetcode.com/problems/replace-words/
    // 648. Replace Words
    /*
        有一个字典包含一系列单词的词根, 用 词根 替换输入的字符串中的每个单词, 要求使用最短的词根.
        输入:["cat","bat","rat"]
        "the cattle was rattled by the battery"
        输出:"the cat was rat by the bat"
        solution1 : build a word map for given dictionary. split sentence by space and iterate over every word.
        constructe a tmp string from 0 to word length, search the word map and if found a root, add it to return string,
        otherwise add the origin word to the return string.
        Runtime: 1239 ms, faster than 5.11% of C++ online submissions for Replace Words.
        Memory Usage: 357 MB, less than 5.23% of C++ online submissions for Replace Words.
    */
    string replaceWords(vector<string> &dictionary, string sentence)
    {
        // soulution1 :
        string ret = "", tmpstr = "";
        map<string, string> map_dic;
        for (auto it : dictionary)
            map_dic[it] = it;

        int left = 0, right = 0;
        while (right < sentence.size())
        {
            bool found_in_dic = false; // 初始化, 当前单词没有在 dic 出现过
            while (sentence.c_str()[right] != ' ' && !found_in_dic && right < sentence.size())
            {
                // 寻找 分隔符
                // construct a tmp string from left to right
                tmpstr = sentence.substr(left, right - left + 1);
                if (map_dic.find(tmpstr) == map_dic.end())
                {
                    ++right;
                    continue;
                }
                // 找到了词根
                if (ret.length() == 0)
                    ret = tmpstr;
                else
                    ret = ret + ' ' + tmpstr;
                found_in_dic = true;
            }
            // 没找到, 则使用原单词
            if (!found_in_dic)
            {
                tmpstr = sentence.substr(left, right - left);
                if (ret.length() == 0)
                    ret = tmpstr;
                else
                    ret = ret + ' ' + tmpstr;
                ++right;
                left = right;
                continue;
            }
            // 找到了, 移动索引到正确位置
            while (sentence.c_str()[right] != ' ' && right < sentence.size())
                ++right;
            // 需要移动到非 分隔符索引
            left = ++right;
        }
        return ret;
    }
}