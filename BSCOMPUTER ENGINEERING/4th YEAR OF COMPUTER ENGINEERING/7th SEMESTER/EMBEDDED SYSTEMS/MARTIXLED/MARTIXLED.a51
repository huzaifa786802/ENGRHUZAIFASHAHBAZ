        ORG     000H

START:  CLR     P1.7
        MOV     R0,#64
        MOV     P2,#0FFH
        MOV     A,#80H

NEXT_COL:
        MOV     P0,A
        CALL    DELAY
        RR      A
        DJNZ    R0,NEXT_COL

        MOV     R0,#64
        MOV     P0,#0FFH
        MOV     A,#80H

NEXT_ROW:
        MOV     P2,A
        CALL    DELAY
        RR      A
        DJNZ    R0,NEXT_ROW

        JMP     START

;===========================================================
; DELAY 0.1S
;===========================================================

DELAY:  MOV     R6,#200

DL1:    MOV     R7,#249
        DJNZ    R7,$
        DJNZ    R6,DL1
        RET
        END
