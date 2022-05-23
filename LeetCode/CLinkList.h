#pragma once
#include<vector>
#include<iostream>
#include<random>
using std::vector;
namespace LinkList {


	class CLinkList
	{
	public:
		// Definition for singly-linked list.
		//template<class T>
		struct ListNode {
			int val;
			ListNode* next;
			ListNode() : val(0), next(nullptr) {}
			ListNode(int x) : val(x), next(nullptr) {}
			ListNode(int x, ListNode* next) : val(x), next(next) {}
		};
		
		static ListNode* next(ListNode* node) {
			if (node != nullptr)
				return node->next;
			return nullptr;
		}
		static ListNode* insert(ListNode* node,int data) {
			ListNode* ret = new ListNode(data, node);
			if (node)
				node->next = ret;
			return ret;
		}

	public:
		// https://leetcode.com/problems/split-linked-list-in-parts/
		// 725. Split Linked List in Parts
		/*
			把一个链表平均分为 k 个子链表, 要求顺序不变, 且每个子链表长度相差不超过1个节点, 前面的链表长度更长
			solution: 1. 计算链表长度 s, 除以k得到每个子链表长度 s/k = l , 若 l == 0 , 则每个链表长度为1 , 不足的用 null 填充,
			若 l > 0 , 每个链表长度为 l, 多余的 s%k = left, 前面的子链表, 每个长度都 + 1 直到 left = 0. 
			先插入链表到结果, 然后找到 断链的地方. 
			Runtime: 7 ms, faster than 79.43% of C++ online submissions for Split Linked List in Parts.
			Memory Usage: 8.8 MB, less than 60.80% of C++ online submissions for Split Linked List in Parts.
		*/
		vector<ListNode*> splitListToParts(ListNode* head, int k) {
			int length = 0;
			ListNode* tmp = head;
			vector<ListNode*> ret;
			// if(!head)	// 可以传入空的链表
			// 	return ret;
			// 计算长度
			while(tmp) {
				++length;
				tmp = tmp->next;
			}
			int l = length / k;
			int left = length % k;
			// k 大于节点个数
			if(l == 0) {
				while (k > 0)
				{
					if(head) {
						ret.push_back(head);
						tmp = head->next;
						head->next = nullptr;
						head = tmp;
					}
					else {
						ret.push_back(nullptr);
					}
					--k;
				}
				return ret;
			}
			// k 小于节点个数
			while (head)
			{
				// 每个子链长度为 l + 1
				int tmp_len = 1;
				ret.push_back(head);
				while(tmp_len < l) {
					head = head->next;
					++tmp_len;
				}
				// 多余的 1个节点
				if(left) {
					head = head->next;
					--left;
				}
				tmp = head->next;
				head->next = nullptr;
				head = tmp;
			}
			return ret;
		}

