#include <iostream>
#include<string>
#include<vector>
#include<list>
#include<queue>
#include<deque>
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
	
	/*
		create a binary tree from a set of node's value. such as {1,2,4, null, 7}
		return the root of the tree
		:attension : if a node's value is zero, how do you differ from null pointer?
	*/
	TreeNode* create_from_vector(vector<int*> values) {
		if(values.size() == 0)
			return nullptr;
		
		queue<TreeNode*> q;
		int val = static_cast<int> (values[0]);
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
			int val_left = static_cast<int>(values[index]);
			if(val_left == 0)
				front->left = nullptr;
			else{
				front->left = new TreeNode(val_left);
				q.push(front->left);
			}
			++index;
			if(index < value.size()) {
				int val_right = static_cast<int>(values[index]);
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
	// 类似寻找 字符串的 子串？ 需要完全匹配，意思是从叶节点到根节点都匹配
	// 只能是 后序遍历，从底部向上对比。 
	// 为 src 树的每个节点生产后序遍历的结果， 为 target 树生成后序遍历的结果
	// 对比是否存在完全相同的结果
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
	bool isSubtree(TreeNode* root, TreeNode* subRoot) {
		// 单节点树判断
		if(root->left == nullptr && root->right == nullptr 
			&& subRoot->left == nullptr && subRoot->right == nullptr) {
				return root->val == subRoot->val;
		}
        vector<vector<int>> subtrees_of_src, subtrees_of_dst;
		vector<int> post_traverse_of_src, post_traverse_of_dst;
		post_order_traverse(root, subtrees_of_src, post_traverse_of_src);
		post_order_traverse(subRoot, subtrees_of_dst, post_traverse_of_dst);

		// 需要对节点个数进行判断，若 size =0 , -1 会得到负数索引
		if(subtrees_of_src.size() == 0) {
			subtrees_of_src.push_back({root->val});
		}
		if(subtrees_of_dst.size() == 0) {
			subtrees_of_dst.push_back({subRoot->val});
		}
		vector<int> target = subtrees_of_dst[subtrees_of_dst.size() - 1];
		bool found = false;

		for(auto it=subtrees_of_src.begin(),ie = subtrees_of_src.end(); 
			it != ie; ++it) {
			vector<int> src_sub_tree = *it;
			// 子树的节点个数必须匹配
			if(src_sub_tree.size() != target.size())
				continue;
			
			bool is_same = true;
			for(int i=0; i < target.size(); ++i) {
				if(target[i] != src_sub_tree[i]) {
					is_same = false;
					break;
				}
			}
			if(is_same) {
				found = is_same;
				break;
			}
		}
		return found;
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
};
