`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/03/2024 12:25:17 PM
// Design Name: 
// Module Name: CODE1
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module CODE1(
    input switch1,
    input switch2,
    output LED1,
    output LED2,
    output LED3,
    output LED4
    );
    wire x,y;
    not a(x,switch1);
    not b(y, switch2);
    and c(LED1,x,y);
    and d(LED2,x,switch2);
    and e(LED3,switch1,y);
    and f(LED4,switch1,switch2);
endmodule