#include "pch.h"
#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

class Solution {
public:
	int reverse(int x) {
		long n = abs(long(x));
		long res = 0;
		
		while (n != 0) {
			res = res * 10 + n % 10;
			n /= 10;
		}

		if (x > 0 and res > INT_MAX) return 0;
		if (x < 0 and -res < INT_MIN) return 0;

		return (x > 0 ? res : -res);
	}
};

int main()
{
	cout << Solution().reverse(321);
}