		// remove n-th node from the end of list . return the head
		// find the node and it's previous node , change prev node.next = cur.next
		// edge situation : the removed node is the head .
		// https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
		static ListNode* removeNthFromEnd(ListNode* head, int n) {
			using std::vector;
			vector<ListNode*> nodes;
			ListNode* ret = head, * cur_node = nullptr, *prev_node=nullptr,* tmp_head=head;
			while (head != NULL) {
				nodes.push_back(head);
				if (head->next == nullptr)
					break;
				head = head->next;
			}
			int remove_index = nodes.size() - n;
			if (remove_index < 0) {
				return tmp_head;
			}
			else if (remove_index == 0) {
				// remove the first node 
				ret = tmp_head->next;
				//free(tmp_head);
			}
			else {
				// get previous 
				prev_node = nodes[remove_index - 1];
				cur_node = nodes[remove_index];
				prev_node->next = cur_node->next;
				//free(cur_node);
			}
			return ret;
		}
		/*
		merge two sorted list into one sorted list. iterate over two list,
		find the smaller one and insert it into the new list, change list pointers.
		*/
		static ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
			ListNode* head = nullptr, * cur_node = nullptr,
				*cur_l1= list1, *cul_l2= list2;
			while (cur_l1 || cul_l2) {
				int cur_val_1 = 0, cur_val_2 = 0;
				ListNode* tmp = nullptr;
				if (cur_l1 != nullptr)
					cur_val_1 = cur_l1->val;
				if (cul_l2 != nullptr)
					cur_val_2 = cul_l2->val;
				// bost list not empty 
				if (cur_l1 && cul_l2) {
					if (cur_val_1 < cur_val_2) {
						tmp = insert(cur_node, cur_val_1);
						cur_l1 = cur_l1->next;
					}
					else {
						tmp = insert(cur_node, cur_val_2);
						cul_l2 = cul_l2->next;
					}
					cur_node = tmp;
					if (head == nullptr) {
						 head = tmp;
					}
					continue;
				}
				// list 1 not empty, concat it 
				else if (cur_l1) {
					if (cur_node) {
						cur_node->next = cur_l1;
					}
					else {
						head = cur_node = cur_l1;
					}
					break;
				}
				// list 1 not empty, concat it 
				else if (cul_l2) {
					if (cur_node) {
						cur_node->next = cul_l2;
					}
					else {
						head = cur_node = cul_l2;
					}
					break;
				}
			}
			return head;
		}
		// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
		// remove all duplicated number from a sorted list, return it's head.
		// my bad: it wishes to remove all node which have duplicated value. thus: [1,1,2]=> [2]
		// we need four pointers,and one bool flag has_dup. 
		// first is for store the original head
		// second is for the prev node, third is for the cur node, fourth is for next node

		static ListNode* deleteDuplicates(ListNode* head) {
			ListNode* next = nullptr;
			ListNode* top = nullptr;
			ListNode* tmp_stack[400] = { 0 };
			int sp = -1;						// stack pointer
			bool has_dup = false;
			if (head == nullptr || head->next == nullptr)
					return head;
			next = head->next;
			tmp_stack[++sp] = head;	// push first node to stack 
			while (next) {			// loop until we hit the last node
				if (sp > -1) {
					// the stack is not empty
					top = tmp_stack[sp];	// get the top node from stack
					if (top->val == next->val) {
						// mark duplicate node found, remove next from list, update top's next 
						has_dup = true;
						top->next = next->next;
						next = next->next;
					}
					else {
						// we need to check if previously found a duplicate node
						if (has_dup) {
							// stack pop
							ListNode* tmp = top;
							if (sp > 0) {
								top = tmp_stack[--sp];
							}
							else {
								top = nullptr;
								--sp;
							}
							// reset top's next 
							if (top)
								top->next = next;
						}
						// mark not duplicated
						has_dup = false;
						// not duplicate node, push the next to stack 
						tmp_stack[++sp] = next;
						next = next->next;
					}

				}
				else {
					// stack is empty, push one node 
					tmp_stack[++sp] = next;
					next = next->next;
				}
			}
			// the last round out , 
			if (has_dup) {
				// stack pop
				ListNode* tmp = top;
				if (sp > 0) {
					top = tmp_stack[--sp];
				}
				else {
					top = nullptr;
					--sp;
				}
				// set 
				if (top)
					top->next = next;
			}
			if (sp > -1)
				return tmp_stack[0];
			return nullptr;
		}
		// https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
		// I resolved yesterday ... but codes were deleted...
		static ListNode* deleteDuplicates2(ListNode* head) {
			ListNode *cur = head, *next = nullptr;
			if (head == nullptr || head->next == nullptr)
				return head;
			next = cur->next;
			while (next) {
				// loop until we hit the end 
				if (cur->val == next->val) {
					// update cur's next
					cur->next = next->next;
					next = next->next;
					continue;
				}
				cur = next;
				next = next->next;
			}
			return head;
		}
		
