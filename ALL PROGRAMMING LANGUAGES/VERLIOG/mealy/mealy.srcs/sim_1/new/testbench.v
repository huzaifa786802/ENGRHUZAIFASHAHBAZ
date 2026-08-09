`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/06/2024 02:20:28 PM
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

module TestBench();
    reg sequence_in;
    reg clock;
    reg reset;
    // Outputs
    wire detector_out;
    // Instantiate the Mealy Machine
    mealy_behavioral uut (
        .din(sequence_in),
        .clk(clock),
        .reset(reset),
        .y(detector_out)
    );

    initial begin
        clock = 0;
        forever #5 clock = ~clock;
    end

    initial begin
        // Initialize Inputs
        sequence_in = 0;
        reset = 1;
        // Wait 100 ns for global reset to finish
        #100;
        reset = 0;
        #10;
        // Input sequence
        #10; sequence_in = 1;
        #10; sequence_in = 0;
        #10; sequence_in = 1;
        #30; sequence_in = 0;
        #10; sequence_in = 1;
        #10; sequence_in = 0;
        #10; sequence_in = 0;
        #10; sequence_in = 1;
        #10; sequence_in = 1;
        #10; sequence_in = 0;
        #10; sequence_in = 1;
        #10; sequence_in = 0;
        #10; sequence_in = 1;
        #10; sequence_in = 0;
    end
endmodule

