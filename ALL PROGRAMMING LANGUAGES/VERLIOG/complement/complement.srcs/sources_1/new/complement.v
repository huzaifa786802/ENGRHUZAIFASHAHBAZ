`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/13/2024 09:58:25 PM
// Design Name: 
// Module Name: complement
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
module complement(
    input a,
    input b,
    input c,
    output d,
    output e,
    output f
    );
    not n1(d,a);
    not n2(e,b);
    not n3(f,c);
endmodule