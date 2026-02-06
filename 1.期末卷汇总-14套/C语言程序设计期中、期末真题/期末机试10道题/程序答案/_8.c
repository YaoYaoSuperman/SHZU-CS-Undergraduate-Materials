#include <stdio.h>

//10 9 8 7 6 5 4 3 2 1
int main(int argc, char *argv[]) {
	int a[10];
	for(int i = 0; i < 10; i++)
		scanf("%d", &a[i]);

	for(int i = 0; i < 9; i++) //每次冒泡的边界
	{
		for(int j = 9 ;j >= i + 1; j--) //每次冒泡操作 [i + 1， 9] 的区间
		{
			if(a[j] < a[j - 1])
			{
				int t = a[j];
				a[j] = a[j - 1];
				a[j - 1] = t;
			}
		}
	}
	
	for(int i = 0; i < 10; i++)
		printf("%d ", a[i]);

	return 0;
}