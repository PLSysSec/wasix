#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/uio.h>

void print_timespec(const char * prompt, struct timespec * ts) {
  printf("%s: %lld:%ld\n", prompt, (long long) ts->tv_sec, ts->tv_nsec);
}

int main(int argc, char * argv[]) {


  // args_get(argv: Pointer<Pointer<u8>>, argv_buf: Pointer<u8>) -> Result<(), errno>
  // args_sizes_get() -> Result<(size, size), errno>
  printf("argc: %d\n", argc);
  for(int i = 0; i < argc; i++) {
    printf("argv[%d]: %s\n", i, argv[i]);
  }

  // environ_get(environ: Pointer<Pointer<u8>>, environ_buf: Pointer<u8>) -> Result<(), errno>
  // environ_sizes_get() -> Result<(size, size), errno>
  const char* s = getenv("PATH");
  printf("PATH :%s\n",(s!=NULL)? s : "getenv returned NULL");

  // clock_res_get(id: clockid) -> Result<timestamp, errno>
  // clock_time_get(id: clockid, precision: timestamp) -> Result<timestamp, errno>
  struct timespec res;
  struct timespec now;
  clock_getres(CLOCK_REALTIME, &res);
  clock_gettime(CLOCK_REALTIME, &now);
  print_timespec("res", &res);
  print_timespec("now", &now);

  // Files
  int fdA = open("a.txt", O_RDWR);
  char buf[5];
  read(fdA, buf, 4);
  buf[4] = '\0';
  printf("read: %s\n", buf);

  int wn = write(fdA, buf, 4);
  printf("%d bytes written to a.txt\n", wn);


  struct stat statA;
  fstat(fdA, &statA);
  printf("uid: %d\n", statA.st_uid);
  printf("gid: %d\n", statA.st_gid);
  printf("size: %lld\n", statA.st_size);
  print_timespec("last access", &statA.st_atim);
  print_timespec("last modification", &statA.st_mtim);
  print_timespec("last status change", &statA.st_ctim);

  posix_fadvise(fdA, 0, 0, POSIX_FADV_DONTNEED);
  // posix_fallocate(fdA, 0, 1);
  fdatasync(fdA);

  close(fdA);

  srand(time(NULL));
  int rn = rand();
  printf("random number is: %d\n", rn);

  return 0;
}