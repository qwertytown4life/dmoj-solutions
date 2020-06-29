#include <bits/stdc++.h> //(DMOJ ONLY)
using namespace std;

int a[105], b[105];

int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

    int type, N, sum = 0;
    cin >> type;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < N; i++) {
        cin >> b[i];
    }

    sort(a,a+N);
    sort(b,b+N);

    if (type == 2) {
        reverse(b, b + N);
    }

    for (int i = 0; i < N; i++) {
        sum += max(a[i],b[i]);
    }

    cout << sum << '\n';
    return 0;
}
