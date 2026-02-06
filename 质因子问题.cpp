#include <iostream>
#include <cstring>
#include <unordered_map>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long LL;

const int N = 5e4 + 10;
int a[N];
int cnt = 0;
int primes[N];
bool vis[N];
unordered_map<int, int> p; //存储质因子及其出现的次数


//https://codeforces.com/contest/1771/problem/C
void getPrimes(int n) //线性筛质数O(N)
{
	for(int i = 2; i <= n; i++)
	{
		if(!vis[i]) primes[cnt ++] = i, p.emplace(i, 0);
		for(int j = 0; primes[j] <= n / i; j++)
		{
			vis[primes[j] * i] = 1;
			if(i % primes[j] == 0) //遇到最小质因子，停止循环，保证只遍历一遍
				break;
		}
	}
}	


/*
2
3
32 48 7
3
14 5 9
*/
int main(int argc, char *argv[]) {
	int t; cin >> t;
	
	getPrimes(N - 10); //1e7以内的质数
	while(t -- )
	{
		int n; cin >> n;
		
		for(int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		
		bool flag = 0;
		vector<int> nums;
		for(int i = 1; i <= n; i++) //遍历数组，对于每个数字分解质因子
		{
			int t = a[i];
			for(int j = 2; j <= t / j; j++)
			{
				if(t % j == 0) //j是我们的最小质因子
				{
					p[j]++;  //注意:最小质因子是 "j"
					nums.push_back(j); //操作过的最小质因子，记录状态以备还原
					if(p[j] >= 2) //出现了重复质因子，直接结束
					{
						flag = 1;
						break;
					}	
					while(t % j == 0)
						t /= j;
				}
			}
          	if(flag)
              break;
			if(t > 1) 
			{
				//剩余一个比sqrt(t)大的最小质因子
				p[t]++; 
				nums.push_back(t);
				if(p[t] >= 2)
				{
					flag = 1;
					break;
				}	
			}
		}
		if(!flag)
			printf("NO\n");
      	else
          	printf("YES\n");
		for(auto x: nums)
			p[x] = 0;
//		cout << p[3] << " " << p[2] << p[5] << endl; 
	}
	
	return 0;
}