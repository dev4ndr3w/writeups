#include <stdio.h>

int main()
{
	char v0[] = "\x90\x90\x90";
	char v1[2] = "\x90\x90\x90\x90";
	char v2[2] = "\x90";
	printf("%d\n%d\n%d", sizeof(v0), sizeof(v1), sizeof(v2));

	return 0;
}
