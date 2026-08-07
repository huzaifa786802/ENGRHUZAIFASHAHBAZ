;**************************************
; 8051 Assembly Program for Sequential Display
; Displays numbers 90 to 09 on DS3 (decrementing)
; and 09 to 90 on DS4 (incrementing)
; Each number stays for 0.5 seconds
;**************************************

ORG 0000H
    LJMP MAIN        ; Jump to main program

ORG 0030H
MAIN:
    ; Initialize port configuration
    MOV P1, #00H     ; Clear Port 1 (assuming DS3 and DS4 are on Port 1)
    MOV P2, #00H     ; Clear Port 2 for additional control if needed

    ; Initialize registers for display
    MOV R2, #90D     ; Starting value for DS3 (decrementing)
    MOV R3, #09D     ; Starting value for DS4 (incrementing)

DISPLAY_LOOP:
    ; Display on DS3 (decrementing)
    MOV A, R2        ; Move current value to Accumulator
    ACALL DISPLAY    ; Call display subroutine
    
    ; Display on DS4 (incrementing)
    MOV A, R3        ; Move current value to Accumulator
    ACALL DISPLAY    ; Call display subroutine
    
    ; Delay for 0.5 seconds
    ACALL DELAY_500MS
    
    ; Decrement DS3 value
    DEC R2           ; Decrement R2
    
    ; Increment DS4 value
    INC R3           ; Increment R3
    
    ; Check if we need to reset values
    MOV A, R2        ; Check DS3 value
    CJNE A, #08H, CONTINUE_LOOP  ; If not reached 08, continue
    MOV R2, #90D     ; Reset DS3 to 90
    
    MOV A, R3        ; Check DS4 value
    CJNE A, #91H, CONTINUE_LOOP  ; If not reached 91, continue
    MOV R3, #09D     ; Reset DS4 to 09

CONTINUE_LOOP:
    SJMP DISPLAY_LOOP  ; Repeat the loop

;**************************************
; DISPLAY Subroutine
; Displays the value in Accumulator
;**************************************
DISPLAY:
    ; Conversion and display logic goes here
    ; This is a placeholder - actual implementation 
    ; depends on your specific display setup
    MOV P1, A        ; Simple display on Port 1
    RET

;**************************************
; DELAY Subroutine
; Creates a 0.5 second delay
; Note: Delay calculation depends on 
; microcontroller clock frequency
;**************************************
DELAY_500MS:
    ; Delay calculation example for 12 MHz crystal
    ; Adjust these nested loops based on your specific clock
    MOV R6, #250     ; Outer loop counter
OUTER_LOOP:
    MOV R7, #250     ; Inner loop counter
INNER_LOOP:
    DJNZ R7, INNER_LOOP  ; Decrement inner loop
    DJNZ R6, OUTER_LOOP  ; Decrement outer loop
    RET
END