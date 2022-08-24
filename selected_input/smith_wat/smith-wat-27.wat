(module
  (type (;0;) (func (result v128 funcref f64 f32 i64 funcref)))
  (type (;1;) (func))
  (import "" "" (func (;0;) (type 0)))
  (import "" "" (table (;0;) 0 253081 externref))
  (func (;1;) (type 1)
    global.get 2
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 2
    i32.const 1
    i32.sub
    global.set 2
    v128.const i32x4 0xeac37d15 0x00007607 0x00000000 0x00000000
    drop
  )
  (func (;2;) (type 0) (result v128 funcref f64 f32 i64 funcref)
    global.get 2
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 2
    i32.const 1
    i32.sub
    global.set 2
    v128.const i32x4 0x00000000 0x00000000 0x00000000 0x00000000
    ref.null func
    f64.const 0x0p+0 (;=0;)
    f32.const 0x0p+0 (;=0;)
    i64.const 0
    ref.null func
  )
  (memory (;0;) 2376 3969)
  (global (;0;) i64 i64.const -20981490820825695)
  (global (;1;) (mut i64) i64.const -1150440813586937777)
  (global (;2;) (mut i32) i32.const 100)
  (start 1)
  (data (;0;) (i32.const 2717029) "")
  (data (;1;) "")
)
