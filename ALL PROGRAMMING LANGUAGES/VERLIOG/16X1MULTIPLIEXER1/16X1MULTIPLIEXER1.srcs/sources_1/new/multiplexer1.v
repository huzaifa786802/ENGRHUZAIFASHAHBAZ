`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/25/2024 11:10:49 AM
// Design Name: 
// Module Name: multiplexer1
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


module multiplexer1(
    input a[16:1],
    output S0,
    output S1
    );
 and (S0,a[16:0]);
 nor(S1,a[16:0)]
endmodule
