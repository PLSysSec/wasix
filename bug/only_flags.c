
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

	int fd1 = open("test_files/small.txt", O_WRONLY);
  if(fd1 == -1) {
    printf("Open failed: %s\n", strerror(errno));
  }
  else {
    printf("Opened test_files/small.txt in O_WRONLY\n");
  }
	readRet = read(fd1, global_rbuf, 4096);
	printf("Read %d bytes, should be -1\n", readRet);
	close(fd1);

	fd1 = open("test_files/small.txt", O_RDONLY);
  if(fd1 == -1) {
    printf("Open failed: %s\n", strerror(errno));
  }
  else {
    printf("Opened test_files/small.txt in O_RDONLY\n");
  }
	writeRet = write(fd1, global_rbuf, 4096);
	printf("Wrote %d bytes, should be -1\n", writeRet);
	close(fd1);
}