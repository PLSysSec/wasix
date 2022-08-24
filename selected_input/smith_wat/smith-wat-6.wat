(module
  (type (;0;) (func (param v128) (result i32 i32 f64)))
  (import "" "" (global (;0;) f32))
  (import "\5c" "" (table (;0;) 294 externref))
  (import "?&\c7\95i" "" (global (;1;) (mut f64)))
  (import "\0bo!b" "" (global (;2;) v128))
  (import "rf" "" (memory (;0;) 3953 8373))
  (func (;0;) (type 0) (param v128) (result i32 i32 f64)
    global.get 3
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 3
    i32.const 1
    i32.sub
    global.set 3
    loop (result externref)  ;; label = @1
      global.get 3
      i32.eqz
      if  ;; label = @2
        unreachable
      end
      global.get 3
      i32.const 1
      i32.sub
      global.set 3
      table.size 0
      i8x16.splat
      f32x4.ceil
      f64x2.trunc
      drop
      ref.null extern
    end
    drop
    i32.const 0
    i32.const 0
    f64.const 0x0p+0 (;=0;)
  )
  (global (;3;) (mut i32) i32.const 100)
  (elem (;0;) externref)
  (data (;0;) "")
)
