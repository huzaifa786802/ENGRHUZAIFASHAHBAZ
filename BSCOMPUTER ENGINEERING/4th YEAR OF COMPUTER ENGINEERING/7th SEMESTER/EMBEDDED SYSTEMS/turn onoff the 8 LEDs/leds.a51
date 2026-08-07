ORG 0000H         ; Start at address 0
MOV P1, #00H      ; Clear all LEDs initially (assuming LEDs are connected to Port 1)
MOV R0, #08H      ; Counter for 8 LEDs

MAIN: 
    MOV A, #01H   ; Initialize with leftmost LED (binary 00000001)
    MOV R1, #08H  ; Load the loop count for 8 LEDs
LOOP:
    MOV P1, A     ; Output current LED state to Port 1
    ACALL DELAY   ; Delay for 0.1 seconds
    RL A          ; Rotate left to shift the bit to the next LED
    DJNZ R1, LOOP ; Decrement R1, repeat for 8 LEDs
    SJMP MAIN     ; Jump back to start for continuous operation
DELAY:            ; 0.1-second delay subroutine (approximate)
    MOV R2, #250
DELAY_LOOP1:
    MOV R3, #250
DELAY_LOOP2:
    DJNZ R3, DELAY_LOOP2
    DJNZ R2, DELAY_LOOP1
    RET
END