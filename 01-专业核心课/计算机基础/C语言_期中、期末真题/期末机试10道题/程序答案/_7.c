#include <stdio.h>
#include <math.h>

_Bool isPrime(int n)
{
	if(n == 1) return 0;
	for(int i = 2; i <= sqrt(n); i++)
	{
		if(n % i == 0)
			return 0;
	}
	return 1;
}

int main(int argc, char *argv[]) {
	
	int sum = 0;
	for(int i = 1; i <= 100; i ++)
		if(isPrime(i))
			sum += i;
		
	printf("%d", sum);
	
	return 0;
}