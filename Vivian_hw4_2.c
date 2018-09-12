#include <stdio.h>

int main() 
{
	int M[5][5] = {0};
	int N[5][5] = {0};
	int X[5][5] = {0};
	int x, y, i, j = 0;
	FILE*fptr1 = fopen("1.txt","r");
	FILE*fptr2 = fopen("2.txt","r");
	FILE*fptr3 = fopen("3.txt","w");

	if(fptr1 == NULL||fptr2 == NULL) 
	{
		printf("Error! opening file");
		return -1;
	}
	


	printf("Matrix M:\n");


	for (i = 0; i < 5; i++) 
	{
		for (j = 0; j < 5; j++) 
		{
			fscanf(fptr1,"%d",&M[i][j]);
			printf("%d ", M[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	printf("Matrix N:\n");

	for (i = 0; i < 5; i++) 
	{
		for (j = 0; j < 5; j++) 
		{
			fscanf(fptr2,"%d",&N[i][j]);
			printf("%d ", N[i][j]);
		}
		printf("\n");
	}



	for (y = 0; y < 5; y++ ) 
	{ 
		for (x = 0; x < 5; x++ ) 
		{
			for (i = 0; i < 5; i++ ) 
			{
				X[y][x] += M[y][i]*N[i][x];
			}
		}
	}
	printf("\n");
	
	
	printf( "result:\n" );
	for (j = 0; j < 5; j++ ) 
	{
		for (i = 0; i < 5; i++ ) 
		{
			printf( "%d ", X[j][i] );
		}
		printf( "\n" );
	}

	for (j = 0; j < 5; j++ ) 
	{
		for (i = 0; i < 5; i++ ) 
		{
			fprintf(fptr3,"%d ",X[j][i]);
		}
		fprintf(fptr3,"\n");
	}
	fclose(fptr1);
	fclose(fptr2);
	fclose(fptr3);
	return 0;
}
