/* from acmicpc.net, solved on 2015 */


#include <stdio.h>


int main()
{
     int n, a, b, r = 1;

     scanf("%d %d %d", &n, &a, &b);

     if (!(a % 2))
      a -= 1;

     if (!(b % 2))
      b -= 1;

     while (a/2 != b/2)
     {
          a /= 2;
          b /= 2;
          r++;
     }

     printf("%d\n", r);
}
