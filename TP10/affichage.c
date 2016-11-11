#include<stdio.h>
 
int aff_chaine(char * p)
{
  printf("%s\n", p);
  return 0;
}
 
long multiplier(long a, long b)
{
  return a * b;
}
 
int jakadi(char ** p)
{
  printf("%s\n", *p);
  printf("Jakadi a dit: ");
  scanf("%s",*p);
  printf("%s\n", *p);
  return 0;
}
