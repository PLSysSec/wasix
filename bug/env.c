
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/uio.h>
#include <string.h>
#include <errno.h>

int main(int argc, char * argv[]) {
  const char* s = getenv("PATH");
	if(s == NULL)
		printf("getenv returnned NULL");
	else
  	printf("PATH:%s\n", s);
}