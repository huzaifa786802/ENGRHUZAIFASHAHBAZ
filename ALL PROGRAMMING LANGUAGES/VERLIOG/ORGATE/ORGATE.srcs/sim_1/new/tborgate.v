`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/26/2024 11:24:51 AM
// Design Name: 
// Module Name: tborgate
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
module tborgate();
  reg a, b;
  wire c;
  or_gate_s uut(a, b, c);
  initial 
  begin
  a=0;b=0; 
#50 a=0;b=1;
#50 a=1;b=0;
#50 a=1;b=1;
end
endmodule