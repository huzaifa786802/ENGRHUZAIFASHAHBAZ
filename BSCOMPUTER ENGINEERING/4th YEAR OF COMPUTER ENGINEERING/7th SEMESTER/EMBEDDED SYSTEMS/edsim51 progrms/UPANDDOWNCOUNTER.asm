ORG 0000H            ; Start at address 0
MOV P1, #00H         ; Initialize Port 1 to 0 (all LEDs off)
MOV R0, #00H         ; Initialize counter value to 0
MOV R1, #09H         ; Set maximum count to 9

UP_COUNT:
    MOV A, R0        ; Move the counter value to the accumulator
    MOV P1, A        ; Display the counter value on LEDs
    ACALL DELAY      ; Call delay subroutine
    INC R0           ; Increment counter
    SJMP DOWN_COUNT  ; Jump to DOWN_COUNT when reaching 9

DOWN_COUNT:
    MOV A, R0        ; Move the counter value to the accumulator
    MOV P1, A        ; Display the counter value on LEDs
    ACALL DELAY      ; Call delay subroutine
    DEC R0           ; Decrement counter
    CJNE R0, #00H, DOWN_COUNT ; If R0 != 0, continue counting down
    SJMP UP_COUNT    ; Jump back to UP_COUNT when reaching 0

DELAY:               ; Delay subroutine for LED visibility
    MOV R2, #250     ; Load R2 with 250 (outer loop counter)
D1: MOV R3, #250     ; Load R3 with 250 (inner loop counter)
D2: DJNZ R3, D2      ; Decrement R3 until it reaches 0
    DJNZ R2, D1      ; Decrement R2 until it reaches 0
    RET              ; Return from delay

END                  ; End of program
