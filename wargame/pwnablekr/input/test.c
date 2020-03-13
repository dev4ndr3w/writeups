#include <stdio.h>
int main()
{
    char s[]={"a"};
    FILE *f = fopen("\x0a", "w");
    fwrite(s, 1, 1, f);
    
}
