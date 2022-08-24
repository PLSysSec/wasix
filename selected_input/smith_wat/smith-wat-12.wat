(module
  (type (;0;) (func (param funcref)))
  (type (;1;) (func (param i64 v128)))
  (func (;0;) (type 1) (param i64 v128)
    (local f64 i64 f32 v128)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
    i32.const -1052566610
    f64.convert_i32_s
    local.set 2
    table.size 0
    global.get 0
    f64.load align=1
    f64.abs
    f32.const 0x0p+0 (;=0;)
    drop
    drop
    drop
  )
  (func (;1;) (type 0) (param funcref)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
  )
  (func (;2;) (type 0) (param funcref)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
  )
  (func (;3;) (type 0) (param funcref)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
  )
  (func (;4;) (type 1) (param i64 v128)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
  )
  (func (;5;) (type 0) (param funcref)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
  )
  (table (;0;) 0 119727 externref)
  (memory (;0;) 0 40437)
  (global (;0;) i32 i32.const -1478100410)
  (global (;1;) (mut i32) i32.const 100)
)
