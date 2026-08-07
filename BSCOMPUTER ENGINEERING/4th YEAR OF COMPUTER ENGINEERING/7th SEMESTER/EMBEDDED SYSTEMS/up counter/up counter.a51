; Up Counter Program for 7-Segment Displays using Table Lookup
ORG 0000H
    LJMP MAIN        ; Jump to main program
; 7-Segment Display Lookup Table (Common Cathode)
; Each entry represents the pattern to display a digit (0-9)
ORG 0030H
LOOKUP_TABLE:
    DB 3FH   ; 0 - 0011 1111
    DB 06H   ; 1 - 0000 0110
    DB 5BH   ; 2 - 0101 1011
    DB 4FH   ; 3 - 0100 1111
    DB 66H   ; 4 - 0110 0110
    DB 6DH   ; 5 - 0110 1101
    DB 7DH   ; 6 - 0111 1101
    DB 07H   ; 7 - 0000 0111
    DB 7FH   ; 8 - 0111 1111
    DB 6FH   ; 9 - 0110 1111
; Main Program
ORG 0100H
MAIN:
    ; Initialize Port 1 for output (7-segment displays)
    MOV P1, #00H     ; Clear Port 1
    ; Initialize counter variables
    MOV R2, #00H     ; Units digit
    MOV R3, #00H     ; Tens digit
COUNTER_LOOP:
    ; Display current number
    ACALL DISPLAY_NUMBER
    ; Delay for 0.1 seconds
    ACALL DELAY
    ; Increment units digit
    INC R2
    MOV A, R2
    CJNE A, #10, CHECK_CONTINUE
    ; Reset units digit and increment tens digit
    MOV R2, #00H
    INC R3
    MOV A, R3
    CJNE A, #10, CHECK_CONTINUE
    ; Reset entire counter when reaching 99
    MOV R3, #00H
CHECK_CONTINUE:
    SJMP COUNTER_LOOP
; Subroutine to display current number on 7-segment displays
DISPLAY_NUMBER:
    ; Get segment pattern for units digit
    MOV A, R2
    MOVC A, @A+DPTR
    MOV P1, A        ; Display on DS4 (units digit)
    ; Get segment pattern for tens digit
    MOV A, R3
    MOVC A, @A+DPTR
    SWAP A           ; Move tens digit pattern to upper nibble
    ORL P1, A        ; Display on DS3 (tens digit)
    RET
; Delay Subroutine for 0.1 seconds (approximate)
; Assumes 12 MHz crystal oscillator
DELAY:
    MOV R7, #50      ; Outer loop counter
DELAY_OUTER:
    MOV R6, #250     ; Inner loop counter
DELAY_INNER:
    DJNZ R6, DELAY_INNER
    DJNZ R7, DELAY_OUTER
    RET
END