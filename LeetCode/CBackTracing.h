#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <map>
using namespace std;
// using leetcode::ListNode;
namespace letcoode
{
    /*
        回溯法: 解决问题有多个步骤, 通过步骤达到某个状态是符合条件的解. 类似一颗N叉树, 到达叶节点时, 判断是否符合解的要求.
        若不符合, 回溯到前一个步骤, 继续寻找下一个可能的解.
        关键点: 寻找可能的解(通常是找一个解/所有的解/所有解的可能个数), 包含一个递归函数, 存在一个终止返回条件.
        参考: https://leetcode.com/discuss/interview-question/1141947/backtracking-study-and-analysis
    */
    // 22. Generate Parentheses
    // https://leetcode.com/problems/generate-parentheses/
    /*
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        思路1: 有多少个左括号 就一定有相同个数的有括号. 先插入所有左括号, 然后再找位置插入有右号.
        思路2: https://leetcode.com/problems/generate-parentheses/discuss/1131364/Clear-and-simple-explanation-with-intuition%3A-100-faster

    */
    void generateParenthesis_(int left, int right, string parenthesis, vecotr<string>& result)
    {
        
    }
    vector<string> generateParenthesis(int n)
    {
    }
};