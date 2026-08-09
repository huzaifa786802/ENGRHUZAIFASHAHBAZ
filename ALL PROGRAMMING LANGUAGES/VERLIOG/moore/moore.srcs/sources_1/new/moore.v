`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/16/2024 09:10:56 AM
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


module moore(
input x,
input clock;
input reset;
output reg y
);
reg [1:0] Next_state;
parameter s0=2'b00,s1==2'b01,s2=2'b10;
always @(posedge clock)
begin
if (reset)
begin
Next_state=s0;
y=1'b0;
end
case(Next_state)
s0:begin
y=1'b0;
if(x)
Next_state=s0;
else:
Next_state=s1;
end
s1:begin
y=1'b0;
if(x)
Next_state=s2;
else
Next_sate=s1;
end
s2:begin
y=1'b1;
if(x)
Next_state=s0;
else
Next_State=s1;
end
endcase
end
endmodule