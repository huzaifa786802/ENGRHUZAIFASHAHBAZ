ORG 0000H                    ; Start of the code at address 0000H

MOV SP, #60                  
CLR P1.7                     
CALL LCMINIT                 
MOV A, #10000000B            
CALL WRINS                    
MOV DPTR, #LINE               
CALL PRTSTR                   
MAIN_LOOP:
    CALL PRTSTR               
    CALL DELAY_500MS           
    CLR P1.5
    CLR P1.6
    CLR P1.7
    CALL DELAY_500MS       
    JMP MAIN_LOOP          
WRINS:
    CALL CHKBSY                
    CLR P1.5                   
    CLR P1.6                   
    SETB P1.7                  
    MOV P0, A                  
    CLR P1.7                   
    RET
WRDATA:
    CALL CHKBSY                
    SETB P1.5                  
    CLR P1.6                   
    SETB P1.7                  
    MOV P0, A                  
    CLR P1.7                   
    RET
CHKBSY:
    MOV P0, #0FFH              
    CLR P1.5                   
    SETB P1.6                  
    SETB P1.7                  
    MOV C, P0.7                
    CLR P1.7                   
    JC CHKBSY                  
    RET
LCMINIT:
    MOV A, #00110000B         
    CALL WRINS
    MOV A, #00000001B         
    CALL WRINS
    MOV A, #00001100B         
    CALL WRINS
    MOV A, #00000110B         
    CALL WRINS
    RET
PRTSTR:
    MOV A, #0                  
    MOVC A, @A + DPTR          
    CJNE A, #'$', PRINT        
    RET                        
PRINT:
    CALL WRDATA                
    INC DPTR                   
    JMP PRTSTR                 
DELAY_500MS:
    MOV R6, #50                
DELAY_LOOP_500MS:
    MOV R7, #200               
DELAY_LOOP_200MS:
    DJNZ R7, DELAY_LOOP_200MS  
    DJNZ R6, DELAY_LOOP_500MS  
    RET
LINE: DB 'Hello! Welcome$'     
end