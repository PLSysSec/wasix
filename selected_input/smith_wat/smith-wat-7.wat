(module
  (type (;0;) (func (result f32 v128 i64 externref)))
  (func (;0;) (type 0) (result f32 v128 i64 externref)
    (local i64)
    global.get 0
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 0
    i32.const 1
    i32.sub
    global.set 0
    f32.const -0x1.191756p-22 (;=-0.00000026178654;)
    ref.func 0
    block  ;; label = @1
      local.get 0
      f64.const 0x1.4e9a6c6cecf78p-493 (;=0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000051109576738956326;)
      call 1
      nop
      data.drop 0
      br 0 (;@1;)
      loop (result f32)  ;; label = @2
        global.get 0
        i32.eqz
        if  ;; label = @3
          unreachable
        end
        global.get 0
        i32.const 1
        i32.sub
        global.set 0
        i32.const 541792931
        ref.null func
        drop
        drop
        f32.const 0x0p+0 (;=0;)
      end
      drop
      drop
      drop
      drop
      drop
      drop
      drop
    end
    drop
    v128.const i32x4 0x00000000 0x00000000 0x00000000 0x00000000
    i64.const 0
    ref.null extern
  )
  (func (;1;) (type 0) (result f32 v128 i64 externref)
    global.get 0
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 0
    i32.const 1
    i32.sub
    global.set 0
    f32.const 0x0p+0 (;=0;)
    v128.const i32x4 0x00000000 0x00000000 0x00000000 0x00000000
    i64.const 0
    ref.null extern
  )
  (func (;2;) (type 0) (result f32 v128 i64 externref)
    global.get 0
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 0
    i32.const 1
    i32.sub
    global.set 0
    f32.const 0x0p+0 (;=0;)
    v128.const i32x4 0x00000000 0x00000000 0x00000000 0x00000000
    i64.const 0
    ref.null extern
  )
  (global (;0;) (mut i32) i32.const 100)
  (elem (;0;) declare externref)
  (elem (;1;) declare funcref (ref.func 0))
  (data (;0;) "")
)
