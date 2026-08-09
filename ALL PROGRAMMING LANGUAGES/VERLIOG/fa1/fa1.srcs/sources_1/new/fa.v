`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/14/2024 05:07:09 AM
// Design Name: 
// Module Name: fa
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


module fa(
    input a,
    input b,
    input cin,
    output sum,
    output carry
    );
    wire w1,w2,w3;
    xor x1(w1,a,b);
    xor x2(sum,w1,cin);
    and a1(w2,cin,w1);
    and a2(w3,a,b);
    or o1(carry,w2,w3);
endmodule