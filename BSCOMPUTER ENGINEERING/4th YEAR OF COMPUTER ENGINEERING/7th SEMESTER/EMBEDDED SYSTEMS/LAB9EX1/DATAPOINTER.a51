; LED Pattern Table Lookup Demonstration
; Uses MOVC A,@A+DPTR instruction to read LED patterns from program memory

ORG 0000H
    LJMP MAIN        ; Jump to main program

; LED Pattern Table in Program Memory
ORG 0100H
LED_PATTERNS:
    DB 01H           ; Pattern 1: First LED
    DB 02H           ; Pattern 2: Second LED
    DB 04H           ; Pattern 3: Third LED
    DB 08H           ; Pattern 4: Fourth LED
    DB 10H           ; Pattern 5: Fifth LED
    DB 20H           ; Pattern 6: Sixth LED
    DB 40H           ; Pattern 7: Seventh LED
    DB 80H           ; Pattern 8: Eighth LED
    DB 81H           ; Pattern 9: First and Last LED
    DB 42H           ; Pattern 10: Second and Seventh LED
    DB 24H           ; Pattern 11: Third and Sixth LED
    DB 18H           ; Pattern 12: Fourth and Fifth LED
    DB 3CH           ; Pattern 13: Middle four LEDs
    DB 7EH           ; Pattern 14: Outer six LEDs
    DB 99H           ; Pattern 15: Alternating LEDs
    DB 55H           ; Pattern 16: Checkerboard pattern
    DB 33H           ; Pattern 17: Another alternating pattern
    DB 0F0H          ; Pattern 18: Upper nibble
    DB 0FH           ; Pattern 19: Lower nibble
    DB 0AAH          ; Pattern 20: Another alternating pattern
    DB 55H           ; Pattern 21: Complementary pattern
    DB 00H           ; Pattern 22: All LEDs off
    DB 0FFH          ; Pattern 23: All LEDs on

MAIN:
    MOV P2, #00H     ; Initialize Port 2 (LED Port) to all LEDs off
    MOV DPTR, #LED_PATTERNS  ; Load data pointer to start of LED patterns
    MOV R0, #23      ; Initialize loop counter (23 patterns)

PATTERN_LOOP:
    ; Read pattern from program memory
    MOV A, R0        ; Move loop counter to accumulator
    DEC A            ; Adjust for zero-based indexing
    MOVC A, @A+DPTR  ; Read pattern byte from program memory
    MOV P2, A        ; Display pattern on Port 2 (LEDs)

    ; Delay routine for 0.1 seconds
    ACALL DELAY_100MS

    ; Decrement loop counter
    DJNZ R0, PATTERN_LOOP

    ; Infinite loop after displaying all patterns
STOP:
    SJMP STOP

; Delay Routine for approximately 0.1 seconds
; Assumes 12 MHz crystal oscillator
DELAY_100MS:
    MOV R7, #250     ; Outer loop counter
OUTER_LOOP:
    MOV R6, #250     ; Inner loop counter
INNER_LOOP:
    DJNZ R6, INNER_LOOP  ; Decrement inner loop
    DJNZ R7, OUTER_LOOP  ; Decrement outer loop
    RET

END