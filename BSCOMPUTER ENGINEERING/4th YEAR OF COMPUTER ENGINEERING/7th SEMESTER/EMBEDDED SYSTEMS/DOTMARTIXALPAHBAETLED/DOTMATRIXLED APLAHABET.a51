ORG 0000H
PATTERN: DB 3CH, 66H, 66H, 7EH, 66H, 66H, 66H, 00H
ROW_SELECT: DB 0FEH, 0FDH, 0FBH, 0F7H, 0EFH, 0DFH, 0BFH, 0FFH
MOV DPTR, #PATTERN   
MOV P0, #0FFH        
MOV P2, #0FFH        ; Clear Port 2 (connected to rows)

MAIN_LOOP:
    MOV R0, #08      ; Loop counter for 8 rows

DISPLAY_LOOP:
    MOVX A, @DPTR    ; Load row data from pattern
    MOV P2, A        ; Output row data to Port 2 (74LS245 for rows)

    MOV A, R0
    DEC A            ; Convert R0 to match row index (0-7)
    MOVC A, @A+ROW_SELECT ; Get row selection value from ROW_SELECT
    MOV P0, A        ; Output to Port 0 (ULN2803 for columns)

    ACALL DELAY      ; Call delay for stable display

    INC DPTR         ; Move to next row in the pattern
    DJNZ R0, DISPLAY_LOOP ; Repeat for all rows

    MOV DPTR, #PATTERN ; Reset DPTR to start of pattern
    SJMP MAIN_LOOP     ; Repeat the main loop indefinitely

; Simple delay subroutine
DELAY:
    MOV R1, #0FFH
    MOV R2, #0FFH
DELAY_LOOP:
    DJNZ R2, DELAY_LOOP
    DJNZ R1, DELAY_LOOP
    RET
END