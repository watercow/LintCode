#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		if (nums.size() < 3) return INT_MAX;
		sort(nums.begin(), nums.end());

		int res = 0, diff = INT_MAX;

		for (int i = 0; i < nums.size(); i++) {
			if (i > 0 && nums[i] == nums[i - 1])
				continue;
			int l = i + 1, r = nums.size() - 1;
			while (l < r) {
				int sum = nums[i] + nums[l] + nums[r];
				if (sum == target) return target;
				else if (sum > target) r--;
				else l++;
				if (diff > abs(sum - target)) {
					diff = abs(sum - target);
					res = sum;
				}
			}
		}
		return res;
	}
};

int main() {
	int nums[7] = { 1, 2, 3, 5, 4, 7, 6};
	vector<int> num(nums, nums + 7);
	cout << Solution().threeSumClosest(num, 5);
}

