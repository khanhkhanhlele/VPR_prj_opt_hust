#include<bits/stdc++.h>
using namespace std;
#define N 20
int n, K, Q;
int d[N];
int c[N][N];
bool visited[N];
int x[N], y[N];
int load[N];
int numSegments = 0;
int cMin = INT_MAX;
int f = 0;
int f_min = 1e9;

void solution()
{
    if (f < f_min) f_min = f;
}

bool checkX(int v, int i, int k)
{
    if(v == 0) return true;
    if(load[k] + d[v] > Q || visited[v]) return false;
    return true;
}

bool checkY(int i, int k)
{
    return d[i] <= Q;
}

void TryX(int i, int k)
{
    if (f + (n + K - numSegments) * cMin > f_min) return;
    for(int v = 0; v <= n; v++)
    {
        if(checkX(v, i, k))
        {
            x[i] = v;
            load[k] += d[v];
            numSegments++;
            visited[v] = true;
            f += c[i][v];
            if(v == 0){
                if(k == K){
                    if (numSegments == n + K) solution();
                } 
                else{
                    TryX(y[k + 1], k + 1);  
                }
            }
            else{
                TryX(v, k);
            }
            load[k] -= d[v];
            numSegments--;
            visited[v] = false;
            f -= c[i][v];
        }
    }  
}

void TryY(int k)
{
    for(int i = y[k - 1] + 1; i <= n - K + k; i++)
    {
        if (checkY(i, k))
        {
            y[k] = i;
            visited[i] = true;
            load[k] += d[i];
            numSegments++;
            f += c[0][i];
            if(k == K){
                TryX(y[1], 1);
            }
            else{
                TryY(k + 1);
            }
            visited[i] = false;
            load[k] -= d[i];
            numSegments--;
            f -= c[0][i];
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> K >> Q;
    for(int i = 1; i <= n; i++)
        cin >> d[i];
    for(int i = 0; i <= n; i++)
        for(int j = 0; j <= n; j++)
        {
            cin >> c[i][j];
            if(i != j && c[i][j] < cMin) cMin = c[i][j];
        }
    fill(visited, visited + n + 1, false);
    fill(load, load + K + 1, 0);
    y[0] = 0;
    TryY(1);
    cout << f_min;
}