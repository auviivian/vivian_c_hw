#include<stdio.h>

int main()
{
	int A[10] = {0};
	int B[10] = {0};
	int C[10] = {0};
	int i,j = 0;
	FILE*fptr1 = fopen("3.txt","r");
	FILE*fptr2 = fopen("4.txt","r");
	
	if(fptr1 == NULL||fptr2 == NULL)
	{
		printf("Error! opening file");
		return -1;	
	}
	for(i = 0;i < 10;i++)
	{
		fscanf(fptr1,"%d",&A[i]);
		fscanf(fptr2,"%d",&B[i]);
		C[i] = A[i] + B[i];
	}
	
	FILE*fptr3 = fopen("5.txt","w");
	for(i =0;i< 10;i++)
	{
    	fprintf(fptr3,"%d ",C[i]);
		printf("%d\n",C[i]);
	} 
	fclose(fptr1);
	fclose(fptr2);
	return 0;
}
