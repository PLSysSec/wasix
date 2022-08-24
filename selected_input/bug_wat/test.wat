(module
    (memory 1)

    (func
        i32.const 0xffff_fff0
        i32.atomic.load offset=16
        drop
    )
    (start 0)
)