		// https://leetcode.com/problems/partition-list/
		/*
		prev =nul, cur =1, 
		prev=1, cur=4
		if prev > cur  and prev >= 3 and cur != 3
			exchange prev and cur 
		else
			prev = cur
			cur = cur->next
		*/
		static bool check_partition(ListNode* head, int x) {
			bool small = true, great = false, has_changed = false, ret = true;
			while (head != nullptr) {
				if (has_changed == false && small && head->val < x) {
					head = head->next;
					continue;
				}
				else {
					small = false;
					has_changed = true;
					great = true;
				}
				if (has_changed && great && head->val >= x) {
					head = head->next;
					continue;
				}
				else if (has_changed ){
					return false;
				}
			}
			return ret;
		}
		static ListNode* partition(ListNode* head, int x) {
			ListNode* small_head = new ListNode(0);
			ListNode* great_head = new ListNode(0);
			ListNode* cur_small = small_head, * cur_great = great_head;
			if (head == nullptr || head->next == nullptr)
				return head;
			while (head != nullptr) {
				if (head->val < x) {
					// insert into small;
					cur_small->next = head;
					cur_small = head;
					head = head->next;
				}
				else {
					cur_great->next = head;
					cur_great = head;
					head = head->next;
				} 
			}
			cur_great->next = NULL;
			cur_small->next = great_head->next;
			if(small_head->next)
				return small_head->next;

			return great_head->next;
		}

		static ListNode* reverseList(ListNode* head) {
			// given a list , reverse it.
			// we need 3 nodes: prev, cur, tmp . let tmp = cur->next, cur->next= prev, prev = cur, cur = tmp
			if (head == nullptr || head->next == nullptr)
				return head;
			ListNode* prev=nullptr, *cur=head, *tmp;
			while(cur != nullptr) {
				tmp = cur->next;
				cur->next = prev;
				prev = cur;
				cur = tmp;
			}
			return prev;
		}

		// https://leetcode.com/problems/reverse-linked-list-ii/

		static ListNode* reverseBetween(ListNode* head, int left, int right) {
			// like reverse a link list, we need to find where the break nodes are. break_1, break_2
			// between break_1 and break_2, reverse the list, and then, hook it back to where it was break.
			if (head == nullptr || head->next == nullptr || left >= right)
				return head;
			int i = 1;
			ListNode * cur = head, *break_1 ,*break_2 = nullptr ;
			ListNode* prev=nullptr,  *tmp;
			while(cur != nullptr) {
				if(i > right)
				{
					break;
				}
				if (i < left) {
					// before reverse start
					++i;
					prev = cur;
					cur = cur->next;
					continue;
				}
				// i >= left , begin reverse procedure
				if (i == left) {
					// save the break point 1 , 2
					break_1 = prev;
					break_2 = cur;
				}
				++i;
				tmp = cur->next;
				cur->next = prev;
				prev = cur;
				cur = tmp;
			}
			// need to fix two nodes: 
			if (break_1) {
				break_1->next = prev;
			}
			if (break_2) {
				break_2->next = cur;
			}
			if (left == 1) {
				// reverse from first position
				return prev;
			}
			else {
				return head;
			}
		}

		// https://leetcode.com/problems/linked-list-cycle/
		// 141. Linked List Cycle
		/*Given head, the head of a linked list, determine if the linked list has a cycle in it.

	There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

	Return true if there is a cycle in the linked list. Otherwise, return false.
		solution1 ： 用两个循环来找是否有环. 类似冒泡排序算法 // 超时
		solution2 ： 用map： 34 ms, faster than 5.29% of C++ online submissions for Linked List Cycle.
		solution3 ： 赛跑。 在一个环里，a跑得比b快一倍，那么一定时间后，a会再次遇到b。 Runtime: 12 ms, faster than 74.89% of C++ online submissions for Linked List Cycle.
	*/
		bool hasCycle(ListNode *head) {
			if(!head || head->next == nullptr)	
				return false;
			ListNode * fast=head, *slow=head;
			while(fast && fast->next) {
				fast = fast->next->next;
				slow = slow->next;
				if(fast == slow)
					return true;
			}
			return false;

			
			// if(!head || head->next == nullptr)	
			// 	return false;
			// map<ListNode*, int> m;
			// while(head) {
			// 	auto r = m.find(head);
			// 	if(r != m.end()) 
			// 		return true;
			// 	m[head] = head->val;
			// 	head = head->next;
			// }
			// return false;


			// bool has_cycle = false;
			// ListNode* cur=head, *iter = nullptr;
			// while (cur && !has_cycle)
			// {
			// 	iter = cur->next;
			// 	while(iter) {
			// 		if(iter->next == cur) {
			// 			has_cycle = true;
			// 			break;
			// 		}
			// 		iter = iter->next;
			// 	}
			// 	cur = cur->next;
			// }
			// return has_cycle;
			
		}
		// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
		// 116. Populating Next Right Pointers in Each Node
		/*You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
		Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

		Initially, all next pointers are set to NULL.
		solution1: use queue. 直接超时。
		solution2：先测量树的深度h，然后从1到h深度遍历二叉树，记录prev节点和cur节点，
		若prev节点不为空，则prev->next=cur，迭代到结束。 一次通过
		Runtime: 24 ms, faster than 63.47% of C++ online submissions for Populating Next Right Pointers in Each Node.
	Memory Usage: 16.7 MB, less than 85.79% of C++ online submissions for Populating Next Right Pointers in Each Node.
		*/
		class Node {
		public:
			int val;
			Node* left;
			Node* right;
			Node* next;

