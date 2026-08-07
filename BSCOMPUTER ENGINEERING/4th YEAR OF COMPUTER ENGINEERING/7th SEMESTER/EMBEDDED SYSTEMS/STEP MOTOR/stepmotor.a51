ORG 0000H       ; Starting address of the program
MAIN:
    MOV A, #0FEH    ; Initialize accumulator with 1111 1110 (binary)
    MOV P1, A       ; Send initial value to Port 1 (LEDs)
LOOP:
    ACALL DELAY     ; Call delay subroutine
    ACALL DELAY_5US ; Call 5-microsecond delay
    RR A            ; Rotate accumulator right
    MOV P1, A       ; Update Port 1 with the rotated value
    SJMP LOOP       ; Repeat the loop
; Delay subroutine to create a visible effect of rotation
DELAY:
    MOV R0, #200    ; Outer loop count
D1: MOV R1, #255    ; Inner loop count
D2: DJNZ R1, D2     ; Decrement R1 until it reaches 0
    DJNZ R0, D1     ; Decrement R0 until it reaches 0
    RET             ; Return from subroutine
; Subroutine for 5 microsecond delay (approximation based on 8051 clock cycle)
DELAY_5US:
    NOP             ; 1 machine cycle (1 microsecond for 12 MHz clock)
    NOP             ; 1 machine cycle
    NOP             ; 1 machine cycle
    NOP             ; 1 machine cycle
    NOP             ; 1 machine cycle
    RET             ; Return from subroutine
END