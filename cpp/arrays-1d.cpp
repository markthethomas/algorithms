#include <iostream>

using namespace std;

int main()
{
    int n;

    // read the int
    cin >> n;

    // create new array w/ size n
    int array[n];

    // add to array
    for	(int i = 0; i < n; i++) {
    	int o;
    	cin >> o;
    	array[i] = o;
    }
    // needs to n-1 bc it's the size of the array and
    // i will be used as an index
    for (int i = n - 1; i >= 0; i--) {
    	cout << array[i] << endl;
    }
    return 0;
}
