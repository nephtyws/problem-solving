/* from acmicpc.net, solved on 2015 */


#include <iostream>

using namespace std;

int main() {
 int n;
 cin >> n;

 for (int i = 0; i < n; i++) {
  for (int j = 0; j < n - 1 - i; j++) {
   cout << " ";
  }

  for (int e = 0; e < 2*i+1; e++) {
    cout << "*";
  }

  cout << endl;
 }
 
 return 0;
}
