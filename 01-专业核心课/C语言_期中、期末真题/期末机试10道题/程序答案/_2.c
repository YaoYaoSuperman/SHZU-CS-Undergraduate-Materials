#include <stdio.h>
#include<string.h>

const int N = 100010;
char s[N];

int main(int argc, char *argv[]) {
	scanf("%s", s);
	int n = strlen(s); //获取字符串的长度
	
	for(int i = 0; i < n; i++)
		if(s[i] == '*')
			continue;
		else 
			printf("%c", s[i]);
	
	return 0;
}