#include<stdio.h>

void trans(int data, int base)

{

int x[64],k,i=0;

while(data)

{

x[i]=data%base;

data/=base;

i++;

}

for(k=i-1;k>=0;k--)


 
if(x[k]<10)

printf("%d", x[k]);

else if(x[k]<=16)

printf("%c", 'A'+x[k]-10);

}

int main(void)

{

int num,base;

scanf("%d%d", &num, &base);

if(base<=0||base>16)

{

printf("data error\n");

return;

}

printf("number=%d base=%d\n",num,base);

trans(num,base);

printf("\n");

return 0;

}
