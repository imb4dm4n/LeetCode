#include <iostream>
#include<string>
#include<vector>
using namespace std;
namespace letcoode{
	/**
	 * Definition for a binary tree node.
	 * struct TreeNode {
	 *     int val;
	 *     TreeNode *left;
	 *     TreeNode *right;
	 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
	 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
	 * };
	 */
	 struct TreeNode {
	 	int val;
	 	TreeNode *left;
	 	TreeNode *right;
	 	TreeNode(): val(0), left(nullptr), right(nullptr) {}
	 	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	 	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
	 };
	 
	void recursive_inorderTraversal(TreeNode* node, vector<int>& r) {
		//
		if (node) {
			recursive_inorderTraversal(node->left, r);
			r.push_back(node->val);
			recursive_inorderTraversal(node->right, r);
		}
	}
	// https://leetcode.com/problems/binary-tree-inorder-traversal/
	vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        recursive_inorderTraversal(root, ret);
        return ret;
    }
};
