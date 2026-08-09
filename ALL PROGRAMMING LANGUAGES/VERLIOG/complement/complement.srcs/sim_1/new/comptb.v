`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/13/2024 10:01:07 PM
// Design Name: 
// Module Name: comptb
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
module comptb();
reg a,b,c;
wire d,e,f;
complement obj(a,b,c,d,e,f);
initial
begin
a=0;b=0;c=0;
#50 a=0;b=0;c=1;
#50 a=0;b=1;c=0;
#50 a=0;b=1;c=1;
#50 a=1;b=0;c=0;
#50 a=1;b=0;c=1;
#50 a=1;b=1;c=0;
#50 a=1;b=1;c=1;
end
endmodule