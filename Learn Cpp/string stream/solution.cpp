#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    vector<int> result;
    string temp;
    
    for (char c : str) {
        if (c != ',') {
            temp += c;
        } else {
            int num = stoi(temp);
            result.push_back(num);
            temp.erase();
        }
    }
    int num = stoi(temp);
    result.push_back(num);
    
    return  result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
