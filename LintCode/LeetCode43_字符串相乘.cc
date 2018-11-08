class Solution {
public:
	string multiply(string num1, string num2) {
		if (num1 == "0" || num2 == "0") return "0";
		int num1_len = num1.length(), num2_len = num2.length();

		vector<int> product(num1_len + num2_len, 0);

		for (int i = num1_len - 1; i >= 0; i--) {
			for (int j = num2_len - 1; j >= 0; j--) {
				product[i + j + 1] += (num1[i] - '0') * (num2[j] - '0'); //注意 i+j要加1 ！
			}
		}

		int carry = 0;
		for (int i = num1_len + num2_len - 1; i > 0; i--) {//注意 i是大于0 因为算上最后一位如果要进位
			int tmp = (product[i] + carry) % 10;
			carry = (product[i] + carry) / 10;
			product[i] = tmp;
		}
		if (carry) product[0] = carry; //最高位的进位

		string res = "";
		for (auto n : product) res += to_string(n);
		if (res[0] == '0') res.erase(res.begin());

		return res;
	}
};
