#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
	bool isValid(string s) {
		stack<char> st;
		for (char &c : s) {
			if (c == '(' || c == '[' || c == '{')
				st.push(c);
			if (c == ')')
				if (st.empty() || st.top() != '(')
					return false;
				else st.pop();
			if (c == ']')
				if (st.empty() || st.top() != '[')
					return false;
				else st.pop();
			if (c == '}')
				if (st.empty() || st.top() != '{')
					return false;
				else st.pop();
		}
		return st.empty();
	}
};

int main()
{
	cout << Solution().isValid("[[])");
    return 0;
}
