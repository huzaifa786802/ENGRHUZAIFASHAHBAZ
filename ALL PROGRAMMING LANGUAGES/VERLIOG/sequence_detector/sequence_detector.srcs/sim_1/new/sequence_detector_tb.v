`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/06/2024 02:36:08 PM
// Design Name: 
// Module Name: sequence_detector_tb
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
`timescale 1ns/1ps

module sequence_detector_tb;

    // Parameters
    parameter CLK_PERIOD = 10; // Clock period in ns

    // Inputs
    reg clk;
    reg reset;
    reg data;

    // Outputs
    wire detected;
    sequence_detector uut (
        .clk(clk),
        .reset(reset),
        .data(data),
        .detected(detected)
    );

    // Clock generation
    always #((CLK_PERIOD/2)) clk = ~clk;
    // Stimulus generation
    initial 
    begin
        clk = 0;
        reset = 1;
        data = 0;

        // Wait for reset to settle
        #20;

        // Release reset
        reset = 0;

        // Non-overlapping case
        $display("Non-overlapping case:");
        #10; data = 1;
        #10; data = 1;
        #10; data = 0;
        #10; data = 1;
        #10; data = 1;
        #10; data = 0;
        #10; data = 0;
        #10; data = 1;
        #10; data = 1;
        #10; data = 1; // Detected at this point
        #10; data = 0;
        #10; data = 1;
        #10; data = 0;
        #10; data = 1;
        // Reset for the next case
        #20;
        reset = 1;
        #20;
        reset = 0;

        // Overlapping case
        $display("\nOverlapping case:");
        #10; data = 1;
        #10; data = 1;
        #10; data = 0;
        #10; data = 1;
        #10; data = 1; // Detected at this point
        #10; data = 1;
        #10; data = 0;
        #10; data = 1;
        #10; data = 1;
        #10; data = 0;
        #10; data = 1;
        // End simulation
        #100;
        $finish;
    end
endmodule
