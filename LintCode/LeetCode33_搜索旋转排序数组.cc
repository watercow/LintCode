class Solution {
public:
	int search(vector<int>& nums, int target) {
		int left = 0, right = nums.size() - 1;
		while (left <= right) {
			int mid = left + (right - left) / 2;

			if (nums[mid] == target) return mid;

			if (nums[mid] < nums[right]) { // 判断条件表示该区间是单调增
				if (target <= nums[right] && target > nums[mid])
					left = mid + 1;
				else right = mid - 1;
			}
			else { //该区间不是单调增
				if (target < nums[mid] && target >= nums[left])
					right = mid - 1;
				else left = mid + 1;
			}
		}
		return -1;
	}
};
