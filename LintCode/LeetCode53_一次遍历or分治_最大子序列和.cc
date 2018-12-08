//O(n)
class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		int res = INT_MIN, sub_sum = 0;
		for (int &x : nums) {
			sub_sum = max(sub_sum + x, x);
			res = max(sub_sum, res);
		}
		return res;
	}
};

//分治O(NlogN)
class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		if (nums.size() == 0) {
			return 0;
		}
		return maxSubArrar(nums, 0, nums.size() - 1);
	}

	int maxSubArrar(vector<int>& nums, int left, int right) {
		if (left == right) {
			return nums[left];
		}

		int mid = (right + left) / 2;
		int leftmax = maxSubArrar(nums, left, mid);
		int rightmax = maxSubArrar(nums, mid + 1, right);

		//考虑跨mid的情况
		int lsub = INT_MIN, rsub = INT_MIN, sum = 0;
		for (int i = mid; i >= left; i--) {
			sum += nums[i];
			lsub = max(sum, lsub);
		}
		sum = 0;
		for (int i = mid + 1; i <= right; i++) {
			sum += nums[i];
			rsub = max(sum, rsub);
		}

		return max(lsub + rsub, max(leftmax, rightmax));
	}
};
