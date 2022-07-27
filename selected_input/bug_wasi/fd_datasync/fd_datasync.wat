(module
  (import "wasi_snapshot_preview1" "proc_exit"
    (func $__wasi_proc_exit (param i32))
  )
  (import "wasi_snapshot_preview1" "fd_prestat_get" 
    (func $__wasi_fd_prestat_get (param i32 i32) (result i32))
  )
  (import "wasi_snapshot_preview1" "path_open"
    (func $__wasi_path_open
      (param i32 i32 i32 i32 i32 i64 i64 i32 i32)
      (result i32)
    )
  )
  (import "wasi_snapshot_preview1" "fd_datasync"
    (func $__wasi_fd_datasync (param i32) (result i32))
  )

  (func $_start (export "_start")
    (local $err i32)
    (local $dirfd i32)
    (local $prestat_p i32)
    (local $fd_p i32)
    (local $success i32)

    (local.set $prestat_p (call $nalloc (i32.const 8)))
    (if
      (i32.eq (local.get $prestat_p) (global.get $null))
      (then (call $__wasi_proc_exit (i32.const 71)))
    )

    (local.set $fd_p (call $nalloc (i32.const 4)))
    (if
      (i32.eq (local.get $fd_p) (global.get $null))
      (then
        (call $nfree (local.get $prestat_p))
        (call $__wasi_proc_exit (i32.const 71))
      )
    )

    (local.set $dirfd (i32.const 3))
    (local.set $success (i32.const 0))

    (block $break
      (loop $loop
        (local.set $err
          (call $__wasi_fd_prestat_get
            (local.get $dirfd)
            (local.get $prestat_p)
          )
        )
        (if
          (i32.eq (local.get $err) (i32.const 8))
          (then (br $break))
        )
        (if
          (i32.ne (local.get $err) (i32.const 0))
          (then
            (call $nfree (local.get $fd_p))
            (call $nfree (local.get $prestat_p))
            (call $__wasi_proc_exit(i32.const 70))
          )
        )

        (local.set $err
          (call $__wasi_path_open
            (local.get $dirfd)
            (i32.const 1) ;; lookupflags
            (i32.const 8) ;; path
            (i32.const 4) ;; path_len
            (i32.const 0) ;; oflags
            (i64.const 0x1) ;; Set `fd_datasync` bit.
            (i64.const 0x1)
            (i32.const 0x01) ;; Set `append` bit.
            (local.get $fd_p)
          )
        )
        (if
          (i32.ne (local.get $err) (i32.const 0))
          (then
            ;; Failed to open file. Increment dirfd and try again.
            (local.set $dirfd (i32.add (local.get $dirfd) (i32.const 1)))
            (br $loop)
          )
        )

        (local.set $err
          (call $__wasi_fd_datasync
            (i32.load (local.get $fd_p))
          )
        )
        (if
          (i32.ne (local.get $err) (i32.const 0))
          (then
            (call $nfree (local.get $fd_p))
            (call $nfree (local.get $prestat_p))
            (call $__wasi_proc_exit (local.get $err))
          )
        )

        (local.set $success (i32.const 1))
        (br $break)
      )
    )

    (call $nfree (local.get $fd_p))
    (call $nfree (local.get $prestat_p))

    (if
      (i32.eqz (local.get $success))
      (then (call $__wasi_proc_exit (i32.const 1)))
    )

    (call $__wasi_proc_exit (i32.const 0))
  )

  ;; Naive stack-oriented storage allocator. Alignment is 8.
  (func $nalloc (param $size i32) (result i32)
    (local $rem i32)

    (local.set $rem (i32.rem_u (local.get $size) (i32.const 8)))
    (if
      (i32.gt_u (local.get $rem) (i32.const 0))
      (then
        (local.set $size
          (i32.add
            (local.get $size)
            (i32.sub (i32.const 8) (local.get $rem))
          )
        )
      )
    )

    ;; If memory size does not fit requested memory size.
    (if
      (i32.lt_u
        (global.get $mem_size)
        (i32.add (global.get $nallocp) (local.get $size))
      )
      (then
        ;; If `memory.grow` fails, return NULL.
        (if
          (i32.eq
            (memory.grow
              ;; Shift right 16 bits to get number of pages to grow by.
              (i32.shr_u
                (local.get $size)
                (i32.const 16)
              )
            )
            (i32.const -1)
          )
          (then (return (global.get $null)))
        )
      )
    )

    ;; Increase `nallocp` by $size to point to next free element.
    (global.set $nallocp (i32.add (global.get $nallocp) (local.get $size)))

    (return (i32.sub (global.get $nallocp) (local.get $size)))
  )

  ;; Naive free.
  (func $nfree (param $p i32)
    (if
      (i32.lt_u
        (local.get $p)
        (global.get $mem_size)
      )
      (then
        (global.set $nallocp (local.get $p))
      )
    )
  )

  (memory $memory (export "memory") 1)

  (global $null i32 (i32.const 0))

  ;; 64 KiB
  (global $page_size i32 (i32.const 65536))

  ;; We start with 1 page.
  (global $mem_size (mut i32) (i32.const 65536))

  ;; Points to the next free element. Using 0 as NULL.
  (global $nallocp (mut i32) (i32.const 16))

  (data $file_name (i32.const 8) "file\00")
)