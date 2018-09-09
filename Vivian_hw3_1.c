#include<stdio.h>




int main()
{
	int A[10] = {0};
	int i =0;
	int j =0;
	int temp = 0;
	FILE*fptr = fopen("1.txt","r");

	if(fptr == NULL)
	{
		printf("Error! opening file");
		return -1;	
	}
	for(i =0;i< 10;i++)
	{
		fscanf(fptr,"%d",&A[i]);
	} 

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
   	fclose(fptr);
    FILE*fptr2 = fopen("2.txt","w");
    for(i =0;i< 10;i++)
	{
    	fprintf(fptr,"%d ",A[i]);
		printf("%d\n",A[i]);
	} 
	

	return 0;
 } 
