`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/04/2024 09:31:09 AM
// Design Name: 
// Module Name: upcounter_testbench
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


module upcounter_testbench();
    reg clk,reset;
    wire[1:0] counter;
    counter dut(clk,reset,counter);
    initial
    begin
    clk=0;
    forever #5 clk=~clk;
    end
    initial
    begin
    reset=0;
    #10 reset=1;
    #1 reset=0;
    end
endmodule