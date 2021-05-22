
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
	char global_rbuf[4096];
	char global_wbuf[4096];
	for(int i = 0; i < 4096; i++) {
		global_wbuf[i] = 'x';
	}

	int readRet = 0;
	int writeRet = 0;

	int fd1 = open("test_files/small.txt", O_RDONLY);
  if(fd1 == -1) {
    printf("Open failed: %s\n", strerror(errno));
  }
  else {
    printf("Opened test_files/small.txt\n");
  }

	readRet = read(fd1, global_rbuf, 1);
  printf("Read %d bytes\n", readRet);
	writeRet = write(fd1, global_wbuf, 4096);
  printf("Wrote %d bytes\n", writeRet);
	writeRet = write(fd1, global_wbuf, 1);
  printf("Wrote %d bytes\n", writeRet);
}