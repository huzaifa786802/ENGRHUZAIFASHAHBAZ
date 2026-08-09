`//timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/21/2024 09:23:49 AM
// Design Name: 
// Module Name: halfadder
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
module halfadder(
    input switch1,
    input switch2,
    output led1,
    output led2
    );
    always @(switch1,switch2)
    begin
    assign led1=switch1*switch2;
    assign led2=switch1&switch2;
    end
endmodule