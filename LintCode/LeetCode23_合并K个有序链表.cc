#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

/*
思路为首先实现一个合并两个有序链表的函数__mergeListNode;
之后两两遍历lists中链表进行合并，使用push_back将合并结果推入lists中
*/
using namespace std;

 struct ListNode {
	 int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		if (lists.size() == 0) return nullptr;
		if (lists.size() == 1) return lists[0];
		while (lists.size() > 1) {
			ListNode* p1 = lists[0], *p2 = lists[1];
			lists.erase(lists.begin());
			lists.erase(lists.begin());
			lists.push_back(__mergeListNode(p1, p2));
		}
		return lists[0];
	}

	ListNode* __mergeListNode(ListNode* l1, ListNode* l2) {
		if (!l1 || !l2) return l1 ? l1 : l2;

		ListNode* res = new ListNode(-1);
		ListNode* p1 = l1, *p2 = l2, *p = res;
		while (p1 && p2) {
			if (p1->val < p2->val) {
				p->next = p1;
				p1 = p1->next;
			}
			else {
				p->next = p2;
				p2 = p2->next;
			}

			p = p->next;
		}
		p->next = p1 ? p1 : p2;

		return res->next;
	}
};
