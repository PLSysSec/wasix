#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
  int fd0 = open("test_files/small.txt", O_RDWR);
  int fd1 = open("test_files/small.txt", O_RDWR);

  // char buf0[5];
  // read(fd0, buf0, 4);
  // buf0[4] = '\0';
  // printf("read from fd0: %s\n", buf0);

  char buf1[5];
  read(fd1, buf1, 4);
  buf1[4] = '\0';
  printf("read from fd1: %s\n", buf1);

  // read(fd0, buf0, 4);
  // buf0[4] = '\0';
  // printf("read from fd0: %s\n", buf0);

  close(fd0);

  read(fd1, buf1, 4);
  buf1[4] = '\0';
  printf("read from fd1: %s\n", buf1);
}
