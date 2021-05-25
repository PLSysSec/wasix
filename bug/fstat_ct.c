#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
  int fd = open("test_files/small.txt", O_RDWR);
  struct stat fs;
  fstat(fd, &fs);
  printf("last status change time is: %lld:%lld\n", 
    (long long) fs.st_ctim.tv_nsec, (long long) fs.st_ctim.tv_nsec);
}
