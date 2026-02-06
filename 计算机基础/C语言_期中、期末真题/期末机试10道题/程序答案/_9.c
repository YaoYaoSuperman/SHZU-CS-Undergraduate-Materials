#include <stdio.h>

#define rep(i, a, b) for(int i = a;i < b; i++)

const int N = 110;
int a[N][N];

/*
3 4
1 2 3 4
9 8 7 6
2 0 5 8
*/
int main(int argc, char *argv[]) {
	int n, m;
	scanf("%d%d", &n, &m);
	
	rep(i, 1, n + 1)
		rep(j, 1, m + 1)
			scanf("%d", &a[i][j]);
	
	int max = a[1][1], row = 1, col = 1; //初始化参数
	rep(i, 1, n + 1)
		rep(j, 1, m + 1)
		{
			if(a[i][j] > max)
			{
				max = a[i][j];
				row = i;
				col = j;
			}
	    }
	
	printf("%d %d %d", max, row, col);
	return 0;
}