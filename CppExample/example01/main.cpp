#include <iostream>

using namespace std;

template <class T>
inline int compare(T x, T y) {
	if (x < y) return -1;
	else if (x == y) return 0;
	else return 1;
}

int main (){
	cout << compare(3, 7) << endl;
	cout << compare("cloud", "route") << endl;
	cout << compare(24.5, 23.5) << endl;
}

