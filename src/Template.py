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
#include <unistd.h>
#include "log.c"

int main(int argc, char * argv[]) {{
	char global_rbuf[4096];
	char global_wbuf[4096];
	for(int i = 0; i < 4096; i++) {{
		global_wbuf[i] = 'x';
	}}

	int syscallCnt = 0;
	int badSyscallCnt = 0;
	int syscallRet = 0;
	{}  
	printf("@Total syscall cnt:%d\\n", syscallCnt);
	printf("@Bad syscall cnt:%d\\n", badSyscallCnt);
}}
"""


report_template="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>

<head>
    <meta http-equiv="Content-Type"
          content="text/html; charset=utf-8" />
    <title>WASIX Report</title>
    <style type="text/css">
      .wasix-clear {{
        color: green;
      }}
      .wasix-error {{
        color: red
      }}

      dl {{
        display: table;
        margin: 0 auto;
      }}

      p {{
        text-align:center;
      }}

      table {{
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }}

      td, th {{
        border: 1px solid black;
        font-weight: normal;
      }}

    </style>
</head>

<body>
  <p>Report generated at {}</p>
  <dl>
    {}
  </dl>
</body>

</html>
"""