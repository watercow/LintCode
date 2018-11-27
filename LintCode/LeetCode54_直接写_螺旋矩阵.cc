class Solution {
public:
	vector<int> spiralOrder(vector<vector<int>>& matrix) {
		vector<int> res;
		if (matrix.size() == 0) return res;
		if (matrix[0].size() == 0) return res;
		int m = matrix.size(), n = matrix[0].size();

		int top = 0, right = n - 1, left = 0, bottom = m - 1;

		while (true) {
			//从左往右
			for (int i = left; i <= right; i++) {
				res.push_back(matrix[top][i]);
			}
			if (++top > bottom) break;

			//从上往下
			for (int i = top; i <= bottom; i++) {
				res.push_back(matrix[i][right]);
			}
			if (--right < left) break;

			//从右往左
			for (int i = right; i >= left; i--) {
				res.push_back(matrix[bottom][i]);
			}
			if (--bottom < top) break;

			//从下往上
			for (int i = bottom; i >= top; i--) {
				res.push_back(matrix[i][left]);
			}
			if (++left > right) break;
		}
		return res;
	}
};
