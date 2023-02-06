#include <iostream>
#include <string>
using namespace std;

int main() 
{
	int n,b,i;
	
	cin >> n;
	int a[n];
	double d[n],avg=0;
	for(i=0;i<n;i++)
	{
		cin >> b;
		a[i] = b;
		d[i] = b;
		
		if(d[i-1] > d[i]) d[i] = d[i-1]; 
	}
	
	for(i=0;i<n;i++)
	{
		avg = avg + (a[i]/d[n-1]*100);
	}
	cout << avg/n;
}