			Node() : val(0), left(NULL), right(NULL), next(NULL) {}

			Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

			Node(int _val, Node* _left, Node* _right, Node* _next)
				: val(_val), left(_left), right(_right), next(_next) {}
		};
		#include<queue>
		//using std::queue;
		// 计算树的最大高度
		void tree_get_height(Node* root,int cur_dep, int& max_dep) {
			if(!root)
				return;
			cur_dep++;
			if(cur_dep > max_dep)
				max_dep = cur_dep;
			tree_get_height(root->left, cur_dep, max_dep);
			tree_get_height(root->right, cur_dep, max_dep);
		}
		// 连接树的每一层节点
		/*
			@prev			前一个节点
			@cur			当前节点
			@target_level	目标层
			@cur_level		当前所在层
		*/
		void tree_connect(Node*& prev, Node* cur, int target_level, int cur_level) {
			if(!cur || cur_level > target_level)
				return;
			cur_level++;
			// 递归达到目标层，修改节点
			if(prev && cur_level == target_level) {
				prev->next = cur;
				prev = cur;
			}
			// 初始化
			else if(prev == nullptr && cur_level == target_level) {
				prev = cur;
			}
			tree_connect(prev, cur->left, target_level, cur_level);
			tree_connect(prev, cur->right, target_level, cur_level);
		}
		Node* connect(Node* root) {
			if(!root)
				return root;
			int tree_height = 0, cur_dep = 0;
			tree_get_height(root, cur_dep, tree_height);
			for(int i=1; i <= tree_height; ++i) {
				Node* prev=nullptr;
				cur_dep = 0;
				tree_connect(prev, root, i, cur_dep);
			}
			return root;
			// if(!root)
			// 	return root;
			// queue<Node*> q;
			// q.push(root);
			// while(!q.empty()) {
			// 	int size = q.size();
			// 	Node* prev = nullptr;
			// 	while(size > 0) {
			// 		Node* head = q.front();
			// 		if(prev != nullptr)
			// 			prev->next = head;
			// 		prev = head;
			// 		size -= 1;
			// 		q.push(head->left);
			// 		q.push(head->right);
			// 	}
			// }
			// return root;
		}

		// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/
		// 117. Populating Next Right Pointers in Each Node II
		/*
			和前一题一样，不同的是这颗不是完全二叉树。 某些层节点不全。
			直接提交前一题即可。
			Runtime: 36 ms, faster than 5.46% of C++ online submissions for Populating Next Right Pointers in Each Node II.
			Memory Usage: 17.4 MB, less than 81.34% of C++ online submissions for Populating Next Right Pointers in Each Node II.
		*/

