`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/26/2024 11:42:14 AM
// Design Name: 
// Module Name: not
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
module notgate(
    input a,
    input b,
    input c,
    input d,
    output e
    );
    not a1(e,a,b,c,d);
endmodule