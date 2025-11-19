#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    cin >> a >> b;
    
    cout << a.size() << " " << b.size() << endl;
    
    cout << a + b << endl;
    
    // swap character is quite challenging for me since this is my first time doing it using cpp. but it actually still worked with the classic one :p
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;
    
    cout << a << " " << b << endl;
    

    return 0;
}