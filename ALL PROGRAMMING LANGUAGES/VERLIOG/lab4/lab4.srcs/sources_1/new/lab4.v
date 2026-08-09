`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/14/2024 09:49:14 AM
// Design Name: 
// Module Name: lab4
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


module lab4(
    input switch1,
    input switch2,
    input switch3,
    input switch4,
    output led1,
    output led2,
    output led3,
    output led4
    );
    assign led4=(switch1&~switch2) |(switch3&~switch4);
endmodule
