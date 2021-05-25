#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
  int fd0 = open("test_files/small.txt", O_RDWR);
  int fd1 = open("test_files/small.txt", O_RDWR);
  int len = 5;
  char buf0[len];
  char buf1[len];
  for(int i = 0; i < len; i++) {
    buf0[i] = 'a';
    buf1[i] = 'a';
  }
  
  int ret0 = 999;
  int ret1 = 999;

  ret0 = write(fd0, buf0, len);
  printf("wrote to fd0 %d bytes\n", ret0);

  ret1 = write(fd1, buf1, len);
  printf("wrote to fd1 %d bytes\n", ret1);

  ret0 = write(fd0, buf0, len);
  printf("wrote to fd0 %d bytes\n", ret0);

  close(fd0);

  ret1 = write(fd1, buf1, len);
  printf("wrote to fd1 %d bytes\n", ret1);
}
