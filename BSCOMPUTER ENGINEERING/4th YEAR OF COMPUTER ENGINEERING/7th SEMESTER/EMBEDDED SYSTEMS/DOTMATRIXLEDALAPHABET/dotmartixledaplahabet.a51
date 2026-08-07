ORG 0000H             ; Starting address
; Define each letter pattern for Dot Matrix (example 5x7 font for A, B, etc.)
LETTER_A: DB 0x7E, 0x09, 0x09, 0x7E, 0x00  ; A
LETTER_B: DB 0x7F, 0x49, 0x49, 0x36, 0x00  ; B
LETTER_C: DB 0x3E, 0x41, 0x41, 0x22, 0x00  ; C
; Add more letters as needed
; Main program
MAIN: 
    MOV R0, #LETTER_A       ; Load letter A pattern
    CALL DISPLAY_LETTER
    CALL DELAY_500MS
    MOV R0, #LETTER_B       ; Load letter B pattern
    CALL DISPLAY_LETTER
    CALL DELAY_500MS
    MOV R0, #LETTER_C       ; Load letter C pattern
    CALL DISPLAY_LETTER
    CALL DELAY_500MS
    SJMP MAIN               ; Loop back to display letters again
; Subroutine to display letter on Dot Matrix
DISPLAY_LETTER:
    MOV R1, #5              ; 5 bytes per letter pattern
DISP_LOOP:
    MOV A, @R0              ; Move pattern byte to accumulator
    MOV P1, A               ; Send to Dot Matrix connected to Port 1
    INC R0                  ; Move to next byte in pattern
    DJNZ R1, DISP_LOOP      ; Repeat for all bytes in pattern
    RET
; Subroutine for 0.5-second delay
DELAY_500MS:
    MOV R2, #50             ; 50 x 10 ms = 500 ms
DELAY_LOOP:
    ACALL DELAY_10MS        ; Call 10 ms delay 50 times
    DJNZ R2, DELAY_LOOP
    RET
; Subroutine for 10 ms delay
DELAY_10MS:
    MOV R3, #200            ; Adjust as needed for 10 ms
DELAY_10MS_LOOP:
    NOP                     ; No operation (wastes time)
    DJNZ R3, DELAY_10MS_LOOP
    RET
END                         ; End of program