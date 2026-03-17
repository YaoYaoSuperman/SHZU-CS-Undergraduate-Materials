#include <stdio.h>

int dic[10]; //存储0 - 9 数字出现的次数

int main(int argc, char *argv[]) {
	
	int a;
	scanf("%d", &a);

	while(a)
	{
		int t = a % 10; // a当前最后一位的位数
		dic[t]++;
		a /= 10;
	}
	int cnt = 0; //统计0-9数字中出现2次的次数
	for(int i = 0; i <= 9; i++)
		if(dic[i] == 2)
			cnt++;
		
	if(cnt == 1) 
		printf("1");
	else
		printf("0");
	
	return 0;
}