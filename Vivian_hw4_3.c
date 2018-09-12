#include<stdio.h>
#define max 10000

int main(void) 
{
	float num[max] = {0,1};
	float number = 0;
	int i = 2;
	int j = 0;
	printf("Please enter an integer:\n");
	scanf("%f",&number);

	if(number == 0 || number == 1) 
	{
		printf("Fib(%.0f)=%.0f\n",number,number);
		return 0;
	}

	if(number < 0) 
	{
		printf("Please do not enter negative numbers.\n");
		return -1;
	}
	if(number-(int)number!= 0) 
	{
		printf("Please do not enter a decimal.\n");
		return -1;
	}


	for(i = 2; i <= number ; i++) 
	{
		num[i]=num[i-1]+num[i-2];
	}
	for(j = 0; j <= number ; j++) 
	{
		printf("Fib(%d)=%.0f\n",&j,num[j]);
	}
	return 0;
}

