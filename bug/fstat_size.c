
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
  int fd = open("test_files/small.txt", O_RDONLY);
  struct stat fs;
  fstat(fd, &fs);
  printf("size is: %lld\n", (long long) fs.st_size);
}