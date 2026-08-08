`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06/13/2024 10:13:54 AM
// Design Name: 
// Module Name: vending_machine
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

module vending_machine(
    input clk,
    input reset,
    input [7:0] coin,
    input select_product,
    output reg [3:0] dispense,
    output reg [7:0] change
    );
    state_t current_state, next_state;
    parameter PRICE1 = 15;
    parameter PRICE2 = 30;
    parameter PRICE3 = 55;
    parameter PRICE4 = 70;
    reg [7:0] total_amount;
    reg [1:0] product_selection;
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            current_state <= IDLE;
            total_amount <= 0;
            product_selection <= 0;
            dispense <= 4'b0000;
            change <= 0;
        end else begin
            current_state <= next_state;
        end
    end
    always @(*) begin
        next_state = current_state; 
        dispense = 4'b0000;  
       change = 0; 
        case (current_state)
            IDLE: begin
                if (coin > 0) begin
                    next_state = WAIT_FOR_PRODUCT;
                end
            end
            WAIT_FOR_PRODUCT: begin
                if (select_product) begin
                    if (total_amount >= PRICE1 && product_selection == 2'b00) begin
                        next_state = DISPENSE_PRODUCT;
                        dispense[0] = 1;
                    end else if (total_amount >= PRICE2 && product_selection == 2'b01) begin
                        next_state = DISPENSE_PRODUCT;
                        dispense[1] = 1;
                    end else if (total_amount >= PRICE3 && product_selection == 2'b10) begin
                        next_state = DISPENSE_PRODUCT;
                        dispense[2] = 1;
                    end else if (total_amount >= PRICE4 && product_selection == 2'b11) begin
                        next_state = DISPENSE_PRODUCT;
                        dispense[3] = 1;
                    end
                end
            end
            DISPENSE_PRODUCT: begin
                if (dispense[0]) begin
                    change = total_amount - PRICE1;
                end else if (dispense[1]) begin
                    change = total_amount - PRICE2;
                end else if (dispense[2]) begin
                    change = total_amount - PRICE3;
                end else if (dispense[3]) begin
                    change = total_amount - PRICE4;
                end
                next_state = RETURN_CHANGE;
            end
            RETURN_CHANGE: begin
                total_amount = 0; 
                next_state = IDLE; 
            end
        endcase
    end
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            total_amount <= 0;
        end else if (current_state == IDLE && coin > 0) begin
            total_amount <= coin;
        end
    end
    always @(posedge clk or posedge reset) 
    begin
        if (reset) begin
            product_selection <= 0;
        end else if (select_product) begin
            product_selection <= product_selection + 1;
        end
    end
endmodule