#include<stdio.h>
int main()
{
	int num1 = 0;
	int num2 = 0;
	int i,j = 0;
	int aarray[10] = {0};
	int temp = 0;
	printf("Please enter 2 numbers:\n");
	scanf("%d\n%d",&num1,&num2);
	printf("Two numbers that you input are :%d,%d",num1,num2);
	
	
	for(i = 0;i < 10; i++)
	{
		num1%aarray[i];
		for(j = 0;j < 10;j++)
		{
			num2%aarray[j];
			temp = aarray[j];
			aarray[j] = aarray[i];
			aarray[i] = temp;
		}
	}
		printf("%d\n",aarray[j]);
	
	printf("\nThe result is:\n");
	for(i = 0;i < 1;i++)
	{
		printf("%d",aarray[i]); 
	}
	return 0;
 } 
