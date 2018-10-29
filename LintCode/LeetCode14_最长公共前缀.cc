#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0) return "";
		if (strs.size() == 1) return strs[0];

		int col = 0;
		string res = "";

		while (1) {
			if (col >= strs[0].size()) return res;
			char ch = strs[0][col];
			for (int row = 1; row < strs.size(); row++) {
				if (col >= strs[row].size() || strs[row][col] != ch)
					return res;
			}
			col++;
			res += ch;
		}
	}
};
