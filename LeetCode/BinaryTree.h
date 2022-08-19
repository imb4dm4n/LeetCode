#include <iostream>
#include<string>
#include<vector>
#include<list>
#include<queue>
#include<deque>
using namespace std;
#include "CAddTwoNumbers.h"
using leetcode::ListNode;
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
	 // binary search tree to double link list  二叉搜索树转双向链表
	 void ConvertNode(TreeNode* node, TreeNode*& prev_node)
	 {
		if(!node)
			return;
		TreeNode* pCurrent = node;
		
		// 中序遍历
		if(pCurrent->left != nullptr)
			ConvertNode(pCurrent->left, prev_node);
		
		// 左节点是前一个节点
		pCurrent->left	=	prev_node;
		
		// 前一个节点的右节点是当前节点
		if(prev_node)
			prev_node->right = pCurrent;
		prev_node	=	pCurrent;
		
		if(pCurrent->right != nullptr)
			ConvertNode(pCurrent->right, prev_node);
	 }
	
	 TreeNode* ConvertBstToDoubleLinkList(TreeNode* root)
	 {
		TreeNode* prev = nullptr;
		ConvertNode(root, prev);
		// 返回双向链表头节点
		TreeNode* pHead = prev;
		while(pHead && pHead->left)
			pHead = pHead->left;
		return pHead;
	 }
	// vector 转 二叉树
	TreeNode* create_bt(vector<int> array, int index)
	{
		TreeNode* root = nullptr;

		if (index < array.size() && array[index] != NULL)
		{
			root = new TreeNode(array[index]);
			root->left = create_bt(array, 2*index + 1);
			root->right = create_bt(array, 2*index + 2);
		}
		return root;
	}
	
	/*
		create a binary tree from a set of node's value. such as {1,2,4, null, 7}
		return the root of the tree
		:attension : if a node's value is zero, how do you differ from null pointer?
	*/
	TreeNode* create_from_vector(vector<int*> values) {
		if(values.size() == 0)
			return nullptr;
		
		queue<TreeNode*> q;
		int val = reinterpret_cast<int> (values[0]);
		// in case the root is a null pointer
		if(val == 0)
			return nullptr;
		
		TreeNode* root = new TreeNode(val);
		q.push(root);
		int index = 1;
		while(!q.empty() && index < values.size()) {
			TreeNode* front = q.front();
			q.pop();
			// get the root's left and right node
			int val_left = reinterpret_cast<int>(values[index]);
			if(val_left == 0)
				front->left = nullptr;
			else{
				front->left = new TreeNode(val_left);
				q.push(front->left);
			}
			++index;
			if(index < values.size()) {
				int val_right = reinterpret_cast<int>(values[index]);
				if(val_right == 0)
					front->right = nullptr;
				else{
					front->right = new TreeNode(val_right);
					q.push(front->right);
				}
				++index;
			}
		}

		return root;
	}
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
	// https://leetcode.com/problems/kth-smallest-element-in-a-bst/
	// 230. Kth Smallest Element in a BST
	/*Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
	输入一个二叉搜索树, 返回第 k 小的节点值. 
	思路: 中序遍历(left, root, right), 递归到 bottom 时, 开始计数 count = 1, 直到 count = k 就可以返回.
	边界测试: k 不能超过节点个数
	Runtime: 37 ms, faster than 24.36% of C++ online submissions for Kth Smallest Element in a BST.
	Memory Usage: 24 MB, less than 87.01% of C++ online submissions for Kth Smallest Element in a BST.
	*/
	void search_k(TreeNode* node, int k, int& count, int& kth)
	{
		if(!node)
			return;
		search_k(node->left, k, count, kth);
		++count;
		if(count == k) {
			kth = node->val;
			return;
		}
		search_k(node->right, k, count, kth);
	}
	int kthSmallest(TreeNode* root, int k) {
        int count=0, kth=0;
		search_k(root, k, count, kth);
		return kth;
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

	// 不通过递归中序遍历二叉树
	vector<int> inorderTraversalByQueue(TreeNode* root){
		vector<TreeNode*> stack;
		vector<int> values;
		while(root || !stack.empty()) {
			// 先插入所有左节点
			while(root) {
				stack.push_back(root);
				root = root->left;
			}
			// 取出栈顶节点
			TreeNode* node = stack.back();
			stack.pop_back();
			values.push_back(node->val);
			// 遍历栈顶节点的右子树
			root = node->right;
		}
		return values;
	}
	
	// https://leetcode.com/problems/same-tree/
	// return true if the given binary tree has same value and same structure
	// recursively traverse two trees, compare their nodes
	/*
	Runtime: 0 ms, faster than 100.00% of C++ online submissions for Same Tree.
	Memory Usage: 10.1 MB, less than 44.28% of C++ online submissions for Same Tree.
	*/
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
	/*
		solution1 : Runtime: 3 ms, faster than 94.06% of C++ online submissions for Symmetric Tree.
		Memory Usage: 16.4 MB, less than 47.93% of C++ online submissions for Symmetric Tree.
		solution2 : 通过前序遍历 和 对称的前序遍历(先右节点再左节点), 去判断对称.
		Runtime: 8 ms, faster than 58.56% of C++ online submissions for Symmetric Tree.
		Memory Usage: 16.4 MB, less than 47.93% of C++ online submissions for Symmetric Tree.
	*/
	bool isSymmetrical(TreeNode* rootA, TreeNode* rootB)
	{
		if(rootA == nullptr && rootB == nullptr)
			return true;
		if(rootA == nullptr || rootB == nullptr)
			return false;
		if(rootA->val != rootB->val)
			return false;
		// ------ 可以发现, 对 rootA 使用的是普通前序遍历(left, right), 对 rootB 使用的是对称前序遍历(right, left)
		return isSymmetrical(rootA->left, rootB->right) && 
			   isSymmetrical(rootA->right, rootB->left);
	}
	bool isSymmetric(TreeNode* root) {
		return isSymmetrical(root, root);
		// if (root == nullptr)
		// 	return true;
        // if (root->left == nullptr && root->right == nullptr)
		// 	return true;
		// if ( (root->left == nullptr && root->right != nullptr) || 
		// 	  (root->left != nullptr && root->right == nullptr))
		// 	return false;
		// return isSameTree(root->left, root->right);
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
	/*Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Level Order Traversal.
	Memory Usage: 12.6 MB, less than 31.07% of C++ online submissions for Binary Tree Level Order Traversal.*/
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
	// https://leetcode.com/problems/unique-binary-search-trees
	// 
	int dynamic_program[21]; 
    int numTrees(int n) {
        if(n<=1)
            return 1;
        if(dynamic_program[n]!=0)
			return dynamic_program[n]; 
        for(int i=1;i<=n;++i) {
			dynamic_program[n] += numTrees(i-1)*numTrees(n-i); 
        }
		return dynamic_program[n];
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
		return tmp;
	}
	vector<TreeNode*> generateTrees(int n) {
		vector<TreeNode*>  ret;
		
		return ret;
    }

	/*
	begin 构建子二叉树起始索引
	end 构建子二叉树结束索引
	*/
	TreeNode* generate_sub_trees(vector<int>& nums, int begin, int end) {
		
		if(begin > end)
			return nullptr;
		// 取出中间索引作为 root 节点值
		int root_id = (begin + end) / 2;
		TreeNode * n = new TreeNode(nums[root_id]);
		n->left = generate_sub_trees(nums, begin, root_id - 1);
		n->right = generate_sub_trees(nums, root_id + 1, end);
		return n;
	}
	// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
	// Runtime: 8 ms, faster than 97.14% of C++ online submissions 一次就完成哈哈
	// 从有序的数组构建一颗平衡的二叉查找树。
	// 思路： 分治思想， 把数组中心作为 root 节点， 划分为左数组（子树） 和 右数组（子树）， 对他们分别继续分治构造二叉树。
	/* 假设输入 6 个数字 [0,5]:
	0+5 / 2 = 2 => [0, 2-1]  [2+1,5] => [0,1] [3,5]
	[0,1] 2 [,3,4,5]

	[0,1]:
	0+1 / 2 = 0 => [0, 0-1] [0+1,1]

	root_id = (begin + end)/2;
	[begin, root_id-1]  , [root_id+1, end]
	*/
	TreeNode* sortedArrayToBST(vector<int>& nums) {
		// 分治思想， 直到数组个数为1.
		TreeNode* ret = generate_sub_trees(nums, 0, nums.size()-1);
		return ret;
    }

	// https://leetcode.com/problems/balanced-binary-tree/
	// give a binary tree, determine if it is heigh balanced.
	// a high balanced tree is in which the left and right subtree of every node differ in heigh by no more than 1
	 
	int max(int a, int b) {
		if(a>b)
			return a;
		return b;
	}
	int dfs_heigh(TreeNode* root) {
		if (root == nullptr)
			return 0;
		int left = dfs_heigh(root->left);
		int right = dfs_heigh(root->right);
		return max(left, right) + 1;
	}
	int abs(int num) {
		if (num<0)
			num = 0 - num;
		return num;
	}
	bool isBalanced(TreeNode* root) {
        // 每个节点自身高度为1， 加上左子树 、右子树最高的那个，  就是节点的高度了
		// 在递归返回的时候，对比两个节点的高度差
		// 计算每个节点的左子树高度和右子树的高度差， 若大于1则直接判定为非平衡的
		if (root == nullptr)
			return true;
		int left = dfs_heigh(root->left);
		int right = dfs_heigh(root->right);
		return (abs(left - right) < 2) && isBalanced(root->left) && isBalanced(root->right); 
    }

	/* https://leetcode.com/problems/minimum-depth-of-binary-tree/
	Given a binary tree, find its minimum depth.
	The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
	Note: A leaf is a node with no children.*/
	// 从叶节点网上回溯到根节点， 计算所有根节点到所有叶子节点的高度，取最小值。
	void DFS_small(TreeNode* node, int& smallest, int& cur_dep) {
		if(node == nullptr)
			return;
		cur_dep += 1;
		if(node->left == nullptr && node->right == nullptr) {
			// this is the leaf node
			if(smallest != 0 && cur_dep < smallest)
				smallest = cur_dep;
			else if (smallest == 0)
				smallest = cur_dep;
			cur_dep -= 1;
			return;
		}
		DFS_small(node->left, smallest, cur_dep);
		DFS_small(node->right, smallest, cur_dep);
		cur_dep -= 1;
	}
	int minDepth(TreeNode* root) {
        if(root == nullptr)
			return 0;
		int dep = 0;
		int smallest = 0;
		DFS_small(root, smallest, dep);
		return smallest;
    }
	// https://leetcode.com/problems/path-sum/
	// given a binary tree and a target sum, return true if find a path to leaf which add all nodes along the path to target sum.
	/*Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.*/
	// use a queue to store path to leaf,each time we enter a node, add it's value, when we hit leaf, compare the sum,
	// if sum != targetSum, we pop the node
	void has_path(TreeNode* root, int& sum, int target, bool& t) {
		if(root == nullptr)
			return;
		sum += root->val;
		if(root->left == nullptr && root->right == nullptr && sum == target)
		{
			t=true;
		}
		has_path(root->left, sum, target, t);
		has_path(root->right, sum, target, t);
		sum -= root->val;
	}
	bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr)
			return false;
		bool t = false;
		int sum = 0;
		has_path(root, sum, targetSum, t);
		return t;
    }
	// https://leetcode.com/problems/binary-tree-preorder-traversal/
	#include<deque>
	using std::deque;
	void dfs_preorder(vector<int>& data, TreeNode* root) {
		if(root == nullptr)
			return;
		data.push_back(root->val);
		dfs_preorder(data, root->left);
		dfs_preorder(data, root->right);
	}
	vector<int> preorderTraversal(TreeNode* root) {
        // 前序遍历
		// recursion: 0 ms
		// vector<int> r;
		// dfs_preorder(r, root);
		// return r;

		// stack apporch 8 ms
		deque<TreeNode*> q;
		vector<int> r;
		q.push_back(root);
		while(!q.empty()) {
			TreeNode* top = q.back();
			q.pop_back();
			if(top) {
				q.push_back(top->right);
				q.push_back(top->left);
				r.push_back(top->val);
			}
		}
		return r;
    }
	// https://leetcode.com/problems/binary-tree-postorder-traversal/
	void dfs_postorder(vector<int>& data, TreeNode* root) {
		if(root == nullptr)
			return;
		dfs_postorder(data, root->left);
		dfs_postorder(data, root->right);
		data.push_back(root->val);
	}
	vector<int> postorderTraversal(TreeNode* root) {
        //vector<int> r;
		// dfs_postorder(r, root);

		deque<TreeNode*> q;
		vector<int> r;
		q.push_back(root);
		q.push_back(root->right);
		q.push_back(root->left);
		while(!q.empty()) {
			TreeNode* top = q.back();
			// q.pop_back();
			if(top) {
				q.push_back(top->right);
				q.push_back(top->left);
				r.push_back(top->val);
			}
			else {
				q.pop_back();
			}
		}
		return r;
    }
	// https://leetcode.com/problems/invert-binary-tree/
	TreeNode* invertTree(TreeNode* root) {
        // 把一个节点的左右孩子做交换，一直交换直到叶节点
		// 方法1：费时间，但是空间是 O（1），13ms 
		if(root) {
			TreeNode * tmp = root->left;
			root->left = root->right;
			root->right = tmp;
			invertTree(root->left);
			invertTree(root->right);
		}

		// 方法2，用栈来保存节点， 3ms 
		deque<TreeNode*> q;
		q.push_back(root);
		while(!q.empty()) {
			TreeNode* top = q.back();
			q.pop_back();
			if(top) {
				std::swap(top->left, top->right);
				// TreeNode* tmp = top->left;
				// top->left = top->right;
				// top->right = tmp;
				if(top->left)
					q.push_back(top->left);
				if(top->right)
					q.push_back(top->right);
			}

		}
		return root;

    }
	// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
	// 寻找最低公共祖先节点。 可以是节点自身
	// 思路： 深入优先，生成到达这两个节点的路径，然后找出第一个不同的祖先，前一个就是最低相同祖先
	// 41ms, 51% defeated
	/*
	生成从 根节点 到 target 的路径到 stack 参数
	*/
	void dfs_generate_path_to_node(deque<TreeNode*>& stack, TreeNode* root, TreeNode* target, bool& found) {
		if(root == nullptr || target == nullptr || found)
			return;
		if(root == target) {
			stack.push_back(root);
			found = true;
			return;
		}
		stack.push_back(root);
		dfs_generate_path_to_node(stack, root->left, target, found);
		dfs_generate_path_to_node(stack, root->right, target, found);
		if(!found)
			stack.pop_back();
	}
	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		if(root == nullptr || p == nullptr || q == nullptr)
			return nullptr;
        
		deque<TreeNode*> stack1,stack2;
		bool found1=false, found2=false;

		dfs_generate_path_to_node(stack1, root, p, found1);
		dfs_generate_path_to_node(stack2, root, q, found2);

		if(!found1 || !found2)
			return nullptr;
		TreeNode * common_ancestor = nullptr;
		while(!stack1.empty() && !stack2.empty()) {
			TreeNode* top1 = stack1.front();
			TreeNode* top2 = stack2.front();
			if(top1 == top2) {
				common_ancestor = top1;
			}
			if(top1 != top2) {
				break;
			}
			stack1.pop_front();
			stack2.pop_front();
		}
		return common_ancestor;
    }
	//https://leetcode.com/problems/binary-tree-paths/
	// given a tree, return all root-to-leaf paths in any order
	#include<deque>
	#include<vector>
	#include<string>
	using namespace std;
	void dfs_generate_path_to_leaf(TreeNode* root, deque<TreeNode*>& stack, vector<string>& paths) {
		if(root == nullptr)
			return;
		
		stack.push_back(root);
		if(root->left == nullptr && root->right == nullptr) {
			// it's a leaf node
			string s="";
			for(auto it=stack.begin(),ie = stack.end();it!=ie;++it){
				s = s + std::to_string((*it)->val) + "->";
			}
			s=s.substr(0, s.length()-2);
			paths.push_back(s);
			stack.pop_back();
			return;
		}
		dfs_generate_path_to_leaf(root->left, stack, paths);
		dfs_generate_path_to_leaf(root->right, stack, paths);
        stack.pop_back();
	}
    vector<string> binaryTreePaths(TreeNode* root) {
        
        vector<string> r;
		deque<TreeNode*> t;
		dfs_generate_path_to_leaf(root, t, r);
		return r;
    }

	// https://leetcode.com/problems/sum-of-left-leaves/
	int sumOfLeftLeaves(TreeNode* root) {
         if(root == nullptr) {
             return 0;
        } 
        if(root->left && root->left->left == nullptr && root->left->right == nullptr)
		    return root->left->val +sumOfLeftLeaves(root->right) ;
        else
            return sumOfLeftLeaves(root->right)+sumOfLeftLeaves(root->left);
		 
    }
	// https://leetcode.com/problems/find-mode-in-binary-search-tree/
	/*Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.*/
	void find_mode(vector<int>& results, int cur_count, int cur_max, int prev_val, TreeNode* node) {
		if(node == nullptr)
			return;
		if(node->val == prev_val) {
			cur_count += 1;
			if(cur_count >= cur_max) {
				cur_max = cur_count;
				results.push_back(node->val);
			}
		}
		else {
			prev_val = node->val;
			cur_count = 1;
			if(cur_count >= cur_max) {
				cur_max = cur_count;
			}
		}
		find_mode(results, cur_count, cur_max, prev_val, node->left);
		find_mode(results, cur_count, cur_max, prev_val, node->right);
	}
	// 应该需要两趟遍历二叉树： 第一次找到最大的重复节点个数。 第二次才能根据这个最大节点个数，把最大值写入到 向量中
	/*
	寻找出现最多次的节点的个数: 中序遍历 BST 可以得到 按顺序的节点值
	@param node 树根节点
	@param cnt 当前节点出现的个数
	@param maxFreq 最多出现的节点个数
	@param prev 前一个节点的值
	*/
	void findMaxFreq(TreeNode* root, int &cnt, int &maxFreq, TreeNode* &prev){
        if(!root)return;
        
        // inorder traversal
        findMaxFreq(root->left, cnt, maxFreq, prev);
        if(prev != nullptr){
            cnt = (prev->val == root->val) ? cnt+1 : 1;
        }else{
            cnt = 1;
        }
        maxFreq = max(maxFreq, cnt);
        prev = root;
        
        findMaxFreq(root->right, cnt, maxFreq, prev);
    }
    
    void findMaxModes(TreeNode* root, int &maxFreq, int &cnt, TreeNode* &prev, vector<int>&result){
        if(!root)return;
            
        // inorder traversal
        findMaxModes(root->left, maxFreq, cnt, prev, result);
        
        if(prev != nullptr){
            cnt = (prev->val == root->val) ? cnt+1 : 1;
        }else{
            cnt = 1;
        }
        
        if( cnt == maxFreq ){
            result.push_back(root->val);
        }
        prev = root;
        
        findMaxModes(root->right, maxFreq, cnt, prev, result);
        
    }
    
    vector<int> findMode(TreeNode* root) {
        int maxFreq = 0;
        int cnt = 0;
        TreeNode* prev = nullptr;
        
        findMaxFreq(root, cnt, maxFreq, prev);
        
        vector<int> result{};
        prev = nullptr;
        cnt = 0;
        
        findMaxModes(root, maxFreq, cnt, prev, result);
        
        return result;
    }
	// https://leetcode.com/problems/minimum-absolute-difference-in-bst/
	// given a binary search tree, return the minimum absolute difference in any two node
	//Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
	void inorder_bst_to_vector(vector<int>&result, TreeNode* root) {
		if(root == nullptr)
			return;
		
		inorder_bst_to_vector(result, root->left);
		result.push_back(root->val);
		inorder_bst_to_vector(result, root->right);
	}
	int getMinimumDifference(TreeNode* root) {
        vector<int> result;
		inorder_bst_to_vector(result, root);
		int m=0xffffff;
		for(int i=0; i < result.size() - 1 ; ++i) {
			int diff = result[i+1] - result[i];
			if(diff < m)
				m = diff;
		}
		return m;
    }
	// https://leetcode.com/problems/diameter-of-binary-tree/
	// given a tree, find the diameter of the tree. a diameter is the longest length of path between any two nodes in a tree.
	// The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
	// the length of a path is the number of edges between two nodes
	int high_of_tree(TreeNode* node, int& max_dep) {
		if(node == nullptr)
			return 0 ;
		int max_left = high_of_tree(node->left, max_dep);
		int max_right = high_of_tree(node->right, max_dep);
		max_dep = max(max_dep, max_left + max_right);
		return max(max_left, max_right)+1;
	}
	int diameterOfBinaryTree(TreeNode* root) {
        // calculate the maximum depth of any node's left tree and right tree. add them up. it's the answer 
		int m = 0;
		high_of_tree(root, m);
		return m;
    }
	
	// https://leetcode.com/problems/binary-tree-tilt/
	// 计算每个节点的左子树 - 右子树的绝对值的和
	// 深度优先计算每个节点的左子树-右子树的绝对值， 累加到 sums
	int tile_of_node(TreeNode* node, int& sums) {
		// 计算一个节点的 左子树 - 右子树 的绝对值
		if(node == nullptr || (node->left == nullptr && node->right == nullptr))
			return 0;

		int sum_left = tile_of_node(node->left, sums) + (node->left? node->left->val : 0); // 左子树的节点总和 + 左子树的值
		int sum_right= tile_of_node(node->right, sums) + (node->right? node->right->val : 0); // 右子树的节点总和 + 右子树的值
		sums +=abs(sum_left - sum_right);
		return sum_left + sum_right; // 前一层调用会加上 当前节点的值，因此不用在这里加 node->val
	}
	int findTilt(TreeNode* node) {
        int sums=0;
		tile_of_node(node, sums);
		return sums;
    }

	// 572. Subtree of Another Tree
	// https://leetcode.com/problems/subtree-of-another-tree/
	// given two trees, judge whether it's a sub tree of another .
	/*
		思路3:
		注意到, 若必须是严格子树(没有多余的叶节点), 子树B 的深度
	*/
	/*思路2:
		递归遍历树A所有节点作为根节点, 判断以每个节点为根的子树是否和B相同
		Runtime: 48 ms, faster than 27.39% of C++ online submissions for Subtree of Another Tree.
		Memory Usage: 28.8 MB, less than 83.54% of C++ online submissions for Subtree of Another Tree.
	*/
	/*
		思路1:
		// 类似寻找 字符串的 子串？ 需要完全匹配，意思是从叶节点到根节点都匹配
		// 只能是 后序遍历，从底部向上对比。 
		// 为 src 树的每个节点生产后序遍历的结果， 为 target 树生成后序遍历的结果
		// 对比是否存在完全相同的结果
		Runtime: 122 ms, faster than 5.05% of C++ online submissions for Subtree of Another Tree.
		Memory Usage: 77.5 MB, less than 5.26% of C++ online submissions for Subtree of Another Tree.*/
	/*
	后序遍历一个节点， 返回后序遍历该节点的结果。 把每个节点的子树都加入到 subtrees 中
	@param node 一个节点
	@param subtrees 保存所有非叶节点
	@nodes 当前节点的后序遍历结果
	*/
	vector<int> post_order_traverse(TreeNode* node, vector< vector<int>>& subtrees, vector<int>& nodes) {
		vector<int> r;
		if(node == nullptr){
			r.push_back(0xffffff);
			return r;
		}
		
		r = post_order_traverse(node->left, subtrees, nodes);
		vector<int> right_nodes = post_order_traverse(node->right, subtrees, nodes);
		r.insert(r.end(), right_nodes.begin(), right_nodes.end());
		r.push_back(node->val);
		subtrees.push_back(r);
		return r;
	}
	/*
	判断树B是否为A的子树: 前序遍历, 若树B节点为空了,则说明树A包含树B; 若树A节点空了, 则说明树A不包含树B
	@param		rootA		树A的节点指针
	@param		rootB		树B的节点指针
	*/
	bool has_sub_tree(TreeNode* rootA, TreeNode* rootB) {
		// LeetCode的限制, 必须是完整的子树相同才是一样的. 因此需要叶节点都为空
		if(rootB == nullptr && rootA == nullptr)
			return true;
		if(rootA == nullptr || rootB == nullptr)
			return false;
		
		if(rootA->val != rootB->val)
			return false;
		
		// 因为最终会因为达到B的叶节点而返回 true
		return has_sub_tree(rootA->left, rootB->left) && has_sub_tree(rootA->right, rootB->right);
	}
	bool isSubtree(TreeNode* root, TreeNode* subRoot) {
		bool is_sub_tree = false;
		
		if(root && subRoot){
			// 只有当节点的值相同时, 才去判断 树A 是否包含 树B
			if(root->val == subRoot->val)
				is_sub_tree = has_sub_tree(root, subRoot);
			
			if(!is_sub_tree)
				is_sub_tree = isSubtree(root->left, subRoot);
			
			if(!is_sub_tree)
				is_sub_tree = isSubtree(root->right, subRoot);
		}
		return is_sub_tree;
		// // 单节点树判断
		// if(root->left == nullptr && root->right == nullptr 
		// 	&& subRoot->left == nullptr && subRoot->right == nullptr) {
		// 		return root->val == subRoot->val;
		// }
        // vector<vector<int>> subtrees_of_src, subtrees_of_dst;
		// vector<int> post_traverse_of_src, post_traverse_of_dst;
		// post_order_traverse(root, subtrees_of_src, post_traverse_of_src);
		// post_order_traverse(subRoot, subtrees_of_dst, post_traverse_of_dst);

		// // 需要对节点个数进行判断，若 size =0 , -1 会得到负数索引
		// if(subtrees_of_src.size() == 0) {
		// 	subtrees_of_src.push_back({root->val});
		// }
		// if(subtrees_of_dst.size() == 0) {
		// 	subtrees_of_dst.push_back({subRoot->val});
		// }
		// vector<int> target = subtrees_of_dst[subtrees_of_dst.size() - 1];
		// bool found = false;

		// for(auto it=subtrees_of_src.begin(),ie = subtrees_of_src.end(); 
		// 	it != ie; ++it) {
		// 	vector<int> src_sub_tree = *it;
		// 	// 子树的节点个数必须匹配
		// 	if(src_sub_tree.size() != target.size())
		// 		continue;
			
		// 	bool is_same = true;
		// 	for(int i=0; i < target.size(); ++i) {
		// 		if(target[i] != src_sub_tree[i]) {
		// 			is_same = false;
		// 			break;
		// 		}
		// 	}
		// 	if(is_same) {
		// 		found = is_same;
		// 		break;
		// 	}
		// }
		// return found;
    }
	
	// https://leetcode.com/problems/construct-string-from-binary-tree/
	// given a binary tree, construct a string with parenthesis of every node's value in pre-order.
	// root=[1,2,3,4]  "1  (2  (4)  ())   ( 3()  ())"  omit empty parenthesis and it will be 
	//  "1(2(4))(3)"   root, (left-tree), (right-tree)  left-tree=(left-val, (left-sub-tree), (right-sub-tree))
	// be caution about the one-to-one relation	map constraint. Which means that each input has exactly one output
	// there might be cases when two input has same output
	// Runtime: 20 ms, faster than 83.74% of C++ online submissions for Construct String from Binary Tree.
	string tree2str(TreeNode* root) {
		if(root != nullptr) {
			// in order to produce unique outputs, I make a parenthesis for empty left node.
			if(root->left == nullptr && root->right != nullptr) {
				return std::to_string(root->val) + string("()(") + tree2str(root->right) + string(")");
			}
			// while empty string for empty right node
			else if(root->left != nullptr && root->right == nullptr) {
				return std::to_string(root->val) + string("(") + tree2str(root->left) + string(")");
			}
			// if both left and right is empty, return current node's value, which will be parenthesis by caller.
			else if (root->left == nullptr && root->right == nullptr)
				return std::to_string(root->val);
			// if both left and right is not empty, recursive until the end
			return std::to_string(root->val) +
				string("(") + tree2str(root->left)+ string(")") + 
				string("(") + tree2str(root->right) + string(")");
		}
		return string("");
    }

	// https://leetcode.com/problems/merge-two-binary-trees/
	// 617. Merge Two Binary Trees
	// given roots of two binary tree, merge every node of these two trees. if nodes are in same position of a tree
	// sum their value as the new node's value
	// solution: use two queues to level-traverse these trees. and merge each node of queues
	// be attention to: if root1->left is null and root2->left is not null, we only need to concat the root2->left.
	// Runtime: 28 ms, faster than 98.57% of C++ online submissions for Merge Two Binary Trees.
	TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
		if(root1 == nullptr && root2 == nullptr)
			return nullptr;

		TreeNode* tmp=new TreeNode();
		tmp->val += (root1? root1->val : 0);
		tmp->val += (root2? root2->val : 0);
		if(root1 == nullptr && root2 != nullptr)
			return root2;
		else if(root1 != nullptr && root2 == nullptr)
			return root1;
		else
		{
			tmp->left = mergeTrees(root1->left , root2->left);
			tmp->right = mergeTrees(root1->right , root2->right);
		}
		return tmp;
		 
    }

	// https://leetcode.com/problems/average-of-levels-in-binary-tree/
	// 637. Average of Levels in Binary Tree
	// given a root of a binary tree. return the average value of nodes on each level in the form of an array.
	// solution : traverse by level, calculate average of each level.
	// Runtime: 31 ms, faster than 22.42% of C++ online submissions for Average of Levels in Binary Tree.
	#include<queue>
	vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> nodes;
		vector<double> results;
		if(root == nullptr)
			return results;

		nodes.push(root);
		int level_node_count;	// save nodes count in each level 
		while(!nodes.empty()) {
			double level_sum = 0, tmp_node_count = nodes.size();
			level_node_count = nodes.size();
			while(level_node_count > 0) {
				TreeNode* n = nodes.front();
				nodes.pop();
				level_sum += n->val;	// adds up all level node's value
				if(n->left)
					nodes.push(n->left);
				if(n->right)
					nodes.push(n->right);
				level_node_count -= 1;	// decrease level node count by 1
			}
			results.push_back(level_sum / tmp_node_count);

		}
		return results;
    }

	// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
	// 653. Two Sum IV - Input is a BST
	// given a root of a binary SEARCH tree and a target K, return true if 
	// there exists two elements in the BST 
	// such that their sum is equal to the given target.
	// 和在一个数组中找两个值加起来能得到 目标值的问题类似。
	// solution: traverse all nodes for given tree, use every nodes value to sub target and put the results in an array.
	// judge whether results are in the tree. // BAD idea: for if we encounter the value of itself.
	/*
	判断一颗 BST 上是否存在目标值 target 且它的节点地址不为 node
	@param root BST的树根
	@param node 被排除的节点指针
	@param target 寻找的目标值
	*/
	bool exist_value(TreeNode* root,TreeNode* node, int target) {
		if (node && root) {
			if(root->val == target && root != node)
				return true;
			if(root->val > target) {
				// search the left sub-tree
				return exist_value(root->left, node, target);
			}
			else {
				return exist_value(root->right, node, target);
			}
		}
		return false;
	}
	/*
	target - 每个节点的值保存到 subs
	T = O(N)
	*/
	void dfs_sub_node(TreeNode* node, vector<int>& subs, vector<TreeNode*>& nodes, int target) {
		if(node == nullptr)
			return;
		dfs_sub_node(node->left, subs, nodes, target);
		dfs_sub_node(node->right, subs, nodes, target);
		subs.push_back(target - node->val);
		nodes.push_back(node);
	}
	bool findTarget(TreeNode* root, int k) {
		// --------------- solution 1 : ---------------
		// Runtime: 72 ms, faster than 32.25% of C++ online submissions for Two Sum IV - Input is a BST.
		// Time = O(N * log N)
		vector<int> subs;
		vector<TreeNode*>nodes;
		dfs_sub_node(root, subs, nodes, k);
		for(int i=0; i < subs.size(); ++i) {
			if(exist_value(root, nodes[i], subs[i]))
				return true;
		}
		return false;
		// --------------- solution 1 : ---------------

    }

	// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
	// 671. Second Minimum Node In a Binary Tree
	// given a non-empty special binary tree consisting of nodes with non-negative value,
	// output the second minimum value in the set made of all the nodes' value in the whole tree.
	/*The number of nodes in the tree is in the range [1, 25].
	1 <= Node.val <= 231 - 1
	root.val == min(root.left.val, root.right.val) for each internal node of the tree.*/
	// if no such second minimum value exists, output -1 instead.
	// solution: DFS 前序遍历，若没有初始化，则设定树根为最小值，寻找大于最小值的节点
	// 若不存在，则 sec_small = 0，返回 -1 。 若存在，则返回
	// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Second
	// Memory Usage: 6.9 MB, less than 99.89% of C++ online submissions for
	void dfs_find_second_small(TreeNode* node, int& smallest, int& sec_small) {
		if(node == nullptr)
			return;

		// init smallest
		if(smallest == 0){
			smallest = node->val;
		}
		// init sec small
		else if(node->val > smallest && sec_small == 0 ){
			sec_small = node->val;
		}
		else if (node->val > smallest && node->val < sec_small){
			sec_small = node->val;
		}

		dfs_find_second_small(node->left, smallest, sec_small);
		dfs_find_second_small(node->right, smallest, sec_small);
	}
	int findSecondMinimumValue(TreeNode* root) {
        int smallest=0, sec_small=0;
		dfs_find_second_small(root, smallest, sec_small);
		if(0 == sec_small)
			return -1;
		return sec_small;
    }

	namespace N_ary_tree {
		class Node {
			public:
				int val;
				vector<Node*> children;

				Node() {}

				Node(int _val) {
					val = _val;
				}

				Node(int _val, vector<Node*> _children) {
					val = _val;
					children = _children;
				}
		};

		// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
		// 559. Maximum Depth of N-ary Tree
		// given a N-ary tree, return it's maximum depth.
		// the maximum depth is the number of nodes along the longest path from the root node 
		// to the farthest leaf node.
		// solution1 :计算每个子树的树高度，求出最大值 + 自身高度1 即可得到最长的
		// 计算node的每个子节点的高度
		// Runtime: 22 ms, faster than 51.18% of C++ online submissions for Maximum Depth of N-ary Tree.
		// solution2 :BFS 遍历，用队列保存当前一层的节点，保存当前层节点个数 n，同时出队列n次，并把每个出的节点的 child 节点加入队列
		int maxDepth(Node* node) {
			if(node == nullptr)
				return 0;
			
			int tmp_max = 0;
			for(auto it=node->children.begin(),ie = node->children.end(); it != ie; ++it) {
				int h = maxDepth(*it);
				if(tmp_max == 0)
					tmp_max = h;
				if(h > tmp_max)
					tmp_max = h;
			}
			return tmp_max + 1;
		}
		// https://leetcode.com/problems/n-ary-tree-preorder-traversal/
		// 589. N-ary Tree Preorder Traversal
		// given a n-ary tree, return it's preorder traverse result
		// Runtime: 57 ms, faster than 9.43% of C++ online submissions for N-ary Tree Preorder Traversal.
		// Runtime: 23 ms, faster than 77.45% of C++ online submissions for N-ary Tree Preorder Traversal.
		void preorder_(Node* root, vector<int>& result) {
			// solution 2
			if(root == nullptr)
				return;
			result.push_back(root->val);
			for(auto it : root->children) {
				preorder_(it, result);
			}
		}
		vector<int> preorder(Node* root) {
			vector<int> result;
			preorder_(root, result);
			return result;
			// solution 1
			// vector<int> result;
			// if(root == nullptr)
			// 	return result;
			
			// // preorder
			// result.push_back(root->val);
			// for(auto it : root->children) {
			// 	vector<int> tmp = preorder(it);
			// 	result.insert(result.end(), tmp.begin(), tmp.end());
			// }
			// return result;
		}

		// https://leetcode.com/problems/n-ary-tree-postorder-traversal/
		// 590. N-ary Tree Postorder Traversal
		// Runtime: 23 ms, faster than 78.46% of C++ online submissions for N-ary Tree
		void postorder_(Node* node, vector<int>& result) {
			if(node == nullptr)
				return;
			
			for(auto it: node->children) {
				postorder_(it, result);
			}
			result.push_back(node->val);

		}
		vector<int> postorder(Node* root) {
			vector<int> result;
			postorder_(root, result);
			return result;
    	}
		// https://leetcode.com/problems/n-ary-tree-level-order-traversal/
		// 429. N-ary Tree Level Order Traversal
		/*
			given an n-ary tree, return the level order traversal of its node's values.
			solution1: use a queue to store nodes to be traversed next time. traverse until the queue is empty.
			Runtime: 39 ms, faster than 24.66% of C++ online submissions for N-ary Tree Level Order Traversal.
			Memory Usage: 11.8 MB, less than 34.21% of C++ online submissions for N-ary Tree Level Order Traversal.

			solution2: 大神的思路, DFS 保存层级关系, 预分配结果, 直接根据层级索引找到需要写入结果的索引.
			Runtime: 23 ms, faster than 86.26% of C++ online submissions for N-ary Tree Level Order Traversal.
			Memory Usage: 11.8 MB, less than 63.14% of C++ online submissions for N-ary Tree Level Order Traversal.
		*/
		void dfs_levelOrder_(Node* node, int level, vector<vector<int>>& ret) {
			// dfs insert
			if(!node)
				return;
			if(ret.size() == level)
				ret.emplace_back();
			// ret[level].push_back(node->val); // 在这里会很慢
			for(auto it: node->children)
				dfs_levelOrder_(it, level + 1, ret);
			// 这一句放前面会变很慢
			ret[level].push_back(node->val);
		}
		vector<vector<int>> levelOrder(Node* root) {
			// solution2:
			vector<vector<int>> ret ;
			dfs_levelOrder_(root, 0, ret);
			return ret;
			// solution1:
			// queue<Node*> level_nodes;
			// vector<vector<int>> ret ;
			// if(!root)
			// 	return ret;
			// level_nodes.push(root);
			// // loop until queue is empty
			// while(!level_nodes.empty()) {
			// 	// 获取当前队列大小, 因为在遍历的时候, 会往队列加新的节点
			// 	int size = level_nodes.size();
			// 	vector<int> tmp;
			// 	while(size > 0) {
			// 		-- size;
			// 		Node* head = level_nodes.front();
			// 		level_nodes.pop();
			// 		tmp.push_back(head->val);
			// 		// 当前节点的所有子节点入队列
			// 		for(auto it:head->children)
			// 			level_nodes.push(it);
			// 	}
			// 	ret.push_back(tmp);
			// }
			// return ret;
		}
		
	};// end of namespace n-ary tree

	// https://leetcode.com/problems/search-in-a-binary-search-tree/
	// 700. Search in a Binary Search Tree
	// given a binary search tree, find the target value and return a sub-tree based on target as root.
	// solution 1: search left tree if target is smaller than root's value.
	// Runtime: 73 ms, faster than 24.44% of C++ online submissions for Search in a Binary Search Tree.
	// solution 2: loop change root pointer
	// Runtime: 45 ms, faster than 74.60% of C++ online submissions for Search in a Binary Search Tree.
	TreeNode* searchBST(TreeNode* root, int val) {
		// -------- // solution 1 
        // if(root == nullptr)
		// 	return nullptr;
		// if(root->val == val)
		// 	return root;
		// else if(root->val > val)
		// 	return searchBST(root->left, val);
		// else 
		// 	return searchBST(root->right, val);
		// -------- // solution 1 
		while(root != nullptr && root->val != val) {
			root =  (root->val > val) ?  root->left: root->right;
		}
		return root;
    }
	
	// https://leetcode.com/problems/kth-largest-element-in-a-stream/
	// 703. Kth Largest Element in a Stream
	// implement a binary search tree, and a dump method which output bst in in-order
	// traversal. change the condition, left sub-tree is bigger and right sub-tree is smaller
	// implementation of a binary search tree
	class BST {
	private:
		TreeNode* root;
	public:
		BST(){
			root = nullptr;
		}
		TreeNode* get_root() {
			return root;
		}
		// inorder traverse binary search tree and return vector result
		void inorder_traverse(vector<int>& result, TreeNode* node) {
			if(node == nullptr)
				return;
			inorder_traverse(result, node->left);
			result.push_back(node->val);
			inorder_traverse(result, node->right);
		}
		// 向 BST 添加一个值
		void push(TreeNode* node, int val) {
			if(root == nullptr)
			{
				root = new TreeNode(val);
				return;
			}
			if(node == nullptr)
				return;
			// value bigger than current node, add it to the left side
			if(node->left && node->val <= val) {
				push(node->left, val);
				return;
			}
			else if (node->right && node->val > val) {
				push(node->right, val);
				return;
			}
			if(node->val <= val) {
				node->left = new TreeNode(val);
			}
			else {
				node->right = new TreeNode(val);
			}
		}
	};
	class KthLargest {
	private:
		BST m_bst;
		int m_k;
	public:
		KthLargest(int k, vector<int>& nums) {
			m_k = k;
			for(auto i : nums) {
				m_bst.push(m_bst.get_root(), i);
			}
		}
		
		int add(int val) {
			m_bst.push(m_bst.get_root(), val);
			vector<int> result;
			m_bst.inorder_traverse(result, m_bst.get_root());
			return result[m_k-1];
		}
	};

	/**
	 * Your KthLargest object will be instantiated and called as such:
	 * KthLargest* obj = new KthLargest(k, nums);
	 * int param_1 = obj->add(val);
	 */

	// https://leetcode.com/problems/leaf-similar-trees/
	// 872. Leaf-Similar Trees
	// Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
	/*Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.*/
	// wrong solution： if node has no left and right child, it's leaf node.
	// ~~traverse by level, find out root1's all leaves. save it to a vector~~
	// traverse by level and compare it with root2's leaves
	// solution: traverse by level will fail. dfs traverse will do.
	// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Leaf-Similar Trees.
	void dfs_find_leaves(TreeNode* node, vector<int>& result) {
		if(node == nullptr)
			return;
		
		dfs_find_leaves(node->left, result);
		if(!node->left && !node->right) {
			result.push_back(node->val);
		}
		dfs_find_leaves(node->right, result);
	}
	bool leafSimilar(TreeNode* root1, TreeNode* root2) {
		if(!root1 && !root2)
			return false;
		
		vector<int> root1_leaves, root2_leaves;
		dfs_find_leaves(root1, root1_leaves);
		dfs_find_leaves(root2, root2_leaves);
		if(root1_leaves.size() != root2_leaves.size())
			return false;
		for(int i=0; i < root1_leaves.size(); ++i){
			if (root2_leaves[i] != root1_leaves[i])
				return false;
		}
		return true;
    }

	// https://leetcode.com/problems/increasing-order-search-tree/
	// 897. Increasing Order Search Tree
	// given a binary search tree, in-order travese it and make a new bst without 
	// left tree.
	/*
	Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
	*/
	// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Increasing Order Search Tree.
	// solution 2 : according to the problem, we should not create new nodes. instead, we need to change the pointer of every node.
	// inorder traverse, change node's left to null, and set node's right to it's parent if it's a left node.
	// if it's a right node, then change it's right node to it's grand-parent.
	/*Runtime: 3 ms, faster than 68.13% of C++ online submissions for Increasing Order Search Tree.
Memory Usage: 7.7 MB, less than 78.53% of C++ online submissions for Increasing Order Search Tree.*/
	TreeNode* create_bst_without_left_sub_tree(vector<int>& values, int index) {
		if(values.size() == index)
			return nullptr;
		TreeNode* node = new TreeNode(values[index]);
		node->right = create_bst_without_left_sub_tree(values, index+1);
		return node;
	}
	TreeNode* increasingBST(TreeNode* root, TreeNode* parent_node=nullptr) {
		// solution 2: 
		if(root == nullptr)
			return parent_node;
		TreeNode* head = increasingBST(root->left, root);	// 对于 根节点， 需要返回最左下角的节点作为新的树根
		root->left = nullptr;									// 左节点全部为 null
		root->right = increasingBST(root->right, parent_node); // 右节点则把当前节点的父节点，即右节点的 祖父节点 传递给他， 当右节点继续递归遇到 null 时，返回祖父节点作为它的右节点
		return head;	// 对于 根节点， 需要返回最左下角的节点作为新的树根

		// solution 1
		// if(!root)
		// 	return nullptr;
        // vector<int> values ;
		// recursive_inorderTraversal(root, values);
		// return create_bst_without_left_sub_tree(values, 0);
    }

	// https://leetcode.com/problems/range-sum-of-bst/
	// 938. Range Sum of BST
	/*Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
	The number of nodes in the tree is in the range [1, 2 * 104].
	1 <= Node.val <= 105
	1 <= low <= high <= 105
	All Node.val are unique.
	solution: Runtime: 157 ms, faster than 64.80% of C++ online submissions for Range Sum of BST.

	*/
	int rangeSumBST(TreeNode* root, int low, int high) {
        if (root == nullptr)
			return 0;
		if (root->val >= low && root->val <= high) {
			return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
		}
		else if(root->val < low) {//	if current node is less than low, find it's right sub tree
			return rangeSumBST(root->right, low, high);
		}
		else if(root->val > high) { // otherwise find it's left sub tree
			return rangeSumBST(root->left, low, high);
		}
		else {
			return 0;
		}
    }

	// https://leetcode.com/problems/univalued-binary-tree/
	// 65. Univalued Binary Tree
	/*A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Univalued Binary Tree.
	solution: according to node value constraint , set a prev value as -1. so that we could know when we hit root of  tree.
	and dfs traverse the tree. 
*/
	bool isUnivalTree(TreeNode* root, int prev = -1) {
        if(root == nullptr)
			return true;
		if(root && prev != -1) {
			// 非根节点
			if(root->val != prev)
				return false;
			return isUnivalTree(root->left, prev) && isUnivalTree(root->right, prev) ;
		}
		else {
			return isUnivalTree(root->left, root->val) && isUnivalTree(root->right, root->val) ;
		}
    }

	// https://leetcode.com/problems/cousins-in-binary-tree/
	// 993. Cousins in Binary Tree
	/*Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the **** same depth **** ****with different parents****.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
	solution: judge whether x and y are in the same level. Also they have different parent.
	dfs find the node and record depth of node and it's parent pointer.
	solution2: cousin node, by which means that they are in the same level. so we can do a level traverse.
	when both x,y was found in the same level, and they have diffrent parent. return true.
	Runtime: 4 ms, faster than 66.28% of C++ online submissions for Cousins in Binary Tree.
*/
	/*
		Runtime: 8 ms, faster than 25.80% of C++ online submissions for Cousins in Binary Tree.
		@node current node
		@parent  parent node
		@target_val  target value to search
		@depth store target node's depth
		@node_parent store target node's parent pointer
		@cur_dep cur_dep
	*/
	void dfs_get_node_depth(TreeNode* node, TreeNode* parent, int target_val, int& depth, TreeNode*& node_parent, int cur_dep) {
		if(node == nullptr || node_parent != nullptr)
			return ;
		cur_dep += 1;
		if(node->val != target_val) {
			dfs_get_node_depth(node->left, node, target_val, depth, node_parent, cur_dep);
			if(node_parent != nullptr)
				return;
			// cur_dep -= 1;
			dfs_get_node_depth(node->right, node, target_val, depth, node_parent, cur_dep);
		}
		else if(node->val == target_val && node_parent == nullptr){
			// find target 
			node_parent = parent;
			depth = cur_dep;
		}
	}
	bool isCousins(TreeNode* root, int x, int y) {
		queue<TreeNode*> q;
		bool found_x = false, found_y = false;
		if(!root) {
			return false;
		}
		q.push(root);
		while(!q.empty()) {
			found_x = found_y = false;
			int n = q.size();			// save queue size， otherwise in the loop, the queue size will change
			for(int i=0; i < n; ++i) {	// traverse this level
				TreeNode * head = q.front();
				q.pop();
				if(head->val == x)
					found_x = true;
				if(head->val == y)
					found_y = true;
				
				// x and y has same parent
				if(head->left && head->right ) {
					if((head->left->val ==x && head->right->val ==y ) || 
						(head->left->val ==y && head->right->val ==x ))
						return false;
				}
				if(head->left)
					q.push(head->left);
				if(head->right)
					q.push(head->right);
			}
			// traverse by level and found both x and y 
			if(found_x && found_y)
				return true;
			// only one node was found , so that they are not in the same level
			if(found_x || found_y)
				return false;
			
		}
		return false;

		/* solution 1 
        TreeNode* p_x = nullptr;
        TreeNode* p_y = nullptr;
		int dep_x=0, dep_y=0;
		dfs_get_node_depth(root, root, x, dep_x, p_x, 0);
		dfs_get_node_depth(root, root, y, dep_y, p_y, 0);
		return dep_x == dep_y && p_x != p_y;
		*/
    }
	
	// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
	// 1022. Sum of Root To Leaf Binary Numbers
	/*You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
	solution: 1 . use a vector to record the node's value when we dfs traverse to
	leaf node. when hit leaf node, calculate the binary number, and add it to sum.
	Runtime: deque 23 ms, faster than 6.53% of C++ online submissions for Sum of Root To Leaf Binary Numbers.
Runtime: vector 8 ms, faster than 66.31% of C++ online submissions for Sum of Root To Leaf Binary Numbers.
*/
	void dfs_sum_bin_num(TreeNode* node, vector<int>& values, int& sum) {
		if(node == nullptr)
			return;
		
		if(node->left == nullptr &&
			node->right == nullptr) {
				// hit leaf node
				int n = 2;
				for(int i=values.size()-1;i>=0; --i){
					sum += (values[i]*n);	// add up the path's node 
					n*=2;
				}
				sum += node->val;
				return;
		}
		values.push_back(node->val);
		dfs_sum_bin_num(node->left, values, sum);
		dfs_sum_bin_num(node->right, values, sum);
		values.pop_back();
	}
	int sumRootToLeaf(TreeNode* root) {
        vector<int> paths;
		int sum=0;
		dfs_sum_bin_num(root, paths, sum);
		return sum;
    }

	// https://leetcode.com/problems/recover-binary-search-tree/
	// 99. Recover Binary Search Tree
	/*
		given the root of a binary search tree, where the values of exactly two nodes
		of the tree where swapped by mistake. Recover the bst without change its structure.
		solution: (be careful, that only two nodes were swapped by mistake.)
		if you traverse by inorder, you will get a ascending order of values.
		and record every node's address. sort the values so that they are ascending.
		and set values back. 
		Time = bst O(N) + sort O(N^2) + reset O(N)
		Runtime: 60 ms, faster than 29.65% of C++ online submissions for Recover Binary Search Tree.
		solution2 :
	*/
	void recursive_inorderTraversal(TreeNode* node, vector< TreeNode* >& pointers, vector< int>& values) {
		//
		if (node) {
			recursive_inorderTraversal(node->left, pointers, values);
			pointers.push_back(node);
			values.push_back(node->val);
			recursive_inorderTraversal(node->right, pointers, values);
		}
	}
	void bubble_sort(vector<int>& values) {
		for(int i=0; i<values.size();++i) {
			for(int j=0; j<values.size()-i-1;++j) {
				if(values[j]>values[j+1]) {
					swap(values[j], values[j+1]);
				}
			}
		}
	}
	void recoverTree(TreeNode* root) {
        vector< TreeNode* > pointers;
        vector< int> values;
        recursive_inorderTraversal(root, pointers, values);	// O(N)
		bubble_sort(values);
		int i = 0;
		for(auto it:pointers) {
			it->val = values[i++];
		}
    }

	// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
	// 103. Binary Tree Zigzag Level Order Traversal
	/*
		given a binary tree, return Zigzag Level Order Traversal of it. traverse in level from left to right, and in the next level right to left.
		->
		<-
		solution1:
		solution:  level 1 ->, level 2 <- ...  it's a deque traverse. change the start of traverse from begin to end , and end to begin.
		Runtime: 3 ms, faster than 77.73% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.
		solution2:
		use two stack(vector) to store node's value.  (slower)
		Runtime: 5 ms, faster than 48.73% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.
		Memory Usage: 12.1 MB, less than 44.94% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.
	*/
	vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
		// solution2: two vector
		if(!root)	return	{};
		vector<vector<int>> ret;
		vector<TreeNode*> left_to_right;
		vector<TreeNode*> right_to_left;
		bool left_to_right_direction = true;
		left_to_right.push_back(root);
		
		// 其中一个不为空则继续
		while(!left_to_right.empty() || !right_to_left.empty()) {
			// 保存当前当前层的节点
			vector<int>	cur_level;
			if(left_to_right_direction) {
				while(!left_to_right.empty()) {
					TreeNode* cur = left_to_right.back();
					left_to_right.pop_back();
					cur_level.push_back(cur->val);
					if(cur->left)
						right_to_left.push_back(cur->left);
					if(cur->right)
						right_to_left.push_back(cur->right);
				}
			}
			else {
				while(!right_to_left.empty()) {
					TreeNode* cur = right_to_left.back();
					right_to_left.pop_back();
					cur_level.push_back(cur->val);
					if(cur->right)
						left_to_right.push_back(cur->right);
					if(cur->left)
						left_to_right.push_back(cur->left);
				}
			}
			left_to_right_direction	=	!left_to_right_direction;
			ret.push_back(cur_level);
		}
		return ret;

		// solution1 
        // deque<TreeNode*> dq;
		// vector<vector<int>> ret;
		// if(!root)
		// 	return ret;
		// dq.push_back(root);
		// bool left_to_right_direction = true;
		// while(!dq.empty()) {
		// 	int n =dq.size();
		// 	vector<int> values;
		// 	for(int i=0; i<n; ++i) {
		// 		TreeNode* node = dq.front();
		// 		dq.pop_front();
		// 		if(!left_to_right_direction)
		// 			values.push_back(node->val);
		// 		else
		// 			values.insert(values.begin(), node->val);	// use insert to append new value
		// 		if(node->right)
		// 			dq.push_back(node->right);
		// 		if(node->left)
		// 			dq.push_back(node->left);
		// 	}
		// 	ret.push_back(values);
		// 	// change direction at the end of this level
		// 	left_to_right_direction = !left_to_right_direction;
		// }
		// return ret;
    }

	// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
	// 105. Construct Binary Tree from Preorder and Inorder Traversal
	/*
		given two integer arrays preorder and inorder where preorders is the preorder traverse of binary tree and likewise. construct the binary tree.
		preorder and inorder consist of unique values.
		solution: the values are unique, so we can use a map to save it's pointers. like {1 : addr, 3 : addr, 9:addr }
		从 preorder 按顺序取节点，就是 任意一个子树的根节点。
		从 inorder 找到这个节点， 那么这个节点的左边便包含 它的左子树，右边包含它的右子树

	*/

	TreeNode* build_tree(vector<int>& preorder, vector<int>& inorder, int& rootIndex,
		int left, int right) {
			if(left > right)
				return nullptr;
			int pivot = left;	// 从inorder中找到当前 rootIndex 的节点偏移量
			while(preorder[rootIndex] != inorder[pivot]) pivot ++;
			rootIndex++;
			TreeNode* node = new TreeNode(preorder[rootIndex]);	// 构造当前子树的根节点
			
			node->left = build_tree(preorder, inorder, rootIndex, pivot, pivot-1);
			node->right = build_tree(preorder, inorder, rootIndex, pivot+1, right);
			return node;
	}
	TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
		int rootIndex = 0;
		TreeNode* root = build_tree(preorder, inorder, rootIndex, 0, preorder.size() - 1);
		return root;
	}

	// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
	// 107. Binary Tree Level Order Traversal II
	/*Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
		solution1 ： insert result in front of the vector , so you can get a bottom up traverse
		Runtime: 37 ms, faster than 5.15% of C++ online submissions for Binary Tree Level Order Traversal II.
		solution2 ： reverse the result will decrease the cost of time

		*/
	vector<vector<int>> levelOrderBottom(TreeNode* root) {
        queue<TreeNode*> q;
		vector<vector<int>> r;
		if(!root)
			return r;
		
		q.push(root);
		while(!q.empty()) {
			int n = q.size();
			vector<int> values;
			for(int i=0; i < n; ++i){
				TreeNode* front = q.front();
				q.pop();
				values.push_back(front->val);
				if(front->left)
					q.push(front->left);
				if(front->right)
					q.push(front->right);
			}
			// r.insert(r.begin(), values);
			r.push_back(values);
		}
		reverse(r.begin(), r.end());
		return r;
    }

	// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
	// 106. Construct Binary Tree from Inorder and Postorder Traversal
	/*Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
	Runtime: 88 ms, faster than 8.39% of C++ online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
		postorder 从右往左遍历，得到每颗子树的根节点
		从 inorder 获取根节点的左子树节点列表和右子树节点列表，递归构建树
	*/
	// @param root_index postorder 中的根节点索引
	// @param left   inorder 分区的起始索引
	// @param right  inorder 分区的结束索引
	TreeNode* create_tree_from_inorder_postorder(vector<int>& inorder, vector<int>& postorder, int& root_index, int left, int right) {
		if(left > right || root_index < 0)
			return nullptr;
		int pivot = left;	// 从 inorder 的左边往右边搜索
		while(inorder[pivot] != postorder[root_index]) ++pivot;
		
		root_index--;	//	postorder 往左边移动
		TreeNode* node = new TreeNode(inorder[pivot]); // 生成当前节点
		
		// 子树的构建顺序必须从右往左： 因为后续遍历的顺序Wie left,right,root. root 左边就是右节点, 因此在 root_index 左移的时候, 先取到的是右节点
		node->right = create_tree_from_inorder_postorder(inorder, postorder, root_index,
			pivot+1, right);
		node->left = create_tree_from_inorder_postorder(inorder, postorder, root_index,
			left, pivot-1);
		return node;
	}
	TreeNode* buildTree_(vector<int>& inorder, vector<int>& postorder) {
        int root_index = inorder.size() - 1;
		return create_tree_from_inorder_postorder(inorder, postorder, root_index, 0, inorder.size() -1 );// 注意索引不要溢出
    }

	// https://leetcode.com/problems/validate-binary-search-tree/
	// 98. Validate Binary Search Tree
	/*Given the root of a binary tree, determine if it is a valid binary search tree (BST).

	A valid BST is defined as follows:

	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.
	Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-231 <= Node.val <= 231 - 1
	solution1: 从底向上生成节点的值，每个子根对比左子树值列表和右子树值列表，校验大小
	注意： vector 的 insert 方法会调整容器大小，导致插入的数据会出现错乱，只能通过索引赋值。
	Runtime: 27 ms, faster than 13.72% of C++ online submissions for Validate Binary Search Tree.
	*/
	vector<int> inorder_bst(TreeNode* node,  bool& valid) {
		vector<int> r;
		if(!node || !valid)
			return r;
		vector<int> l_nodes = inorder_bst(node->left,  valid);
		vector<int> r_nodes = inorder_bst(node->right,  valid);
		for(auto i : l_nodes) {
			if(i>=node->val)
			{
				valid = false;
				return r;
			}
		}
		for(auto i : r_nodes) {
			if(i<=node->val)
			{
				valid = false;
				return r;
			}
		}
		r.resize(l_nodes.size() + r_nodes.size() + 1);
		int i = 0;
		if (l_nodes.size() > 0) {
			for (int i = 0; i < l_nodes.size(); ++i)
				r[i] = l_nodes[i];
		}
		// i 最后的取值是指向 l_nodes 的最后一个, 需要先加1
		if (r_nodes.size() > 0) {
			i = l_nodes.size();
			for (int j = 0; j < r_nodes.size(); ++j)
				r[i++] = r_nodes[j];
		}
		r[r.size()-1] = node->val;
		return r;
	}
	bool validate(TreeNode* node, TreeNode* &prev) {
		return true;
	}
	bool isValidBST(TreeNode* root) {
		// solution 3 : 7 ms	21.7 MB
        TreeNode* prev = NULL;
        return validate(root, prev);
		

		// solution 2 : traverse by queue. 29 ms	21.7 MB
		// vector<TreeNode*> stack;
		// TreeNode* prev = nullptr;
		// while(root || !stack.empty()) {
		// 	// inorder traverse: previous node must less than current node, otherwise
		// 	// it's not a sorted bst.
		// 	while(root) {
		// 		stack.push_back(root);
		// 		root = root->left;
		// 	}
		// 	TreeNode* top = stack.back();
		// 	stack.pop_back();
		// 	if(prev && prev->val >= top->val)
		// 		return false;
		// 	prev = top;
		// 	root = top->right;
		// }
		// return true;
		// solution 1 : 27 ms	27.7 MB
		// bool valid = true;
		// inorder_bst(root, valid);
		// return valid;
    }

	// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
	// 109. Convert Sorted List to Binary Search Tree
	/*
		given the head of a linked list where elements are sorted in ascending order.
		convert it to a height balanced BST.
		solution1: list 转 vector， 通过二分法， 找到中间节点 pivot，用 0,pivot-1 构造左子树
		pivot + 1, size-1 构造右子树。  因为只要是从中间去拆分，那么左右节点的个数差距不会超过1
		Runtime: 20 ms, faster than 97.00% of C++ online submissions for Convert Sorted List to Binary Search Tree.
	*/
	// 
	TreeNode* create_bst_from_sorted_list(vector<int>& values, int left, int right) {
		if(left > right) {
			return nullptr;
		}
		// 找到根节点
		int pivot = ( right+ left +1) / 2 ;	// +1 是为了取出值较大的节点的索引
		TreeNode* sub_root = new TreeNode(values[pivot]);
		sub_root->left = create_bst_from_sorted_list(values, left, pivot-1);
		sub_root->right = create_bst_from_sorted_list(values, pivot+1, right);
		return sub_root;
	}

	TreeNode* sortedListToBST(ListNode* head) {
        vector<int> values;
		if(!head)
			return nullptr;
		while(head) {
			values.push_back(head->val);
			head = head->next;
		}
		return create_bst_from_sorted_list(values, 0, values.size()-1);
    }

	// https://leetcode.com/problems/path-sum-ii/
	// 113. Path Sum II
	/*given a root of binary tree and an integer target sum， return all root-to-leaf
	paths where the sum of the node values in the path equal target sum. Each path
	should be returned as a list of node values.
	solution： 和之前的一个 sum 类似，之前是只要找到一个就可以，现在是全部
	深度优先遍历, 进入一个节点 push 一个值, 同时加到 sum, 返回的时候出对应的值, 同时 sum 减去当前节点
	Runtime: 20 ms, faster than 46.53% of C++ online submissions for Path Sum II.

	*/
	void path_sum(TreeNode* node, int& sum, vector<int>& path_nodes, 
		vector<vector<int>>& result, int targetSum) {
		if(node == nullptr)
			return;
		sum += node->val;
		path_nodes.push_back(node->val);
		if(node->left == nullptr && node->right == nullptr) {
			// leaf node: check sum
			if(sum ==targetSum) {
				vector<int> tmp = path_nodes;
				result.push_back(tmp);
			}
			sum -= node->val;
			path_nodes.pop_back();
			return;
		}
		path_sum(node->left, sum, path_nodes, result, targetSum);
		path_sum(node->right, sum, path_nodes, result, targetSum);
		sum -= node->val;
		path_nodes.pop_back();
	}
	vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
		if(!root)
			return result;
		int sum = 0;
		vector<int> path_nodes;
		path_sum(root, sum, path_nodes, result, targetSum);
		return result;
    }

	// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
	// 114. Flatten Binary Tree to Linked List
	/*
		given a root of binary tree, flatten the tree into a 'linked list'.
		it should be in the same order as a pre-order traversal of the binary tree.
		solution1 ： 学来的。 通过 right/left/root 遍历二叉树，在回溯的过程中，保存遍历过的前一个节点
		Runtime: 8 ms, faster than 59.99% of C++ online submissions for Flatten Binary Tree to Linked List.
	*/
	// 把当前节点的右节点设置为 next，左节点设置为 null
	void flat_to_right(TreeNode* node, TreeNode*& next) {
		if(!node)
			return;
		flat_to_right(node->right, next);
		flat_to_right(node->left, next);
		node->right = next;
		node->left = nullptr;
		next = node;
	}
    void flatten(TreeNode* root) {
		if(!root)
			return;
		TreeNode* tmp = nullptr;
		flat_to_right(root, tmp);
    }

	// https://leetcode.com/problems/sum-root-to-leaf-numbers/
	// 129. Sum Root to Leaf Numbers
	/*
		You are given the root of a binary tree containing digits from 0 to 9 only.
		Each root-to-leaf path in the tree represents a number.
		For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
		Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
		solution: 
			dfs: 一个变量保存到当前节点构成的数字  cur_val , 一个变量保存最终的 和 sum, 
			每进入一层计算一次 cur_val = val + cur_val * 10
			遇到 null 节点时, 把 cur_val
			Runtime: 4 ms, faster than 43.19% of C++ online submissions for Sum Root to Leaf Numbers.
			Memory Usage: 9.3 MB, less than 49.14% of C++ online submissions for Sum Root to Leaf Numbers.
	*/
	void dfs_sumNumbers(TreeNode* root, int cur_val, int& sum) {
        if(!root)
			return ;
		if(root->left == nullptr && root->right == nullptr) {
			// the leaf
			sum += cur_val*10 + root->val;
			return ;
		}
		dfs_sumNumbers(root->left, cur_val*10 + root->val, sum);
		dfs_sumNumbers(root->right, cur_val*10 + root->val, sum);
    }
	int sumNumbers(TreeNode* root) {
        if(!root)
			return 0;
		int sum =0, cur_val = 0;
		dfs_sumNumbers(root, cur_val, sum);
		return sum;
    }
	// https://leetcode.com/problems/serialize-and-deserialize-bst/
	// 449. Serialize and Deserialize BST
	/*
		design a class which can serialize a bst to a string , and convert it back to bst.
		solution: 中序遍历得到顺序的结果; 然后用中序遍历构造 bst ... 直接代码复用啊..
		solution2: 这是一颗二叉搜索树, 并且数值都是 >=0 . 
		不能复用, 因为若存在重复的值, 会有问题.
		通过前序遍历序列化二叉树，遇到空指针添加 $, 
	*/
	class Codec {
	private:
		string m_value;	//	to store the encoded binary tree
		int    m_index; //  to store current index of string to deserialize
		int		read_int(const char * str)
		{
			// 2,1,6,$,$,$,3,$,5,$,$,
			printf("current %s\n", str);
			int sum = 0, radix = 1;
			while(*str && *str != ',')
			{
				sum += sum*radix + (*str - '0');
				radix *= 10;
				++str;
			}
			return sum;
		}
		bool	decode_value(const char * str, int& value)	//	decode a int value from string, return true if success
		{
			if(!str || *str == 0 || *str == '$')
				return false;
			// sscanf_s(str, "%d", &value);
			value = read_int(str);
			return true;
		}
		// 123,34
		void	find_next_sep(const char * str)
		{
			if(!str)
				return;
			while(*(str+ m_index) && *(str + m_index) != ',')
				++m_index;
			++m_index;
		}
		string _serialize(TreeNode* root)
		{
			if(!root) {
				m_value += "$,";
				return m_value;
			}
			// char buf[35];
			// m_value += itoa(root->val, buf, 10);
			m_value += std::to_string(root->val);
			m_value += ",";
			_serialize(root->left);
			_serialize(root->right);
			return m_value;

		}
		TreeNode* _deserialize()
		{
			// move input string to before next seperator. and decode a value
			int num;
			if(decode_value(m_value.c_str() + m_index, num)) {
				TreeNode* node = new TreeNode();
				node->val =	num;
				// find_next_sep(m_value.c_str() + m_index);
				find_next_sep(m_value.c_str());
				node->left = _deserialize();
				// find_next_sep(m_value.c_str() + m_index);
				find_next_sep(m_value.c_str());
				node->right = _deserialize();
				return node;
			}
			return nullptr;
		}
	public:

		// Encodes a tree to a single string.
		string serialize(TreeNode* root) {
			m_value	=	"";
			return _serialize(root);
		}

		// Decodes your encoded data to tree.
		TreeNode* deserialize(string data) {
			m_index = 	0;
			m_value	=	data;
			return _deserialize();
		}
	};
	// https://leetcode.com/problems/delete-node-in-a-bst/
	// 450. Delete Node in a BST
	/*
		given a root node reference of a BST and a key. delete the node with the given key in the BST. return the root node of the BST.
		hint: 1.search the key to remove. 2.if the node if found, delete it.
		constraints: each node has unique value.
		solution1: 判断删除的节点类型: 叶子节点(直接删除父节点对它的引用); 
		非叶子非根节点(最多影响两个节点, 它的父节点和一个子节点);
		根节点(找到右子树的最左节点,)
		solution2: 中序遍历, 找到目标节点后, 把后面的节点的值往前面修改, 最后只要删除最后一个节点的引用即可.
		类似从 [1,2,3,4,5,] 删除4 , 得到 [1,2,3,5,] 把5的值修改到4上, 最后再删除对原始5的引用.
		solution3: 注意这是BST, 搜索应该是 logN 时间复杂度. 前一个算法是 N 的时间复杂.
		solution4: 别人的. 删除节点主要3种情况: 
		a.叶子节点 : 直接删除父节点对它的引用
		b.目标有一个子节点: 让目标的父节点引用它的子节点
		c:目标有两个子节点: 替换目标节点为 左子树最大的值 或 右子树最小的值, 同时删除
		选择的子树中 被替换值的节点
	*/
	// void inorder_search_delete_bst(TreeNode* cur, TreeNode*& prev, TreeNode*& prev_2, int key, bool& found) {
	// 	if(!cur)
	// 		return;
	// 	inorder_search_delete_bst(cur->left, cur,prev_2, key, found);
	// 	if(found && prev) {
	// 		// 找到目标, 开始覆盖
	// 		prev->val = cur->val;
	// 	}
	// 	prev_2 = prev;
	// 	prev = cur;	//	记录当前节点
	// 	if(cur->val == key) {
	// 		found = true;	// 可以进行替换
	// 	}
	// 	inorder_search_delete_bst(cur->right, cur,prev_2, key, found);
	// }
	/*
		二分查找目标, 找到设置它的父节点
		@param	node	节点指针
		@param	key		目标数字
		@param	parent	保存目标数字的父节点指针
	*/
	// void bst_search(TreeNode* node, int key, TreeNode*& parent) {
	// 	if(!node)
	// 		return;
	// 	if(node->val == key)
	// 		return;
	// 	// search the right sub tree
	// 	if(key > node->val) {
	// 		// if found target, set its parent
	// 		if(node->right && node->right->val == key){
	// 			parent = node;
	// 			return;
	// 		}
	// 		bst_search(node->right, key, parent);
	// 	}
	// 	// search the left sub tree 
	// 	else {
	// 		if(node->left && node->left->val == key){
	// 			parent = node;
	// 			return;
	// 		}
	// 		bst_search(node->left, key, parent);
	// 	}
	// }
	TreeNode* deleteNode(TreeNode* root, int key) {
		if(root)
			if(root->val < key)			// root 小于 target 搜索 右子树
				root->right = deleteNode(root->right, key);
			else if(root->val > key)	// root 大于 target 搜索 左子树
				root->left = deleteNode(root->left, key);
			else {
				// found target key with 3 conditions
				// a. target has no child
				if(!root->left && !root->right)
					return nullptr;
				// b. target has one child, return it
				if(!root->left || !root->right)
					return root->left ? root->left : root->right;
				// c. target has two children. search for the greatest node in the left sub-tree or smallest node in the right sub-tree.
				TreeNode* tmp = root->left;	// I search for the left sub-tree
				while(tmp->right)	tmp = tmp->right;
				// replace current node's value with the greatest node in the left sub-tree
				root->val = tmp->val;
				// delete the duplicated node
				root->left = deleteNode(root->left, root->val);
			}
		return root;
		// if(!root)
		// 	return nullptr;

		// TreeNode* parent=nullptr;
		// bst_search(root, key, parent);
		// // 判断是否为根节点
		// if(root->val == key) {
		// 	// 把左子树最右的节点作为根
		// 	// 或者把右子树最左的节点作为根
		// }
		// // 找到节点的父节点了
		// if(parent) {
		// 	// 确认节点
		// 	TreeNode* target = nullptr;
		// 	if(parent->left && parent->left->val == key)
		// 		target = parent->left;
		// 	else
		// 		target = parent->right;
			
		// }
		// // 没找到节点直接返回
		// else {
		// 	return root;
		// }
        // if(!root)
		// 	return nullptr;
		// bool found = false;
		// TreeNode* prev = nullptr, *prev_2;
		// inorder_search_delete_bst(root, prev, prev_2, key, found);
		// if(found) {
		// 	// 
		// }
    }
};
