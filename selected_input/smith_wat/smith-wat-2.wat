(module
  (type (;0;) (func (param f64) (result i64)))
  (func (;0;) (type 0) (param f64) (result i64)
    (local externref externref f32)
    global.get 1
    i32.eqz
    if  ;; label = @1
      unreachable
    end
    global.get 1
    i32.const 1
    i32.sub
    global.set 1
    local.get 1
    local.get 3
    i64.trunc_sat_f32_s
    elem.drop 1
    data.drop 0
    i32.wrap_i64
    global.get 0
    local.tee 3
    f32.ceil
    f32.abs
    i32.trunc_sat_f32_s
    drop
    drop
    drop
    i64.const 0
  )
  (memory (;0;) 421)
  (global (;0;) f32 f32.const -0x1.51e09p+98 (;=-418271700000000000000000000000;))
  (global (;1;) (mut i32) i32.const 100)
  (export "" (global 0))
  (export "\0c\c3\a4(" (global 0))
  (elem (;0;) externref)
  (elem (;1;) declare externref)
  (data (;0;) (i32.const 1064726) "\ef")
)
