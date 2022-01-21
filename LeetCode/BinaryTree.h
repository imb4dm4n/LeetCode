#include <iostream>
#include<string>
#include<vector>
#include<list>
#include<queue>
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
	//  template<class T>
	//  class ABSTreeNode;
	 
	 template<class T>
	 class ABSTreeNode {
	 	T val;	// abstracted tree node's value
	 	ABSTreeNode *left;
	 	ABSTreeNode *right;
	 	ABSTreeNode(): val(0), left(nullptr), right(nullptr) {}
	 	ABSTreeNode(T x) : val(x), left(nullptr), right(nullptr) {}
	 	ABSTreeNode(T x, ABSTreeNode *left, ABSTreeNode *right) : val(x), left(left), right(right) {}
	 };

	TreeNode* createTree(list<int*>& inputs) {
		if(inputs.empty()) {
			return nullptr;
		}
		int* data = inputs.front();
		inputs.pop_front();
		TreeNode* ret = new TreeNode(*data);
		ret->left = createTree(inputs);
		ret->right = createTree(inputs);
		return ret;
	}
	 
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
	
	// https://leetcode.com/problems/same-tree/
	// return true if the given binary tree has same value and same structure
	// recursively traverse two trees, compare their nodes
	void cmpTreeNode(TreeNode* p, TreeNode* q,bool& same)
	{
		if(same == false || (p == nullptr && q == nullptr)) {
			// same was false or we hit the bottom of the tree, return 
			return;
		}
		if ( (p == nullptr && q != nullptr) ||
			 (p != nullptr && q == nullptr)) {
				same = false;
				return;
		}
		if( p->val != q->val) {
			same = false;
			return;
		}
		cmpTreeNode(p->left, q->left, same);
		// cmpTreeNode(p->right, q->left, same); // for symmetric-tree/
		if(same == false)
			return;
		cmpTreeNode(p->right, q->right, same);
		// cmpTreeNode(p->left, q->right, same); // for symmetric-tree/
		
	}
	bool isSameTree(TreeNode* p, TreeNode* q) {
        bool ret = true;
		cmpTreeNode(p, q, ret);
		return ret;
    }

	// https://leetcode.com/problems/symmetric-tree/
	// solution: check the root's sub-tree, using isSameTree but exchange the node's 
	bool isSymmetric(TreeNode* root) {
		if (root == nullptr)
			return true;
        if (root->left == nullptr && root->right == nullptr)
			return true;
		if ( (root->left == nullptr && root->right != nullptr) || 
			  (root->left != nullptr && root->right == nullptr))
			return false;
		return isSameTree(root->left, root->right);
    }
	void test_bt() {
		list<int*> datas;
		datas.push_back(new int(1));
		datas.push_back(new int(2));
		datas.push_back(new int(3));
		datas.push_back(new int(1));
		datas.push_back(new int(1));
		
	}

	void DFS(TreeNode* root, int& depth, int& max_dep) {
		// deep first search a given tree, return it's maximum depth
		if(root == nullptr)
			return;
		depth++;
		if (depth >= max_dep)
			max_dep = depth;
		DFS(root->left, depth, max_dep);
		depth--;
		DFS(root->right, depth, max_dep);
		depth--;
	}
	// https://leetcode.com/problems/maximum-depth-of-binary-tree/
	int maxDepth(TreeNode* root) {
        int dep = 0, max_dep = 0;
		DFS(root, dep, max_dep);
		return max_dep;
    }
	// https://leetcode.com/problems/binary-tree-level-order-traversal/
	// traverse binary tree by level order from left to right
	// 
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> ret;
		if (root == nullptr)
			return ret;
		// 1. push the root's value 
		vector<int> tmp;
		tmp.push_back(root->val);
		ret.push_back(tmp);
		// 2. use a queue to store all nodes in the same level
		queue<TreeNode*> tasks;
		// 3. push the first round
		tasks.push(root->left);
		tasks.push(root->right);
		// 4. used to store how many nodes in the same level
		int nodes_cout = 2;
		while (!tasks.empty()) {
			// 5. to store all values in the same level
			vector<int> tmp_level;
			// 6. loop until nodes in the same level was popped 
			while (nodes_cout > 0) {
				--nodes_cout;
				TreeNode* tmp_node = tasks.front();
				tasks.pop();

				if (tmp_node) {
					tmp_level.push_back(tmp_node->val);
					tasks.push(tmp_node->left);
					tasks.push(tmp_node->right);
				}
			}
			// in case we push an empty [] to the vector
			if(tmp_level.size() > 0)
				ret.push_back(tmp_level);
			nodes_cout = tasks.size();
		}
		return ret;

	}
	// https://leetcode.com/problems/unique-binary-search-trees-ii/
	// Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
	// every new tree can be created by it's predecessor or so called ancient.
	// so we need to deliever a list of unique BST ancients to create a list of new unique BST.
	// find all posible positions to insert new value, and append it to the vector
	// to detective every node's left and right, find a place to insert the new value.
	// traverse every node in a tree, detective whether we can insert a new value to it's left or right.

	/*
	* 根据输入的 TreeNodes 修复每个节点的关系，构造二叉树
	*/
	TreeNode* createBst(list<TreeNode*> inputs) {
		if(inputs.size() == 0)
			return nullptr;
			
		TreeNode* ret = inputs.front();
		inputs.pop_front();
		if(ret) {
			ret->left = createBst(inputs);
			ret->right= createBst(inputs);
		}
		return ret;
	}

	// 克隆一个二叉树
	TreeNode* cloneBST(TreeNode* root) {
		if (root == nullptr)
			return nullptr;
		TreeNode* node = new TreeNode(root->val);
		node->left = cloneBST(root->left);
		node->right = cloneBST(root->right);
		return node;
	}

	void DFS_insert(TreeNode* node, vector<TreeNode*>& ret, int val) {
		if(node) {
			if(node->left == nullptr) {
				TreeNode* tmp = new TreeNode(val);
				node->left = tmp;
				ret.push_back(tmp);
			}
		}
	}

	vector<TreeNode*> breedBST(vector<TreeNode*>& ancients, int level, int target) {
		vector<TreeNode*> tmp;
		int old_len = ancients.size();
		for(int i=0; i < old_len; ++i) {
			// DFS search tree, find possible 
			TreeNode* root = ancients[i];
			
		}
	}
	vector<TreeNode*> generateTrees(int n) {
		vector<TreeNode*>  ret;
		return ret;
    }
};
