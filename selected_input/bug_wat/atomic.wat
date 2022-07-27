(module
    (memory 1)
    (func (export "_start")
        i32.const 0xffff_fff0
        i32.atomic.load offset=16
        drop
    )
)