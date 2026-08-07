ORG 000H
SJMP START       ; Jump to start to avoid executing data

CLR P1.7         ; Clear P1.7 (optional)

START:
    MOV DPTR,#TABLE   ; Load address of the table
    MOV R2,#00000001B ; Start column selection from the first column (LSB)
    MOV R1,#0         ; Initialize row counter

NEXT:
    MOV A,R1
    MOVC A,@A+DPTR    ; Fetch row pattern from TABLE
    MOV P2,A          ; Send row pattern to P2 (row control)
    MOV A,R2
    MOV P0,A          ; Send column selection to P0
    CALL DELAY        ; Call delay to keep it visible
    RL A              ; Rotate left to shift column to the next
    MOV R2,A          ; Update column position
    INC R1            ; Move to the next row
    CJNE R1,#7,NEXT   ; Loop through all 7 rows

    JMP START         ; Restart displaying

;==============================
; DELAY 5mS
;==============================
DELAY:
    MOV R6,#10
DL1:
    MOV R7,#249
    DJNZ R7,$
    DJNZ R6,DL1
    RET

;==============================
TABLE: 
    DB 01111110B   ; Row 1
    DB 01000010B   ; Row 2
    DB 01110110B   ; Row 3
    DB 01010110B   ; Row 4
    DB 01010110B   ; Row 5
    DB 01000010B   ; Row 6
    DB 01000010B   ; Row 7
;==============================
END  ; End directive
