`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/26/2024 11:43:53 AM
// Design Name: 
// Module Name: testnotgate
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
module testnotgate();
reg a,b,c,d;
wire e;
nots notgate(a,b,c,d,e);
initial
begin
a=0;b=0;c=0;d=0
#50 a=0;b=0;c=0;d=1;
#50 a=0;b=0;c=1;d=0;
#50 a=0;b=0;c=1;d=1;
#50 a=0;b=1;c=0;d=0;
#50 a=0;b=1;c=0;d=1;
#50 a=0;b=1;c=1;d=1;
#50 a=1;b=0;c=0;d=0;
#50 a=1;b=0;c=0;d=1;
#50 a=1;b=0;c=1;d=1;
#50 a=1;b=1;c=1;d=1;
end
endmodule