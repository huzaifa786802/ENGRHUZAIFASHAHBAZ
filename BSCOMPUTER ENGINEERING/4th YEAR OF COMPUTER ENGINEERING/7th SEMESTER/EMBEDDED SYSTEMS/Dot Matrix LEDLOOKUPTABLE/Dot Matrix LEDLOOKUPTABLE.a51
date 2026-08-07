; 8051 Assembly Program to Display First Alphabets on Dot Matrix LED
; Using Table Lookup Method with Delay and Repetition Technique
    ORG 0000H
    LJMP MAIN        ; Jump to main program
; Dot Matrix LED Column Display Table for First Alphabets
ALPHABET_TABLE:
    ; 5-column patterns for first alphabets (example patterns)
    ; Each byte represents one column of the character
    ; A pattern
    DB 07H, 05H, 05H, 05H, 07H
    ; B pattern
    DB 07H, 05H, 07H, 05H, 07H
    ; S pattern
    DB 07H, 04H, 07H, 01H, 07H
; 5ms Delay Subroutine
DELAY_5MS:
    MOV R7, #20
DELAY_LOOP1:
    MOV R6, #250
DELAY_LOOP2:
    DJNZ R6, DELAY_LOOP2
    DJNZ R7, DELAY_LOOP1
    RET
; Display Character Subroutine
; Input: DPTR points to character pattern, R2 = column counter
DISPLAY_CHAR:
    MOV R3, #20      ; Display character 20 times (0.5 seconds)
REPEAT_CHAR:
    MOV R2, #5       ; 5 columns to display
COLUMN_LOOP:
    ; Get column pattern
    MOV A, R2
    DEC A            ; Adjust for 0-based indexing
    MOVC A, @A+DPTR  ; Get column pattern from table
    ; Display column
    MOV P1, A        ; Output to LED
    ACALL DELAY_5MS  ; 5ms delay for column display
    ; Next column
    DJNZ R2, COLUMN_LOOP
    ; Repeat character display
    DJNZ R3, REPEAT_CHAR
    RET
; Main Program
MAIN:
    ; Initialize Port
    MOV P1, #00H     ; Clear Port 1 (Dot Matrix LED)
    ; Display First Alphabets
    ; A
    MOV DPTR, #ALPHABET_TABLE    ; Point to start of table
    ACALL DISPLAY_CHAR           ; Display 'A'
    ; B - Move DPTR to B pattern
    MOV DPTR, #ALPHABET_TABLE+5  ; Skip 5 bytes to B pattern
    ACALL DISPLAY_CHAR           ; Display 'B'
    ; S - Move DPTR to S pattern
    MOV DPTR, #ALPHABET_TABLE+10 ; Skip 10 bytes to S pattern
    ACALL DISPLAY_CHAR           ; Display 'S'
    ; Clear display
    MOV P1, #00H
; Infinite loop to stop program
STOP:
    SJMP STOP
    END