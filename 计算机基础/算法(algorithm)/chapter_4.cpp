#include <iostream>
#include <algorithm>
#define abs(x) (x)<0 ? -(x):(x) //talk is cheap, show me the code~
#define INF 99999 //dmin的初始化

using namespace std;

int MinDif(int a[], int n)
{
	int dmin = INF;
	for(int i = 0; i <= n-2; i++)
	{
		for(int j = i+1; j <= n-1; j++) //从想比较第一个元素后开始进行比较
		{
			int tmp = abs(a[i] - a[j]);
			if(tmp < dmin)
				dmin = tmp;
//			cout << tmp << endl ;
		}
	}
	return dmin;
}
//改进后的算法时间复杂度为O（nlogn) [即sort函数的时间复杂度]
int Optimize(int a[], int n)
{
	sort(a, a+n);	//由小到大升序
	int dmin = a[1] - a[0];
	for(int i = 2; i <= n-1; i++)
	{
		int tmp = a[i] - a[i-1];
		if(tmp  < dmin)
			dmin = tmp; //距离更新
	}
	return dmin;
}
int factor1(int n) //求 n!
{
	int f = 1;
	for(int i = 2; i <= n; i++)
		f = f * i;
	return f;
}
int f2(int n) //枚举法求 1！+2！+ ··· + n!
{
	int sum = 0; //初始化！！
	for(int i = 1; i <= n; i++)
		sum += factor1(i);
	return sum;
}
int f_Optimize(int n) //优化版(记忆化搜索) -> 省去很多计算量
{
	int sum = 0;
	int fn = 1;
	for(int i = 1; i <= n; i++)
	{
		fn = fn * i;	
		sum += fn;
	}
	return sum;
}

void ChickenAndRabbit()
{
	int n, m, cFeet, rFeet;
	for(int i = 1; i <= 5; i++)
		for(int j = 0; j <= 5; j++)
			for(int k = 0; k <= 5; k++)
	{
		cFeet = i*100 + j*10 + k;
		if(cFeet % 2 ==0) //是否能被二整除判断！！[条件]
			n = cFeet / 2;
		else
			continue;	
		m = n; //只数相等
		if(((m*4)/100>=0 && (m*4)/100<=5) && ((m*4)/10%10>=0 && (m*4)/10%10<=5) &&((m*4)%10>=0 && (m*4)%10<=5)) //保证各位数字在题干要求的区间内
			rFeet = m*4;
		else
			continue;
		printf("chicken:%d, rabbit:%d, cF:%d, rF:%d\n", n, m, cFeet, rFeet);
	}
}

void ThreeDigit()
{
	for(int i = 1; i <= 5; i++)
		for(int j = 0; j <= 5; j++)
			for(int k = 0; k <= 5; k++)
	{
		if(k>i && i>j && i+j+k==i*j*k)
			printf("%d%d%d", i, j, k);
	}
}

char map[100][100];
int MaxArea(int n)
{
	int  maxArea = 0;
	for(int j = 0; j < n; j++) //对第j列进行遍历(按列处理数组)
	{	
		int cnt = 1 ; //遍历到j列，重新对cnt初始化
		for(int i = 1; i < n; i++) //从第二个开始比较即可
		{
			if(map[i][j] == 0) //当空字符时 停止遍历（未被赋字符）
				break;
			if(map[i][j] == map[i-1][j])
				cnt++;
			else
				cnt = 1; //重新开始计数
//			cout << cnt << endl;		
			if(cnt > maxArea)
				{	
					//			cout << cnt << endl;
					maxArea = cnt;
				}
			
		}
	}
	return maxArea;
}
//测试用例：6---###  7####--- 8------&&
int main(int argc, char *argv[]) {
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) //接收数组只有一列（简单～）
	{
		scanf("%c", map[i]); 
//		printf("%s", map[i]);
	}	
	printf("%d\n",  MaxArea(n));
}
