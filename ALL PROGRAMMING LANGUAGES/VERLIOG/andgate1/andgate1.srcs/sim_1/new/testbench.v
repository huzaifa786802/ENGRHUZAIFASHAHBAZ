`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/24/2024 11:48:20 PM
// Design Name: 
// Module Name: testbench
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


module testbench();
reg a,b;
wire c;
andgate and_gate_inst (a, b, y);
initial
begin
a=0;b=0;
#50 a=0;b=1;
#50 a=1;b=0;
#50 a=1;b=1;
end
endmodule
