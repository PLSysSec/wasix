#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>

#include <wasi/api.h>

int main(int argc, char **argv) {

        __wasi_fdstat_t statbuf;
        printf("__wasi_fd_fdstat_get for stdout: %d\n", __wasi_fd_fdstat_get(fileno(stdout), &statbuf));
        printf("rights for stdout: %llu\n", statbuf.fs_rights_base);
        printf("type for stdout: %d\n", statbuf.fs_filetype);
        printf("has filestat_get rights for stdout: %s\n", (statbuf.fs_rights_base & __WASI_RIGHTS_FD_FILESTAT_GET) != 0 ? "yes" : "no");

        __wasi_filestat_t filestat;
        int filestat_res = __wasi_fd_filestat_get(fileno(stdout), &filestat);
        printf("__wasi_fd_filestat_get for stdout: %d\n", filestat_res);
        if (filestat_res != 0) {
                printf("  E: __wasi_fd_filestat_get returned error: %d\n", filestat_res);
        }

        struct stat sb;
        int f = fstat(fileno(stdout), &sb);
        printf("fstat for stdout (fd: %d): %d\n", fileno(stdout), f);

        if (f < 0) {
                perror("  E: fstat returned error");
        }

        return 0;
}