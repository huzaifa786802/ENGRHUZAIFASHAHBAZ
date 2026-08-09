`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/06/2024 02:32:56 PM
// Design Name: 
// Module Name: sequence_detector
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


module sequence_detector(
    input clk,
    input reset,
    input data,
    output reg detected
    );
    parameter IDLE = 2'b00;
    parameter STATE1 = 2'b01;
    parameter STATE2 = 2'b10;
    parameter STATE3 = 2'b11;
    reg [1:0] state, next_state;
    always @(posedge clk or posedge reset) begin
        if (reset) 
        begin
            state <= IDLE;
        end 
        else 
        begin
            state <= next_state;
        end
    end
    always @(*) begin
        case(state)
            IDLE: begin
                if (data)
                 begin
                    next_state = STATE1;
                end 
                else 
                begin
                    next_state = IDLE;
                end
                detected = 0;
            end
            STATE1: begin
                if (data) begin
                    next_state = STATE2;
                end else begin
                    next_state = IDLE;
                end
                detected = 0;
            end
            STATE2: begin
                if (data) begin
                    next_state = STATE3;
                end else begin
                    next_state = IDLE;
                end
                detected = 0;
            end
            STATE3: begin
                if (data) begin
                    next_state = STATE2;
                    detected = 0;
                end else begin
                    next_state = STATE1;
                    detected = 0;
                end
                if (state == STATE2 && data) begin
                    detected = 1;
                end
            end
        endcase
    end
    endmodule