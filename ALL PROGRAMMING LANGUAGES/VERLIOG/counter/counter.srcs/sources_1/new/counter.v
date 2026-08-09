`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/04/2024 09:43:18 AM
// Design Name: 
// Module Name: counter
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


module counter(
    input clk,
    input reset,
    output [N-1 :0]counter
    );
    reg [1:0] out;
    always @(posedge clk or posedge reset)
    begin
    if(reset)
    begin
    out <=2'b00;
    end
    else 
    begin
    if(DOWN)
    out <= out- 2'b01;
    else
    out <= out+ 2b'01;
    end
endmodule