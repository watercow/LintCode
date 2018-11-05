using namespace std;

// 题中重要条件是“除了某个元素只出现一次以外，其余每个元素均出现两次”
// 注意是均出现两次，利用异或操作。
// 异或的性质1：交换律a ^ b = b ^ a，性质2：0 ^ a = a。于是利用交换律可以将数组假想成相同元素全部相邻，于是将所有元素依次做异或操作，相同元素异或为0，
// 最终剩下的元素就为Single Number

class Solution {
public:
	int singleNumber(vector<int>& nums) {
		int res = 0;
		for (int n : nums) {
			res ^= n;
		}
		return res;
	}
};
