
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/uio.h>
#include "log.c"

int main(int argc, char * argv[]) {
	char global_rbuf[4096];
	char global_wbuf[4096];
	for(int i = 0; i < 4096; i++) {
		global_wbuf[i] = 'x';
	}

	int readRet = 0;
	int writeRet = 0;

	FILE *fp = fopen("9a267460759ed471.trace", "w");
	log_add_fp(fp, LOG_TRACE);
	int fd3 = open("test_files/not_exist.txt", O_RDWR | O_CREAT | O_EXCL);
	writeRet = write(fd3, global_wbuf, 4096);
	log_trace("numOfBytes Written %d", writeRet);
	int fd2 = open("test_files/not_exist.txt", O_RDWR | O_CREAT);
	readRet = read(fd3, global_rbuf, 1);
	log_trace("numOfBytes Read %d", readRet);
	// posix_fallocate(fd2, 0, 0);
	readRet = read(fd2, global_rbuf, 1);
	log_trace("numOfBytes Read %d", readRet);
	readRet = read(fd3, global_rbuf, 1);
	log_trace("numOfBytes Read %d", readRet);
	// posix_fallocate(fd2, 0, 0);
	struct timespec ts_8;
	clock_getres(CLOCK_REALTIME, &ts_8);
	writeRet = write(fd3, global_wbuf, 0);
	log_trace("numOfBytes Written %d", writeRet);
	close(fd3);
	writeRet = write(fd2, global_wbuf, 2283);
	log_trace("numOfBytes Written %d", writeRet);
	writeRet = write(fd2, global_wbuf, 2332);
	log_trace("numOfBytes Written %d", writeRet);
	readRet = read(fd2, global_rbuf, 0);
	log_trace("numOfBytes Read %d", readRet);
	int fd1 = open("test_files/not_exist.txt", O_RDWR);
	posix_fallocate(fd1, 0, 0);
	posix_fallocate(fd2, 0, 0);
	writeRet = write(fd1, global_wbuf, 4096);
	log_trace("numOfBytes Written %d", writeRet);
	readRet = read(fd1, global_rbuf, 4096);
	log_trace("numOfBytes Read %d", readRet);
	readRet = read(fd2, global_rbuf, 4096);
	log_trace("numOfBytes Read %d", readRet);
	struct timespec ts_20;
	clock_getres(CLOCK_REALTIME, &ts_20);
	int fd0 = open("test_files/small.txt", O_RDWR);
	posix_fallocate(fd0, 0, 0);
	writeRet = write(fd0, global_wbuf, 2558);
	log_trace("numOfBytes Written %d", writeRet);
	readRet = read(fd1, global_rbuf, 0);
	log_trace("numOfBytes Read %d", readRet);
	writeRet = write(fd0, global_wbuf, 3479);
	log_trace("numOfBytes Written %d", writeRet);
	readRet = read(fd0, global_rbuf, 1);
	log_trace("numOfBytes Read %d", readRet);
	struct timespec ts_27;
	clock_gettime(CLOCK_REALTIME, &ts_27);
	readRet = read(fd1, global_rbuf, 0);
	log_trace("numOfBytes Read %d", readRet);
	posix_fallocate(fd2, 0, 0);
}
