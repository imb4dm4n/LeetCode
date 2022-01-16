# README

## purpose

- This repository is for practice only.



## 4 两个有序数组的中位数

- 问题分析：先合并两个数组， 需要找到他们的边界。
- 思路：
  - 合并数组a，b：
    - 情况 a 所有的值都小于 b
      - 顺序合并 a，b
    - a所有的值都大于b
      - 合并b，a
    - a的最大值大于b的最小值，但是 小于b的最大值
      - [  aaaa [bbb  ]aaabbb   ]
      - 找到a中
  - 用两个整数id_a, id_b，分别记录当前正在读取的数组的偏移。 当他们是中位数偏移时， break。
  - 先计算两个数组总过有多少数字count， 判定中位数的偏移是奇数，还是偶数（两数之和除以二）
    - 基数：
      - 中位数偏移 count/2 + 1
      - 
    - 偶数：
      - 中位数偏移 count/2，count/2 + 1

## 最长回文

- 原理：
  	对称的字符串有的特性：
  以中轴字符起，左右两个字符都相同。 相同意味着用 xor 得到0 。
  进一步加速，可以把字符转为 short 、 int 、 long long 数字进行对比。

- 无非就是想确定， 对称发生的字符的偏移量a， 对称结束的字符偏移量b，  b -a 得到对称长度，构造字符串，从b开始 2*(b-a) 长。
  
- 剩下的就是去探测，哪里开始不对称。 从最优情况，就是最中间开始， 假设整个字符串是对称的，因此在最远处的两个字符应该是相同的， 若不是，则对称字符长度减一。 
  
  
  
- 实现：
  字符串长度 n
  需要记录最长子串长， 因为每个中轴索引，都有 n/2 种可能的长度。
  或者不这样， 从长到短去寻找， 意思是遍历所有对称串可能长度的子串，如果没有发现，
  则减少对称串的长度。 

- 先从字符串最中间开始找，如果左右都相同，则找到，如果不是对称的，则设置 offset 
  
- 需要3个索引： 中轴索引，根据中轴推出左右两个子串的每个字符索引。 中轴索引都会有相应的
  对称点，因此需要生成两次。
  一个对称长度，记录对称串的长度

  子串生成 -》 对称判断函数

  最后根据中轴索引和对称串长度，得到 对称串起始地址和结束地址。

###  判断字符串是否对称

#### 栈

- 如果字符串对称， 那么在中间点之前入栈， 中间点之后出栈时，字符是相同的。

  - ~~~
    abcdcba
    a-b-c-d 出栈 d - c - b - a
    ~~~

  - 



## 链表

### swap nodes pair

- https://leetcode.com/problems/swap-nodes-in-pairs

- 思路：
  - 核心思想是修改当前节点的 next 和 下一个节点的 next。
  - 需要修复前一对节点的后一个节点的 next 为 交换后的新的当前节点。
    - 如1-2-3-4  第一次交换 2-1-3-4 。 下一步交换 3-4得到 （2-1）（4-3），但是 1 的next指针是3，因此需要修复1的next为4 。

### rotate list

- https://leetcode.com/problems/rotate-list/
- 循环移位链表k次。 类似 汇编指令的 ror ，不同的是数据不同而已。
- 思路：
  - 核心问题： 新的头节点、 移位的节点位置，它的前节点 next 修改， 移位的后半段链表最后一个节点的next修改。
  - 通过指针数组快速做一次O（n）的遍历即可。

## 链表

### 删除重复1

- 移除有序链表中存在重复的数字。可以保留一个。
- https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

- 思路：
  - 用两个指针，一个是当前指针，一个是next，如果值相同，则移动 next。 如果不同，则同时移动 当前指针 和 next 。



### 删除重复2

- 移除有序链表中所有重复的数字。 

- https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

- 思路：

  - 用栈的方法做。假设输入： `1, 2, 2, 3, 3, 4`

    - ~~~
      [1,2,2,3,3,4]
      初始化，入栈一个节点，一个指针指向当前工作节点 cur ，一个栈顶指针 top
      [1]
      
      准备入栈2，对比是否相同，相同则标记 has_dup， 不同则直接入栈
      [1,2]
      
      准备入栈2…… 存在相同，标记 has_dup=True， 修改栈顶的 next 为当前工作节点的next
      [1,2]
      
      准备入栈3，对比是否相同，并判断是否有重复，有重复则出栈，且修改新的栈顶的next
      [1,3]	// 2 出栈，同时修改 1 的 next为当前工作节点 cur 
      
      准备入栈3，对比是否相同，相同则标记 has_dup
      [1,3]
      
      准备入栈4…… has_dup = True
      [1,4]
      
      结束，返回栈底
      
      ~~~

    - 

### 分区 partition

- 把小于等于 n 的节点移动到 大于 n的节点的左边， 需要保持节点间原始顺序关系。



- 输入输出：

  - ~~~
    [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    
    ~~~

  - 

- 思路：

  - O(n ^ 2)。类似冒泡排序。 只是相关条件不同。 

  - 冒泡排序从头开始， 把最大值（最小值），送到最后一个位置。 

  - 这题是反过来，从尾部开始，把小于 x 的数往前推。

  - ~~~
    input： [1,4,3,2,5,2], x = 3
    
    prev =nul, cur =1, 
    prev=1, cur=4
    if prev > cur  and prev >= 3 and cur != 3
    	exchange prev and cur 
    else
    	prev = cur
    	cur = cur->next
    
    [1,4,2,3,5,2]
    
    [1,4,2,3,2,5]
    
    [1,2,4,3,2,5]
    
    [1,2,4,2,3,5]
    
    [1,2,2,4,3,5]
    
    ~~~

  - 

#### 答案

- 把链表数字中小于x的放前面， 大于等于的放后面。 实际上就是   [small]  [great] 分组。
- 通过建立两个链表，把小的放 small，大的放 great， 然后连接一下就行了 …… O(n) 复杂度。

- 注意最后一个 当前大节点的 next要设置为null， 否则可能产生无限循环链表。 比如x=3， 输入【1，5，2】

### 反转链表

- https://leetcode.com/problems/reverse-linked-list-ii/
- reverse nodes from  m-th to n-th (m,n). 
- thought：
  - set  `(m-1)->next = n` , set `m->next = n->next` , set` n->next = m`
  - edge condition: m >= n , do nothing
- solution:
  - easy: store all nodes in an array， exchange  `tmp = (left-1)->next` with right, right->next = left->next

## 树

### 唯一搜索树

- https://leetcode.com/problems/unique-binary-search-trees-ii/

- given an integer n， return all the structurally unique BST，which has exactly n nodes of unique values from 1 to n。
- 



### 树的深度

- https://leetcode.com/problems/maximum-depth-of-binary-tree/
- calculate the depth of the tree。
- deep first traverse the tree。
- 搜索到达所有叶子节点的值， 获取最大的那个。 