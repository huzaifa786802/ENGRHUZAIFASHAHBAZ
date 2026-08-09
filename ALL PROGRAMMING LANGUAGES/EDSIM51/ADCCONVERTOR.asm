ORG 0000H
MOV P1,#0FFH; Set Port 1 as input port (for ADC data)
MOV P2,#00H; Set Port 2 as output port (for control signals)
CALL INIT_LCD;Initialize the LCD
START:
SETB P2.0;SEND HIGH TO START CONVERSION(SC PIN)
CLR P2.0;SEND LOW TO STOP CONVERSION
JB P2.1,START;WAIT UNIT END OF CONVERSION(EOC PIN)
MOV A,P1;READ DIGITAL VALUE FROM ADC(8-BIT)
CALL DISPLAY;SEND  VALUE TO LCD DISPLAY
SJMP START;REPEAT FOREVER
DISPLAY:
;Code to display the value on LCD (implement your own LCD routine)
RET
INIT_LCD:
; Code to initialize LCD (implement your own LCD routine)
RET
END