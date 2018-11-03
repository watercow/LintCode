#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

/*
利用快速排序partition函数的作用，
找到某次partition时访问的元素是否为整个序列的第k个元素
*/

class Solution {
public:
	int findKthLargest(vector<int>& nums, int k) {
		int left = 0, right = nums.size() - 1;

		return __findKthLargest(nums, left, right, k);
	}

	int __findKthLargest(vector<int>& nums, int left, int right, int k) {
		
		int index = __partition(nums, left, right);
		if (index == (k - 1)) {
			return nums[index];
		}
		else if (index > k - 1) {
			return __findKthLargest(nums, left, index - 1, k);
		}
		else {
			return __findKthLargest(nums, index + 1, right, k);
		}
	}

	int __partition(vector<int>& nums, int left, int right) {
		//返回当前访问元素排序后的index值
		int v = nums[left];

		// nums[l+1,...j] < v; nums[j+1,...,i) > v
		int j = left;
		for (int i = j + 1; i <= right; i++) {
			if (nums[i] > v) {
				swap(nums[++j], nums[i]);
			}
		}

		swap(nums[left], nums[j]);
		return j;
	}
};

