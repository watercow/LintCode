#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

// 直接从最后一位遍历生成新的结果，比较两个数是否相同

class Solution {
public:
	bool isPalindrome(int x) {
		if (x < 0) return false;
		long num = long(x);
		long temp = 0;
		while (num) {
			temp = temp * 10 + num % 10;
			num /= 10;
		}
		return temp == long(x);
	}
};
