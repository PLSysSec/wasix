plain_c_template = """
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

int main(int argc, char * argv[]) {{
	char global_rbuf[4096];
	char global_wbuf[4096];

	int readRet = 0;
	int writeRet = 0;

	{}  
}}
"""