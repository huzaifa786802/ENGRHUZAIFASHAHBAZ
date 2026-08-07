; Program to toggle between even and odd LEDs on an 8051 microcontroller
; using Keil Assembly Language
ORG 0000H          ; Origin, start of the program
START:          ; Start label
    MOV P1, #0  ; Initialize Port 1 to 0 (all LEDs off)
MAIN_LOOP:      ; Main loop label
    MOV A, P1   ; Move current state of Port 1 to Accumulator A
    CPL A       ; Complement the accumulator (toggle the state)
    MOV P1, A   ; Output the toggled state back to Port 1
    ACALL DELAY ; Call delay subroutine
    SJMP MAIN_LOOP ; Jump back to main loop
DELAY:          ; Delay subroutine
    MOV R0, #20 ; Load R0 with a value for delay
DELAY_LOOP:     
    NOP          ; No operation (do nothing)
    DJNZ R0, DELAY_LOOP ; Decrement R0 and repeat if not zero
    RET          ; Return from subroutine
END             ; End of program