		// https://leetcode.com/problems/copy-list-with-random-pointer/
		// 138. Copy List with Random Pointer
		/*
			给定一个链表，每个节点还有一个random指针指向任意一个节点， 深拷贝这个链表，且新的链表不能指向旧的链表。
			solution1： 用一个无序字典存储 它的地址和节点索引； 用一个vector存储新分配的链表节点的地址。
			Runtime: 12 ms, faster than 54.98% of C++ online submissions for Copy List with Random Pointer.
			Memory Usage: 11.5 MB, less than 9.74% of C++ online submissions for Copy List with Random Pointer.
			Runtime: 8 ms, faster than 82.66% of C++ online submissions for Copy List with Random Pointer.
			Memory Usage: 11.3 MB, less than 63.36% of C++ online submissions for Copy List with Random Pointer.
		*/
		// https://leetcode.com/problems/linked-list-cycle-ii/
		// 142. Linked List Cycle II
		// Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
		ListNode *detectCycle(ListNode *head) {
			ListNode* fast=head,*slow=head;
			while(fast && fast->next) {
				fast = fast->next->next;
				slow = slow->next;
				if(fast && fast->next == slow) {
					return slow;
				}
				if(fast == slow)
					return slow;
			}
			return nullptr;
		}

		// https://leetcode.com/problems/reorder-list/
		//143. Reorder List
		/*You are given the head of a singly linked-list. The list can be represented as:

		L0 → L1 → … → Ln - 1 → Ln
		Reorder the list to be on the following form:

		L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
		You may not modify the values in the list's nodes. Only nodes themselves may be changed.
		solution1： iterate over the list and save each node in a vector. 推导过程：
		奇数和偶数个的节点，最终都把left节点的next设置为null
		Input: head = [1,2,3,4,5]
		Output: [1,5,2,4,3]
		while l < r:
			l = 0
			r = 4
			v[r]->next = v[l]->next
			v[l]->next = v[r]
			1->5
			5->2
			++l;
			--r;
			
			// [1,5,2,3,4]
			l = 1
			r = 3
			4->3 
			2->4
			3->4	--->>> fix this 
			l=2
			r=2

		if l == r
				v[l]->next = null;

		1,5,2,4,3

		[1,2,3,4]
		[1,4,2,3]
		l=0
		r=3
		1->4
		4->2

		l=1
		r=2
		3->3
		2->3

		l=2
		r=1
		if l>r:
			l->next=null 
		1->4->2->3->3

		[1,5,2,4,3]
		Runtime: 44 ms, faster than 77.60% of C++ online submissions for Reorder List.
		Memory Usage: 19 MB, less than 12.71% of C++ online submissions for Reorder List.
		*/
		void reorderList(ListNode* head) {
			vector<ListNode*> nodes;
			int left=0,right=0;
			while(head) {
				nodes.push_back(head);
				head = head->next;
			}
			right = nodes.size() - 1;
			while(left < right) {
				nodes[right]->next = nodes[left]->next;
				nodes[left]->next = nodes[right];
				++left;
				--right;
			}
			// if(left == right)
			nodes[left]->next = nullptr;
		}

		// https://leetcode.com/problems/insertion-sort-list/
		// 147. Insertion Sort List
		/*给定一个单链表，完成插入排序。 流程：
		1.Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
		2.At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the  sorted list and inserts it there.
		3.It repeats until no input elements remain.
		插入排序思想： 两个数组，一个是已经排序的，另一个是无序的，从无序的开始迭代，逐个插入到有序的数组中。
		每次迭代从输入数据取出一个元素，在有序链表中找到一个合适的位置插入，直到输入数据为空。
		从小到大排序。
		Runtime: 41 ms, faster than 65.92% of C++ online submissions for Insertion Sort List.
		Memory Usage: 9.4 MB, less than 96.07% of C++ online submissions for Insertion Sort List.
		*/
		ListNode* insertionSortList(ListNode* head) {
			if(!head || head->next == nullptr)
				return head;
			ListNode* ret_head = nullptr,* unsorted_head;// 一个保存有序链表头指针，一个保存 无序链表头指针
			while(head) {
				// 初始化
				if(!ret_head){
					ret_head = head;
					head = head->next;
					ret_head->next = nullptr;	// 关键点：有序链表的末尾先置空
					continue;
				}
				// 开始插入排序
				ListNode* tmp_head = ret_head, * prev=nullptr;
				// 找到一个大于当前值的节点
				while (tmp_head && tmp_head->val < head->val)
				{
					prev = tmp_head;
					tmp_head = tmp_head->next;
				}
				unsorted_head = head->next;	// 保存下一个遍历无序链表的地址
				if(prev) {
					prev->next = head;
					head->next = tmp_head;
					head = unsorted_head;
					continue;
				}
				else {
					// 需要修改返回的头
					ret_head = head;
					head->next = tmp_head;
					head = unsorted_head;
					continue;
				}
			}
			return ret_head;
		}

