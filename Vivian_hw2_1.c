#include<stdio.h>
int main()
{
	int A[10] = {0};
	int i = 0, j = 0;
	int temp = 0;

	printf("Please input 10 mumbers:\n");
	printf("�п�J�Ĥ@�Ӿ��:");
    scanf("%d",&A[0]);
    printf("�п�J�ĤG�Ӿ��:");
    scanf("%d",&A[1]);
    printf("�п�J�ĤT�Ӿ��:");
    scanf("%d",&A[2]);
    printf("�п�J�ĥ|�Ӿ��:");
    scanf("%d",&A[3]);
    printf("�п�J�Ĥ��Ӿ��:");
    scanf("%d",&A[4]);
    printf("�п�J�Ĥ��Ӿ��:");
    scanf("%d",&A[5]);
    printf("�п�J�ĤC�Ӿ��:");
    scanf("%d",&A[6]);
    printf("�п�J�ĤK�Ӿ��:");
    scanf("%d",&A[7]);
    printf("�п�J�ĤE�Ӿ��:");
    scanf("%d",&A[8]);
    printf("�п�J�ĤQ�Ӿ��:");
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
        printf("�e�T�j��:");
    	for( i = 0; i < 3; i++)
    	{
        	printf("%d,", A[i]);
    	}
	return 0;
} 

