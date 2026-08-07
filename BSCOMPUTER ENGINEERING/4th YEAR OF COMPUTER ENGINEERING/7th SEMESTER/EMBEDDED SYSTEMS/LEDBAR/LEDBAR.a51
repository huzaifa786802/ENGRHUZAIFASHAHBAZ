ORG 0000H
LJMP MAIN
ORG 0030H
MAIN:
    MOV P1, #0FFH      ; Configure P1 as input for buttons
    MOV P2, #00H       ; Configure P2 as output for LED bar
CHECK_BUTTONS:
    MOV A, P1          ; Read button states
    ; Check if button 0 is pressed (active low)
    JNB P1.0, LEFT_TO_RIGHT
    ; Check if button 1 is pressed (active low)
    JNB P1.1, RIGHT_TO_LEFT
    SJMP CHECK_BUTTONS
LEFT_TO_RIGHT:
    MOV R0, #8         ; Counter for 8 LEDs
    MOV R1, #80H       ; Start with leftmost LED (10000000B)
L2R_LOOP:
    MOV P2, R1         ; Output pattern to LED bar
    LCALL DELAY        ; Add delay
    MOV A, R1          ; Move current pattern to accumulator
    RR A               ; Rotate right
    MOV R1, A          ; Store back to R1
    DJNZ R0, L2R_LOOP  ; Repeat until all LEDs are lit
    MOV P2, #0FFH      ; Turn on all LEDs
    LCALL DELAY
    MOV P2, #00H       ; Turn off all LEDs
    SJMP CHECK_BUTTONS
RIGHT_TO_LEFT:
    MOV R0, #8         ; Counter for 8 LEDs
    MOV R1, #01H       ; Start with rightmost LED (00000001B)
R2L_LOOP:
    MOV P2, R1         ; Output pattern to LED bar
    LCALL DELAY        ; Add delay
    MOV A, R1          ; Move current pattern to accumulator
    RL A               ; Rotate left
    MOV R1, A          ; Store back to R1
    DJNZ R0, R2L_LOOP  ; Repeat until all LEDs are lit
    MOV P2, #0FFH      ; Turn on all LEDs
    LCALL DELAY
    MOV P2, #00H       ; Turn off all LEDs
    SJMP CHECK_BUTTONS
DELAY:                 ; Delay subroutine
    MOV R6, #5
DELAY_OUTER:
    MOV R7, #200
DELAY_INNER:
    DJNZ R7, DELAY_INNER
    DJNZ R6, DELAY_OUTER
    RET
END