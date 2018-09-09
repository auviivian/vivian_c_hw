#include<stdio.h>
int main()
{
	int i,j = 2;
	int isPrime(int i);
	printf("Please enter a prime number:");
	scanf("%d",&i);
	
	   if ( i == 0 || i == 1)
	   {
	   	printf("%d isn't a prime number!!!\n", i);
	   	printf("Please enter an integer greater than 1.\n", i);
	   	return 0;
	   }
	   
	   if ( i < 0 )
	   {
	   	printf("%d isn't a prime number!!!\n", i);
	   	printf("Please enter an integer greater than 1.\n", i);
	   	return 0;
	   }
	   
	    if(isPrime(i))
    		{
        		printf("%d is a prime number.\n", i);
    		}
			else
			{
        		printf("%d isn't a prime number!!!\n", i);
    		}
    		return 0;
    	}
	
		int isPrime(int i)
		{
    		if(i == 1)
        	return 0;
        	int j = 2;
            for(j = 2; j*j <= i; j++)
    		{
        		if(i%j == 0)
        	    {
            		return 0;
        		}
    	    }	
    		return 1;
		}
    
	
//		for ( j = 2 ; j <= (i-1); j++ )
//		{
//			if ( i%j == 0 )
//			{
//				printf("%d isn't a prime number!!!\n", i);
//				break;
//			}
//		}
//			if ( j == i )
//			{
//				printf("%d is a prime number.\n", i);
//				return 0;
//			}
//			
//				return 0;
//}
