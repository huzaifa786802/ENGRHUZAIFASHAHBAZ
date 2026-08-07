; 8051 Assembly Code for LED Patterns using Table Lookup
; This program demonstrates LED patterns stored in memory.
; Each pattern stays on for 0.1 seconds.
ORG 0000H       ; Origin, start of program memory
; Define the LED patterns in a lookup table
PATTERNS: DB 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80 ; 8 patterns for LEDs
; Define constants
DELAY_COUNT EQU 250 ; Adjust this value to achieve approximately 0.1 seconds delay
; Main program starts here
START:  
    MOV DPTR, #PATTERNS ; Point to the start of the patterns table
    MOV R0, #08          ; Set R0 to number of patterns (8)
MAIN_LOOP:
    CLR A                 ; Clear accumulator
    MOVC A, @A+DPTR      ; Load pattern from lookup table into accumulator
    MOV P1, A            ; Output the pattern to Port 1 (LEDs connected here)
    ACALL DELAY          ; Call delay subroutine
    INC DPTR             ; Move to the next pattern in the table
    DJNZ R0, MAIN_LOOP   ; Decrement R0 and repeat if not zero
    SJMP START           ; Repeat the main loop indefinitely
DELAY:  
    MOV R1, #DELAY_COUNT ; Load delay count into R1
DELAY_LOOP:
    DJNZ R1, DELAY_LOOP  ; Decrement R1 until it reaches zero
    RET                   ; Return from delay subroutine
END                     ; End of program