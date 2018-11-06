/*
双指针，一前一后
*/
using namespace std;
 
 class Solution {
 public:
	 int removeDuplicates(vector<int>& nums) { //注意：输入是个引用
		 if (nums.size() < 2) return nums.size();
		 int res = 1;
		 for (auto &c : nums) {
			 if (c != nums[res - 1]) {
				 nums[res++] = c;
			 }
		 }
		 return res;
	 }
 };
