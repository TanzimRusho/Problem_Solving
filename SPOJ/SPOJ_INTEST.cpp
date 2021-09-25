#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, k, num;
    int count = 0;
    
    cin >> n >> k;
    
    while(n--)
    {
        cin >> num;
        
        if (num % k == 0)
            ++count;
    }
    
    cout << count << '\n';
    
    return 0;
}
