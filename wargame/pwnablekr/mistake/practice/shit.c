#include <stdio.h>
#include <fcntl.h>

int main()
{
  int fd;
  if(fd=open("./password",O_RDONLY,0400) < 0){
	printf("can't open password %d\n", fd);
	return 0;
  }
  if((fd=open("./password",O_RDONLY,0400)) < 0){
	printf("can't open password %d\n", fd);
	return 0;
  }
}
