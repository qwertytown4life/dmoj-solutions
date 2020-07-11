#include <bits/stdc++.h>

#define ll long long
using namespace std;

int N, M, start, End;
ll minutes;
vector<tuple<int, int, int>> graph[200003];

bool dijk(int begin, int end, int K, ll time) {
    vector<ll> dist (200003,LONG_LONG_MAX);
    deque<int> q;
    dist.at(begin) = 0;
    q.push_front(begin);
    int cur;
    int inq[200003];
    inq[begin] = 1;
    while (!q.empty()) {
        cur = q.front();
        q.pop_front();
        inq[cur] = 0;
        for (tuple<int, int, int> thing : graph[cur]) {
            if (get<0>(thing) <= K) {
                ll distance = dist[cur] + get<2>(thing);
                if (dist[get<1>(thing)] > distance) {
                    dist[get<1>(thing)] = distance;
                    if (!inq[get<1>(thing)]) {
                        q.push_back(get<1>(thing));
                        inq[get<1>(thing)] = 1;
                    }
                }
            }
        }

    }
    return dist[end] < time;
}


int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> N >> M;

    for (int i = 1; i <= M; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].emplace_back(i,b,w);
        graph[b].emplace_back(i,a,w);
    }
    cin >> start >> End >> minutes;

    int lo = 0, hi = M;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (dijk(start, End, mid, minutes)) {
            hi = mid - 1;
        }
        else (lo = mid + 1);
    }
    if (lo <= M) {
        cout << lo << '\n';
    }
    else (cout << "-1" << '\n');
    return 0;
}
