	area addressingMode_1,CODE,READONLY
	entry
	mov r5, #15
	mov r2, #0xC
	mov r1, r5
	add r0, r1, r2 ;r0 = 0x18
	add r0, r1, r2, lsr #1 ;
	ldr r4, =0x90000
	str r0,[r4]
	str r0,[r4, #4]
	str r0, [r4, #4]!
	str r0, [r4], #4
here 	b here
	end