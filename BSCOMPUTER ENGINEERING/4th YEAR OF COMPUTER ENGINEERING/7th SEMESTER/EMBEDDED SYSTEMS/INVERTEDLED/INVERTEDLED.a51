; 8051 Assembly Code to Sequentially Blink Two LEDs
; LEDs connected to P1.0 and P1.1

ORG 00H          ; Origin, start of the program

START: 
    MOV P1, #00H ; Initialize Port 1 (turn off both LEDs)

MAIN: 
    ; Turn on LEDs from ends towards the middle
    MOV A, #01H   ; Start with LED at P1.0
    MOV P1, A     ; Output to Port 1

    ACALL DELAY   ; Call delay
    MOV A, #02H   ; Next LED at P1.1
    MOV P1, A     ; Output to Port 1

    ACALL DELAY   ; Call delay

    ; Invert sequence after reaching the middle
    MOV A, #01H   ; Reset to LED at P1.0
    MOV P1, A     ; Output to Port 1

    ACALL DELAY   ; Call delay
    MOV A, #00H   ; Turn off both LEDs
    MOV P1, A     ; Output to Port 1

    ACALL DELAY   ; Call delay

    SJMP MAIN     ; Repeat the sequence

DELAY: 
    MOV R0, #255  ; Outer loop counter
DELAY_LOOP:
    MOV R1, #255  ; Inner loop counter
INNER_LOOP:
    DJNZ R1, INNER_LOOP ; Decrement and loop if not zero
    DJNZ R0, DELAY_LOOP  ; Decrement outer loop and repeat if not zero
    RET             ; Return from subroutine

END                ; End of program