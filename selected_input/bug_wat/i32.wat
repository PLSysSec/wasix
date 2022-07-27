(module
  (func (param i32) (result i32)
    local.get 0
    i32.const -1
    i32.rem_u
  )
  (func (export "_start")
    i32.const -1
    call 0
    drop
  )
)