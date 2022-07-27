(module
  (memory 1)
  (func (export "_start")
        call 1
        drop)

  (func (result v128)
    v128.const i32x4 0 0 0 0
    i32.const 1
    v128.load
    v128.xor)
)