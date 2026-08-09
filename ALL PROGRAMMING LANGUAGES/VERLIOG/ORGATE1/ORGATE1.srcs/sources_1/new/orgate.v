`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/25/2024 10:31:26 AM
// Design Name: 
// Module Name: orgate
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


module orgate(
    input LED1,
    input LED2,
    input LED3,
    input LED4,
    output Switch1
    );
or (Switch1,LED1,LED2,LED3,LED4);
endmodule

/*module orgate(a,b,c,d,e);
input a;
input b;
input c;
input d;
output e;
reg a,b,c,d;
wire e;
or (e,a,b,c,d);
endmodule*/ 