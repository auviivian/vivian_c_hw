#include<stdio.h>
int main()
{
	int A[10] = {0};
	int i = 0, j = 0;
	int temp = 0;

	printf("Please input 10 mumbers:\n");
	printf("請輸入第一個整數:");
    scanf("%d",&A[0]);
    printf("請輸入第二個整數:");
    scanf("%d",&A[1]);
    printf("請輸入第三個整數:");
    scanf("%d",&A[2]);
    printf("請輸入第四個整數:");
    scanf("%d",&A[3]);
    printf("請輸入第五個整數:");
    scanf("%d",&A[4]);
    printf("請輸入第六個整數:");
    scanf("%d",&A[5]);
    printf("請輸入第七個整數:");
    scanf("%d",&A[6]);
    printf("請輸入第八個整數:");
    scanf("%d",&A[7]);
    printf("請輸入第九個整數:");
    scanf("%d",&A[8]);
    printf("請輸入第十個整數:");
    scanf("%d",&A[9]);
    
	
	for( i = 0; i < 10; i++) 
	{
        for( j = i; j < 10; j++) 
		{
            if( A[j] > A[i] ) 
			{
                temp = A[j];
                A[j] = A[i];
                A[i] = temp;
            }
        }
    }
        printf("前三大為:");
    	for( i = 0; i < 3; i++)
    	{
        	printf("%d,", A[i]);
    	}
	return 0;
} 

