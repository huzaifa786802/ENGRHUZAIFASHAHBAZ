`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06/13/2024 10:37:56 AM
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
    vending_machine uut (
        .clk(clk),
        .reset(reset),
        .coin(coin),
        .select_product(select_product),
        .dispense(dispense),
        .change(change)
    );
    initial 
    begin
        clk = 0;
        forever #5 clk = ~clk; 
    end
    initial 
    begin
        reset = 1;
        coin = 10;
        select_product = 0;    
        #10;
        reset = 0;
        #10;
        reset = 1;
        #10;
        reset = 0;
        coin = 20;
        #10;
        select_product = 1; 
        #10;
        select_product = 0; 
        #20;
        if (dispense !== 4'b0001 || change !== 5) 
        begin
            $display("Test case 1 failed");
        end 
        else 
        begin
            $display("Test case 1 passed");
        end
        reset = 1;
        #10;
        reset = 0;
        coin = 45;
        #10;
        select_product = 1; 
        #10;
        select_product = 0; 
        #20;
        if (dispense !== 4'b0010 || change !== 20) 
        begin
            $display("Test case 2 failed");
        end 
        else 
        begin
            $display("Test case 2 passed");
        end
        reset = 1;
        #10;
        reset = 0;
        coin = 75;
        #10;
        select_product = 1; 
        #10;
        select_product = 0; 
        #20;
        if (dispense !== 4'b1000 || change !== 0) begin
            $display("Test case 3 failed");
        end 
        else 
        begin
            $display("Test case 3 passed");
        end
        reset = 1;
        #10;
        reset = 0;
        coin = 60;
        #10;
        select_product = 1; 
        #10;
        select_product = 0; 
        #20;
        if (dispense !== 4'b0100 || change !== 5) 
        begin
            $display("Test case 4 failed");
        end 
        else 
        begin
            $display("Test case 4 passed");
        end
        $finish;
    end
endmodule