`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06/13/2024 10:00:56 AM
// Design Name: 
// Module Name: vending_machine_tb
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

module vending_machine_tb();
reg clk;
    reg reset;
    reg [7:0] coin;
    reg select_product;
    wire [3:0] dispense;
    wire [7:0] change;
    // Instantiate the vending machine
    vending_machine uut (
        .clk(clk),
        .reset(reset),
        .coin(coin),
        .select_product(select_product),
        .dispense(dispense),
        .change(change)
    );
    // Clock generation
    initial begin
        clk = 0;
        forever #5 clk = ~clk; // 10 ns clock period
    end

    // Test sequence
    initial begin
        // Initialize signals
        reset = 1;
        coin = 0;
        select_product = 0;
        #10;

        // Reset the vending machine
        reset = 0;
        #10;
        reset = 1;
        #10;
        reset = 0;

        // Test case 1: Insert 20 rupees and select the first product (cost 15 rupees)
        coin = 20;
        #10;
        select_product = 1; // Select the first product
        #10;
        select_product = 0; // De-select the product to simulate button press
        #20;

        // Check the output
        if (dispense != 4'b0001 || change != 5) begin
            $display("Test case 1 failed");
        end else begin
            $display("Test case 1 passed");
        end
        // Reset the vending machine
        reset = 1;
        #10;
        reset = 0;
        // Test case 2: Insert 50 rupees and select the second product (cost 30 rupees)
        coin = 50;
        #10;
        select_product = 1; // Select the second product
        #10;
        select_product = 0; // De-select the product to simulate button press
        #20;
        // Check the output
        if (dispense != 4'b0010 || change != 20) begin
            $display("Test case 2 failed");
        end else begin
            $display("Test case 2 passed");
        end
        // Reset the vending machine
        reset = 1;
        #10;
        reset = 0;
        // Test case 3: Insert 70 rupees and select the fourth product (cost 70 rupees)
        coin = 70;
        #10;
        select_product = 1; // Select the fourth product
        #10;
        select_product = 0; // De-select the product to simulate button press
        #20;

        // Check the output
        if (dispense != 4'b1000 || change != 0) begin
            $display("Test case 3 failed");
        end else begin
            $display("Test case 3 passed");
        end

        // Reset the vending machine
        reset = 1;
        #10;
        reset = 0;
        // Test case 4: Insert 60 rupees and select the third product (cost 55 rupees)
        coin = 60;
        #10;
        select_product = 1; // Select the third product
        #10;
        select_product = 0; // De-select the product to simulate button press
        #20;
        // Check the output
        if (dispense != 4'b0100 || change != 5) begin
            $display("Test case 4 failed");
        end else begin
            $display("Test case 4 passed");
        end
        // Test completed
        $finish;
    end
endmodule
