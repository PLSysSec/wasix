(module
  (type (;0;) (func (result funcref)))
  (type (;1;) (func (param f64 i64) (result i32)))
  (type (;2;) (func (param f64) (result externref)))
  (func (;0;) (type 2) (param f64) (result externref)
    (local f64 i64 i64 i64)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
    f32.const 0x1.8f3baap+103 (;=15815251000000000000000000000000;)
    f64.promote_f32
    call 1
    drop
    drop
    ref.null extern
  )
  (func (;1;) (type 0) (result funcref)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
    ref.null func
  )
  (memory (;0;) 2377)
  (global (;0;) f64 f64.const 0x1.534a5a7b57355p+163 (;=15496048068242860000000000000000000000000000000000;))
  (global (;1;) (mut i32) i32.const 100)
  (export "-" (func 1))
  (export "=4I\14=" (global 0))
  (export "" (global 0))
  (elem (;0;) externref)
  (elem (;1;) declare func)
)
