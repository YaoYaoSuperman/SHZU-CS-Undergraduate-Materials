#include <stdio.h>

#define rep(i, a, b) for(int i = a; i < b; i++)
	
typedef struct student{
	int no;
	char name[20];
	int score;
} stu;

/*
5
10101 Zhang 78
10103 Wang 98
10106 Li 86
10108 Ling 73
10110 Sun 100
*/
int main(int argc, char *argv[]) {
	int n; 
	scanf("%d", &n);
	
	stu stus[n];
	
	rep(i, 0, n)
	{
		int no, score;
		char name[20];
		scanf("%d%s%d", &stus[i].no, stus[i].name, &stus[i].score);
	}
	
	for(int i = 0; i < n - 1; i++) //每次冒泡的边界
	{
		for(int j = n - 1 ;j >= i + 1; j--) //每次冒泡操作 [i + 1， 9] 的区间
		{
			if(stus[j].score > stus[j - 1].score)
				{
					stu t = stus[j];
					stus[j] = stus[j - 1];
					stus[j - 1] = t;
				}
		}
	}
	
	rep(i, 0, n)
		printf("%d %s %d\n", stus[i].no, stus[i].name, stus[i].score);
	
	return 0;
}