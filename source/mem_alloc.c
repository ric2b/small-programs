#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>

#define MB 1048576u
#define Mb 131072u

int main()
{
	unsigned int n = 1;
	int check;
	char * aux;
	while (1)
	{
		printf("how many 100MB blocks to allocate? 0 to leave >> ");
		check = scanf("%ud", &n);
		if(n == 0 || check != 1)
		{
			puts("leaving, bye");
			exit(0);
		}
		
		if(100*Mb > INT_MAX/n)
		{
			printf("integer overflow, try allocating less than %d 100MB blocks\n\n", INT_MAX/(100*Mb));
		}
		else
		{				
			aux = (char *) calloc(n*100*Mb,8); /*100MB * number of blocks*/
			if(aux == NULL)
			{
				puts("Can't allocate this ammount of memory");
			}
			else
			{
				memset(aux, rand()%50+1,n*100*MB);
				
				puts("sucessful alloc, press enter to free");
				getchar();
				getchar();
				free(aux);
				puts("memory freed\n");
			}		
		}
	}
}
