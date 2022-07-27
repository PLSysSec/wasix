(module
  (import "wasi_snapshot_preview1" "proc_exit"
    (func $__wasi_proc_exit (param i32))
  )
  (import "wasi_snapshot_preview1" "fd_datasync"
    (func $__wasi_fd_datasync (param i32) (result i32))
  )

  (func $_start (export "_start")
    (call $__wasi_fd_datasync
      (i32.const 1)
    )
    call $__wasi_proc_exit
  )

  (memory $memory (export "memory") 1)
)