 #include <stdio.h>

const int N = 10;
double a[N];

int main(int argc, char *argv[]) {
	
	for(int i = 1; i <= 7; i++)
		scanf("%lf", &a[i]);
	
	double min = a[1], max = a[1], sum = 0;
	for(int i = 1; i <= 7; i++)
	{
		if(a[i] < min)
			min = a[i];
		if(a[i] > max)
			max = a[i];
		sum += a[i];
	}
	
	sum -= max + min;
	
	printf("score=%.2lf", sum / 5.0);
	
	return 0;
}