ORG 0H         ; Start from address 0
MOV P1, #0FFH  ; Initialize Port 1 (turn off all LEDs initially)

; Define delay subroutine
DELAY:
    MOV R0, #250
DELAY_LOOP:
    DJNZ R0, DELAY_LOOP
    RET

; Main program
MAIN:
    ; Repeat each case 8 times
    MOV R2, #8    ; Set loop count for 8 repetitions

; Case 1: Turn on LEDs from left to right
CASE1_LOOP:
    MOV A, #01H   ; Start with the leftmost LED on (bit 0)
CASE1_SHIFT:
    MOV P1, A     ; Output the current value to LEDs
    ACALL DELAY   ; Call delay subroutine
    RL A          ; Shift LED pattern left
    CJNE A, #0, CASE1_SHIFT ; Repeat until all LEDs are on
    DJNZ R2, CASE1_LOOP     ; Repeat case 1

    ; Reset loop count for next case
    MOV R2, #8    

; Case 2: Turn on LEDs from right to left
CASE2_LOOP:
    MOV A, #80H   ; Start with the rightmost LED on (bit 7)
CASE2_SHIFT:
    MOV P1, A     ; Output the current value to LEDs
    ACALL DELAY   ; Call delay subroutine
    RR A          ; Shift LED pattern right
    CJNE A, #0, CASE2_SHIFT ; Repeat until all LEDs are on
    DJNZ R2, CASE2_LOOP     ; Repeat case 2

    ; Reset loop count for next case
    MOV R2, #8

; Case 3: Blink two sets (left and right) alternately
CASE3_LOOP:
    MOV P1, #0F0H ; Turn on the left set of LEDs
    ACALL DELAY
    MOV P1, #0FH  ; Turn on the right set of LEDs
    ACALL DELAY
    DJNZ R2, CASE3_LOOP

    ; Reset loop count for next case
    MOV R2, #8

; Case 4: Blink all 8 LEDs
CASE4_LOOP:
    MOV P1, #00H  ; Turn all LEDs on
    ACALL DELAY
    MOV P1, #0FFH ; Turn all LEDs off
    ACALL DELAY
    DJNZ R2, CASE4_LOOP

    SJMP MAIN     ; Repeat the entire sequence indefinitely

END
