`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/06/2024 02:18:43 PM
// Design Name: 
// Module Name: mealy
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


module mealy_behavioral (
    input din,
    input clk,
    input reset,
    output reg y
    );
    
    reg [1:0] cst, nst;
    parameter S0 = 2'b00,
              S1 = 2'b01,
              S2 = 2'b10,
              S3 = 2'b11;
              
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            cst <= S0;
        end
        else begin
            cst <= nst;
        end
    end

    always @(cst or din) begin
        case (cst)
            S0: begin
                    if (din == 1'b1) begin
                        nst = S1;
                        y = 1'b0;
                    end
                    else begin
                        nst = cst;
                        y = 1'b0;
                    end
                end
            S1: begin
                    if (din == 1'b0) begin
                        nst = S2;
                        y = 1'b0;
                    end
                    else begin
                        y = 1'b0;
                        nst = cst;
                    end
                end
            S2: begin
                    if (din == 1'b1) begin
                        nst = S3;
                        y = 1'b0;
                    end
                    else begin
                        nst = S0;
                        y = 1'b0;
                    end
                end
            S3: begin
                    if (din == 1'b0) begin
                        nst = S0;
                        y = 1'b1;
                    end
                    else begin
                        nst = S1;
                        y = 1'b0;
                    end
                end
            default: nst = S0;
        endcase
    end
    
endmodule
                                                                                                       