		// https://leetcode.com/problems/sort-list/
		// 148. Sort List
		/* given a head of sorted list, return the list after sorting it in ascending order. 
		soulution1 : 参考147题，直接插入排序。 
		*/
		ListNode* sortList(ListNode* head) {
			if(!head || head->next == nullptr)
				return head;
			ListNode tmp_head, *cur=head, *order_node=head;
			tmp_head.next = head;
			while(cur) { 
				// 当前节点的值大于下一个节点的值. 把小的值 插入到有序链表里
				if(cur->next && cur->next->val < cur->val) {
					// 把下一个节点插入到有序链表
					// 退出条件是 当前节点
					while(order_node && (order_node->next && order_node->next->val < cur->next->val)) {
						order_node = order_node->next;
					}
				}
				else {
					cur = cur->next;
				}
			}
		}

		// https://leetcode.com/problems/remove-linked-list-elements/
		// 203. Remove Linked List Elements
		/*
			given a linked list and a integer val. remove nodes of the linked list that node.val == val. 
			solution: use a dumy head to store the original head of the linked list. 
			Runtime: 31 ms, faster than 49.70% of C++ online submissions for Remove Linked List Elements.
			Memory Usage: 15.3 MB, less than 18.85% of C++ online submissions for Remove Linked List Elements.
		*/
		ListNode* removeElements(ListNode* head, int val) {
			ListNode dumy, *prev;
			dumy.next = head;
			prev = &dumy;
			for(;head;head=head->next)
				if(head->val != val)
					prev=head;
				else
					prev->next = head->next;

			// solution 1:					
			// while(head) {
			// 	if(head->val == val) {
			// 		prev->next = head->next;
			// 		delete head;
			// 		head = prev->next;
			// 		continue;
			// 	}
			// 	// not equal, move forward to next
			// 	prev = head;
			// 	head = head->next;
			// }
			return dumy.next;

		}
		// https://leetcode.com/problems/odd-even-linked-list/
		// 328. Odd Even Linked List
		/*
		given the head of singly linked list, group all the nodes with odd indices together followed by the nodes with even indices. must O(1) space and O(N) time complexity.
		solution: 给一个计数器，当前指针，两个头指针，两个临时指针， 遍历原始链表，
		计数器为奇数时加入到 odd，为偶数时加入到 even 链表，最后拼接两个链表。
		Runtime: 8 ms, faster than 95.44% of C++ online submissions for Odd Even Linked List.
		Memory Usage: 10.4 MB, less than 75.98% of C++ online submissions for Odd Even Linked List.
		*/
		ListNode* oddEvenList(ListNode* head) {
			if(!head || !head->next)
				return head;
			ListNode head_odd , head_even ,
			*tmp_odd, *tmp_eve=nullptr;
			int i =1;
			tmp_odd = &head_odd;
			tmp_eve = &head_even;
			while (head)
			{
				if(i % 2 != 0) {
					// odd
					tmp_odd->next = head;
					tmp_odd = head;
				}
				else {
					// even
					tmp_eve->next = head;
					tmp_eve = head;
				}
				++i;
				head = head->next;
			}
			tmp_odd->next = head_even.next;
			tmp_eve->next = nullptr;
			return head_odd.next;
			
		}

		// https://leetcode.com/problems/linked-list-random-node/
		// 382. Linked List Random Node
		/*
			given a singly linked list, return a random node's value from it. Each node should have same probability of being chosen. Implement ths class.
			input : ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
			[[[1, 2, 3]]
			output: [null, 1, 3, 2, 2, 3]
			follow up: the list is extremely large and length is unknown. use O(1) space.
			solution: 
		*/
		class Solution {
		private:
			ListNode* m_head;
			long long m_index;
		public:
			Solution(ListNode* head) {
				// srand(reinterpret_cast<unsigned int>(head));
				srand(1);
				m_index = rand();
			}
			
