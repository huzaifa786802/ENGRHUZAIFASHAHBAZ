MOV TMOD, #20H       ; Timer1 in Mode 2 (8-bit auto-reload)
MOV TH1, #-3         ; Baud rate = 9600 for 11.0592 MHz crystal
MOV SCON, #50H       ; Configure UART in Mode 1 (8-bit UART), REN = 1
SETB TR1             ; Start Timer1

AGAIN: 
       MOV A, #'H'   ; Load 'H' into Accumulator
       ACALL TRANS   ; Transmit 'H'
       MOV A, # 'U'   ; Load 'U' into Accumulator
       ACALL TRANS   ; Transmit 'U'
       MOV A, # 'Z'   ; Load 'Z' into Accumulator
       ACALL TRANS   ; Transmit 'Z'
       MOV A, # 'A'   ; Load 'A' into Accumulator
       ACALL TRANS   ; Transmit 'A'
       MOV A, # 'I'   ; Load 'I' into Accumulator
       ACALL TRANS   ; Transmit 'I'
       MOV A, #'F'   ; Load 'F' into Accumulator
       ACALL TRANS   ; Transmit 'F'
       MOV A, #'A'   ; Load 'A' into Accumulator
       ACALL TRANS   ; Transmit 'A'
       SJMP AGAIN    ; Repeat the sequence

TRANS:
       MOV SBUF, A   ; Move Accumulator data to SBUF for transmission
HERE:  JNB TI, HERE  ; Wait for the Transmission Interrupt (TI) flag
       CLR TI        ; Clear the TI flag for the next transmission
       RET           ; Return to the main program
       
END
