`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/16/2024 10:10:08 AM
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
    reg x;
    reg clock;
    reg reset;
    wire y;

    moore uut(
        .y(y),
        .x(x),
        .clock(clock),
        .reset(reset)
    );

    initial
    begin
        x = 0; clock = 1; reset = 1;
        #10 reset = 0;
        #10 x = 0;
        #10 x = 1;
        #10 x = 0;
        #10 x = 1;
        #10 x = 0;
        #10 x = 1;
        #100;
        $finish;
    end

endmodule