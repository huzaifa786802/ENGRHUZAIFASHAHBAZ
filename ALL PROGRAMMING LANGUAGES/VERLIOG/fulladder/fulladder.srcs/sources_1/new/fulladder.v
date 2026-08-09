`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/21/2024 09:27:54 AM
// Design Name: 
// Module Name: fulladder
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


module fulladder(
    input switch1,
    input switch2,
    input switch3,
    output led1,
    output led2
    );
    always @(switch1 or switch2 or switch3)
    begin
    assign led1=switch1*switch2*switch3;
    assign led2=switch1&switch2&switch3;
    end
endmodule
