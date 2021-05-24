
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/uio.h>

int main(int argc, char * argv[]) {
  char global_rbuf[4096];
  char global_wbuf[4096];

  int fd1 = open("small.txt", O_RDONLY);
	write(fd1, global_wbuf, 1);
	posix_fallocate(fd1, 0, 0);
	read(fd1, global_rbuf, 401);
	write(fd1, global_wbuf, 0);
	write(fd1, global_wbuf, 1);
	posix_fallocate(fd1, 0, 0);
	write(fd1, global_wbuf, 2306);
	struct timespec ts_8;
	clock_getres(CLOCK_REALTIME, &ts_8);
	close(fd1);  
}
