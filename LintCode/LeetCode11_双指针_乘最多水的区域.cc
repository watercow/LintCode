#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

// 不需要双指针从同一方向走，这样时间复杂度高
// 两个指针从两端向中间走

class Solution {
public:
	int maxArea(vector<int>& height) {
		int max_res = 0, h;
		int left = 0, right = height.size() - 1;
		while (left < right) {
			h = min(height[left], height[right]);
			max_res = max(max_res, h * (right - left));

			if (height[left] < height[right]) left++;
			else right--;
		}
		return max_res;
	}
};

int main()
{
	cout << Solution().maxArea(vector<int>([1, 2, 3, 4, 5]));
}
