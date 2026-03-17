#include <stdio.h>

int main(int argc, char *argv[]) {
	int min = 2147483647; //定义成int的最大值
	for(int i = 1;i <= 10; i++)
	{
		int x; 
		scanf("%d", & x);
		if(x < min)
			min = x;
	}
	printf("%d", min);
	
	return 0;
}