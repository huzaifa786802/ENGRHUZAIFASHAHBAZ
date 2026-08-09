`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/14/2024 05:43:41 AM
// Design Name: 
// Module Name: fatestbench
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


module fatestbench();
reg a,b,cin;
wire carry,sum;
fa obj(a,b,cin,sum,carry);
initial
begin
a=0;b=0;cin=0;
#50 a=0;b=0;cin=1;
#50 a=0;b=1;cin=0;
#50 a=0;b=1;cin=1;
#50 a=1;b=0;cin=0;
#50 a=1;b=0;cin=1;
#50 a=1;b=1;cin=0;
#50 a=1;b=1;cin=1;
end
endmodule