(module
  (type (;0;) (func (param externref)))
  (type (;1;) (func))
  (import "\02" "" (table (;0;) 1156 externref))
  (func (;0;) (type 1)
    global.get 0
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 0
    i32.const 1
    i32.sub
    global.set 0
    i64.const -620786082216367485
    drop
    loop  ;; label = @1
      global.get 0
      i32.eqz
      if  ;; label = @2
        unreachable
      end
      global.get 0
      i32.const 1
      i32.sub
      global.set 0
      data.drop 0
      data.drop 1
      f64.const 0x1.728e1cf627b84p+519 (;=2484166001346348200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000;)
      ref.null extern
      f32.const 0x1.54p-142 (;=0.000000000000000000000000000000000000000000238;)
      drop
      drop
      drop
    end
  )
  (func (;1;) (type 0) (param externref)
    global.get 0
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 0
    i32.const 1
    i32.sub
    global.set 0
  )
  (memory (;0;) 0)
  (global (;0;) (mut i32) i32.const 100)
  (export "lk\11" (memory 0))
  (export "" (memory 0))
  (data (;0;) "")
  (data (;1;) "s")
)
