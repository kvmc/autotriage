#include <iostream>

using namespace std;

int test = 100;

int main(int argc, char ** arg) {
	cout << "Hello, World!" << endl;

	cout << test << endl;

	int* a = new int[10];

	for (int i = 0; i < 10; i++) {
		a[i] = i;
	}

	size_t len = sizeof(a) / sizeof(a[0]);

	for (int i = 0 ; i < len ; i++) {
		cout << a[i] << endl;
	}


}


