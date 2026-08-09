`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/16/2024 09:43:40 PM
// Design Name: 
// Module Name: moore
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


module moore(clock,reset,sequence_in,detector_out);
input clock;
input reset;
input sequence_in;
output reg detector_out;
parameter Zero-3'b00,One=3'b001,OneZero=3'b011,OneZeroOne=3'b010,OneZeroOne=3'b110;
reg [2:0] current_state,next_state;
always @(posedge clock,posedge reset)
begin
if(reset==1)
current_state<=Zero;
else
current_state<=next_state;
end
always@(current_state,sequence_in)
begin
case(current_state)
Zero:begin
if(sequence_in==1)
next_state=One;
else
next_state=Zero;
end
One:begin
if(
endmodule