			int getRandom() {
				if(!m_head)
					return 0;
				ListNode* tmp = m_head;
				int len = 0, cur = 0;
				while(tmp && cur != m_index) {
					tmp = tmp->next;
					if(!tmp && cur < m_index) {
						// overflow
						m_index = m_index % cur;
						tmp = m_head;
						cur = 0;
					}
				}
				m_index = rand();
				return tmp->val;
				
			}
		};


	};
	
	namespace randNode {
		class Node {
		public:
			int val;
			Node* next;
			Node* random;
			
			Node(int _val) {
				val = _val;
				next = NULL;
				random = NULL;
			}
		};
		#include<map>
		using std::map;
		Node* copyRandomList(Node* head) {
			if(!head)
				return nullptr;
			map<Node*, int> map_addr_id;	// 节点的地址和索引 map
			vector<Node*> addrs;
			Node* ret_head = nullptr, *tmp = nullptr, *prev = nullptr, *org_head=head;
			int i = 0;
			while(head) {
				map_addr_id[head] = i;
				tmp = new Node(head->val);
				if(!ret_head)
					ret_head = tmp;
				if(prev)
					prev->next = tmp;
				prev = tmp;
				addrs.push_back(tmp);
				++i;
				head = head->next;
			}
			// 修复random节点
			int n = 0;
			head = org_head;
			while(head) {
				// 
				if(head->random == nullptr) {
					// next
					head = head->next;
					++n;
					continue;
				}
				Node* cur = addrs[n];
				// 取出 head->random的索引，链接当前节点cur的random到对应索引
				int index = map_addr_id[head->random];
				cur->random = addrs[index];
				++n;
				head = head->next;
			}
			return ret_head;
		}
	};
		// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
		// 430. Flatten a Multilevel Doubly Linked List
		/*
		扁平化一个多层次的双向链表。 使得所有层都在同一层。 返回的链表的每个节点 child 都为 null
		solution: 循环扫描链表， 保存当前指针，下一个指针，遇到有child时，递归进入，遍历完毕一个没有
		child的链表，返回它的尾部指针.
		Input:
		[1,null,2,null,3,null]
		Output:
		[1,2]
		Expected:
		[1,2,3]
		Runtime: 3 ms, faster than 86.78% of C++ online submissions for Flatten a Multilevel Doubly Linked List.
		Memory Usage: 7.3 MB, less than 92.56% of C++ online submissions for Flatten a Multilevel Doubly Linked List.
		Runtime: 0 ms, faster than 100.00% of C++ online submissions for Flatten a Multilevel Doubly Linked List.
		Memory Usage: 7.5 MB, less than 20.34% of C++ online submissions for Flatten a Multilevel Doubly Linked List.
		*/
	namespace Node2{
		class Solution {
		public:
			class Node {
			public:
				int val;
				Node* prev;
				Node* next;
				Node* child;
			};
			// 递归的扁平化链表
			Node* recursive_flatten(Node* cur) {
				if(!cur)
					return nullptr;
				Node* cur_next, * tail = cur;
				while(cur) {
					cur_next = cur->next;
					if(cur->child) {
						// has next level
						tail = recursive_flatten(cur->child);
						cur->next = cur->child;	// 当前节点下一个节点改为 child
						cur->child->prev = cur; // child 节点的 prev 为当前节点
						tail->next = cur_next;	// 从 2 返回到 1 的时候， tail 指针不是指向3，而是 2，导致回到1，把节点3删除了
						if(cur_next)
							cur_next->prev = tail;
						cur->child = nullptr;
						// ----------------- > 关键点 < -----------------
						if(!cur_next)
							return tail;
					}
					// 如何找到正确的 tail 指针返回
					if(!cur_next)
						tail = cur;
					cur = cur_next;
				}
				return tail;
			}
			Node* flatten(Node* head) {
				// 0 ms 
				recursive_flatten(head);
				return head;
				// 3 ms
				// Node* tmp_head = head;
				// recursive_flatten(head);
				// return tmp_head;
			}
		};
	};
};
