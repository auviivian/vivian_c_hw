#include <stdio.h>
#include <stdbool.h>

bool isPrime;

int main() 
{
	float num = 0;
	printf("Please enter a prime number:");
	scanf("%f", &num);

	if( num <= 1 ) 
	{
		printf("%.3f isn't a prime number!!!\n", num);
		printf("Please enter an integer greater than 1.\n");
		return -1;
	}
	if(num-(int)num!= 0 ) 
	{
		printf("Please do not enter a decimal.\n");
		return -1;
	}


	int p = 2;
	for(p = 2; p <= num; p++) 
	{
		isPrime = true;
		int d = 2;
		for(d = 2; d < p; d++) 
		{
			if (p % d == 0) 
			{
				isPrime = false;
			}
		}

		if (isPrime) 
		{
			printf("%d\n", p);
		}
	}
	return 0;
}
