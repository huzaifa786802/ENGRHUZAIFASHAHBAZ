`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/25/2024 10:10:26 AM
// Design Name: 
// Module Name: multiplexertesbench
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


module multiplexertesbench();
reg a,b,c,d;
wire S0,S1;
initial
begin
a=16b'00;
#50 a=16b'01;
#50 a=16b'10;
#50 a=16b'11;
end
endmodule