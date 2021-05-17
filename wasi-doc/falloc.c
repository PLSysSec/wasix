#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
  int fd = open("falloc.txt", O_RDWR);
  struct stat fs;

  char buf[5];
  read(fd, buf, 4);
  buf[4] = '\0';
  printf("read: %s\n", buf);

  printf("Before fallocate:\n");
  fstat(fd, &fs);
  printf("size is: %lld\n", (long long) fs.st_size);

  int r = posix_fallocate(fd, 0, 1);
  printf("posix_fallocate returns %d\n", r);
  if(r != 0) {
    printf("error is: %s\n", strerror(r));
  }

  printf("After fallocate:\n");
  fstat(fd, &fs);
  printf("size is: %lld\n", (long long) fs.st_size);
}
