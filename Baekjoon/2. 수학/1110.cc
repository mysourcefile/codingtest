#include <iostream>
using namespace std;

int main()
{
	int N,A,B,C,i=0;
    cin >> N;
    int M = N;
    while(1){
        A = M/10; //10의 자리 수
        B = M%10; // 1의 자리 수
        C = (A+B)%10; // 둘을 더한 후 일의 자리 수
        M = 10*B + C; 
        i++;  // 새로운 수 구축 후 카운터 증가
        if(N == M){ // 입력받은 수와 새로 구축한 수 비교
            cout << i; 
            break;
        }
    }
}