#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int cnt = 99;
    
    if(N <= 99)
    {
        cout << N << endl;
    }
    
    
    else
    {
        for(int i = 100; i <= N; i++)
        {
            string str = to_string(i);
            if((str[0] - str[1]) == (str[1] - str[2]))
            {
                cnt++;
            }
            
            else
            {
                continue;
            }
         }
        cout << cnt << endl;
    }
    return 0;
}

