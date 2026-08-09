`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/21/2024 10:04:42 AM
// Design Name: 
// Module Name: 2bitadders
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


module 2bitadders(
    input switch1,
    input switch2,
    input switch3,
    input switch4,
    output led1,
    output led2,
    output led3,
    output led4
    );
    always@(switch1 or switch2 or switch3 or switch4)
    begin
    assign led1=switch1*switch2;
    assign led2=switch1&switch2;
    assign led3=switch3*switch4*led2;
    assign led4=led2&(switch1*switch4)|(switch3&switch4);
    end
endmodule