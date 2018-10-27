#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

class Solution {
public:
	int myAtoi(string str) {
		int len = str.length();
		int i = 0;
		for (; i < len && str[i] == ' '; i++) continue;
		if (i == len) return 0;
		if (!isdigit(str[i]) && str[i] != '+' && str[i] != '-') return 0;
		int minus_flag = (str[i] == '-' ? -1 : 1);
		if (str[i] == '+' || str[i] == '-') i++;
		long res = 0;
		for (; i < len && isdigit(str[i]); i++) {
			res = 10 * res + str[i] - '0';
			if (minus_flag == 1 && res > INT_MAX) return INT_MAX;
			if (minus_flag == -1 && -res < INT_MIN) return INT_MIN;
		}

		return res * minus_flag;
	}
};

int main()
{
	cout << Solution().myAtoi("-321");
}


