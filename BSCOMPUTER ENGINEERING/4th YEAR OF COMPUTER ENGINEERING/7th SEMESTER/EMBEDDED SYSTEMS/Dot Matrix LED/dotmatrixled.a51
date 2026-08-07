ORG 0000H          
MOV P1, #0FFH   
MOV P2, #00H    
A_PATTERN: DB 0x18, 0x3C, 0x66, 0xC3, 0xFF, 0xC3, 0xC3, 0xC3
MAIN:           ; Main loop to continuously display the letter
    MOV R0, #A_PATTERN    
DISPLAY:
    MOV R1, #08H          
DISPLAY_ROW:
    MOV A, @R0            
    MOV P1, A             
    MOV A, R1             
    CPL A                 
    MOV P2, A             
    ACALL DELAY           
    INC R0                
    MOV A, R1
    RL A                  
    MOV R1, A             
    DJNZ R1, DISPLAY_ROW  
    SJMP MAIN             
DELAY:
    MOV R2, #255
DELAY_LOOP1:
    DJNZ R2, DELAY_LOOP1
    MOV R2, #255
DELAY_LOOP2:
    DJNZ R2, DELAY_LOOP2
    RET
END