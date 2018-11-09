using namespace std;

//全排列问题使用DFS标记是否出现过
//推荐博客: https://blog.csdn.net/feengzhk/article/details/70226682
 
class Solution {
public:
	vector<vector<int>> permute(vector<int>& nums) {
		vector<vector<int>> res;
		dfs(nums, 0, res);
		return res;
	}

	void dfs(vector<int>& nums, int cur, vector<vector<int>>& res) {
		if (cur == nums.size()) {
			res.push_back(nums);
			return;
		}
		for (int i = cur; i < nums.size(); i++) {
			swap(nums[i], nums[cur]);
			dfs(nums, cur + 1, res);
			swap(nums[i], nums[cur]);
		}
	}
};
