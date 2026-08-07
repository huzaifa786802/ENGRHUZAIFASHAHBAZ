;Name: Switch to LED Control
;Description: Turns on the rightmost LED by pressing the leftmost switch, and so on.

org 0000h
ljmp main

org 0030h
main:
    mov P1, #0FFh ; Initialize all LEDs to off
    mov R0, #0    ; Initialize switch counter
    
loop:
    jb P3.0, nopress ; Check if switch is pressed
    mov A, P1       ; Get current LED state
    rl A            ; Rotate left (shift right)
    mov P1, A       ; Update LED state
    inc R0          ; Increment switch counter

nopress:
    sjmp loop       ; Loop back

end