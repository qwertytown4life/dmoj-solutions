#include <bits/stdc++.h> //(DMOJ ONLY)
using namespace std;
int Q, N;

int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
    cin >> Q;
    for (int j = 0; j < Q; j++) {
        vector<int> branch;
        vector<int> cart;
        int next = 1;
        cin >> N;
        for (int i = 0; i < N; i++) {
            int a;
            cin >> a;
            cart.push_back(a);
        }

        bool isGood = true;
        while (next <= N and isGood) {
            
            if (!cart.empty() and cart.back() == next) {
                next += 1;
                cart.pop_back();
            } 
            else if (!branch.empty() and branch.back() == next) {
                next += 1;
                branch.pop_back();
            } 
            else if (!cart.empty()) {
                branch.push_back(cart.back());
                cart.pop_back();
            } 
            else {
                isGood = false;
            }
        }
        if (isGood) {
            cout << "Y" << '\n';
        } else {
            cout << "N" << '\n';
        }
    }
    return 0;
}
