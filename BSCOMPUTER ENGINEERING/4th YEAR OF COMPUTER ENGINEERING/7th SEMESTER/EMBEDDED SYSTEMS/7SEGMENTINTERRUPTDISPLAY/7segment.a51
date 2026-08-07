ORG 000H      ; Reset vector
JMP START      ; Jump to the START label
ORG 0003H      ; Interrupt vector for external interrupt 0
JMP INTO       ; Jump to INTO interrupt service routine
START:
    MOV SP, #30H       ; Initialize stack pointer
    MOV P1, #0FFH      ; Set Port 1 as input (default value)
    MOV P2, #0         ; Clear Port 2
    MOV IE, #10000001B ; Enable external interrupt 0 (INT0) and global interrupts
    CLR IT0            ; Configure INT0 as level-triggered
JMP $                 ; Infinite loop
INTO:
    CLR EX0            ; Clear external interrupt 0 flag
    MOV A, P1          ; Read Port 1
    ANL A, #0FH        ; Mask upper nibble (optional, modify as needed)
    MOV P2, A          ; Output result to Port 2
    SETB EX0           ; Re-enable external interrupt 0
    RETI               ; Return from interrupt
END