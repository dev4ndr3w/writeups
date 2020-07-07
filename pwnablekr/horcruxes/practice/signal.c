#include <stdio.h>
#include <signal.h>


typedef void (*sighandler_t)(int);
void handle_signal(unsigned int sig)
{
	printf("signal num: %d", sig);
}

int main()
{
	signal(SIGINT, (sighandler_t)handle_signal);
	while(1){}
	return 0;
}

