ORG 0000H            ; Start of code memory
START:
    MOV P1, #01H   ; Initialize the leftmost LED (bit 0 of Port 1)
    MOV R0, #01H   ; Set up the direction for the sequence (left to right)
LOOP:
    MOV P1, A      ; Update the Port 1 to the value of A register
    ACALL DELAY    ; Call the delay subroutine
    MOV A, P1      ; Load the current state of LEDs into A
    RLC A          ; Rotate left through carry (move to next LED in sequence)
    MOV P1, A      ; Update the Port 1 with the new value
    ACALL DELAY    ; Call the delay subroutine
    JNB P1.7, LOOP ; Jump back to LOOP if the rightmost LED is not reached
    ; Invert the direction (right to left)
    MOV P1, #80H   ; Set the rightmost LED
    MOV R0, #80H   ; Set up the direction for the sequence (right to left)
INVERT_LOOP:
    MOV P1, A      ; Update Port 1 with the current value
    ACALL DELAY    ; Call the delay subroutine
    MOV A, P1      ; Load the current state of LEDs into A
    RRC A          ; Rotate right through carry (move to previous LED in sequence)
    MOV P1, A      ; Update the Port 1 with the new value
    ACALL DELAY    ; Call the delay subroutine
    JNB P1.0, INVERT_LOOP ; Jump back to INVERT_LOOP if the leftmost LED is not reached
    ; Repeat the sequence
    SJMP LOOP      ; Jump back to the start of the loop
DELAY:
    MOV R1, #200   ; Outer loop count
DELAY1:
    MOV R2, #250   ; Inner loop count
DELAY2:
    NOP            ; No Operation (used for delay)
    NOP
    NOP
    NOP
    DJNZ R2, DELAY2 ; Decrement inner loop counter
    DJNZ R1, DELAY1 ; Decrement outer loop counter
    RET            ; Return from the delay subroutine
END