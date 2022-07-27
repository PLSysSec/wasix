(module
      (type (;0;) (func))
      (func (;0;) (type 0)
        global.get 0
        i32.eqz
        if  ;; label = @1
          unreachable
        end
        global.get 0
        i32.const 1
        i32.sub
        global.set 0)
      (memory (;0;) 0 1)
      (global (;0;) (mut i32) (i32.const 1000))
      (export "" (func 0))
      (export "\0e" (func 0))
      (data (;0;) (i32.const 249) "")
      (func (export "_start")))