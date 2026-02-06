x equ 45 ;x赋值为45
y equ 64 ;y赋值为64
stack_top equ 0x1000
	area code1,code,readonly
	entry
	code32
_strart ;代码开始标志
	mov sp, #stack_top ;初始化堆栈指针
	mov r0, #x ; r0 = 45
	
	str r0,[sp]  ;?str是什么指令来着
	
	mov r0, #y  ;r0 = 64
	ldr r1,[sp] ;r1 = 
	add r0, r0, r1
	
	str r0, [sp]
stop	b stop
	end
