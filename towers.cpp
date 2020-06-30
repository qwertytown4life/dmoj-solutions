#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
    int N;
    cin >> N;
    int array[N];
    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }
    int goodCount = 0;
    for (int i = 1; i < N - 1; i++) {
        if (array[i] > array[i - 1] and array[i] < array[i + 1]) {
            goodCount++;
        }
    }
    cout << goodCount << endl;
    return 0;
}
