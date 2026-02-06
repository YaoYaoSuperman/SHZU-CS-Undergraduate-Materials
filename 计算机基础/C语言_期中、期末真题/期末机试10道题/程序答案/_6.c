#include <stdio.h>

int main(int argc, char *argv[]) {
	int n;
	scanf("%d", &n);
	
	double zi = 2, mu = 1, sum = 0; //初始化分子 分母
	for(int i = 1; i <= n; i++)
	{
		sum += zi / mu;
		double t = mu;
		mu = zi;
		zi = zi + t;
	}
	sum = sum - (int) sum ;
	printf("%.3lf", sum);
	
	return 0;
}