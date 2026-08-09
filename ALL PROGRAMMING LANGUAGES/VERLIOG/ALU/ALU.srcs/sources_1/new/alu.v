`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/04/2024 10:26:30 AM
// Design Name: 
// Module Name: alu
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
module ALU #(parameter N = 0)
  (
   input [31:0] operand1,
   input [31:0] operand2,
   input [1:0] operation,
   output reg [31:0] result,
   output reg zero_flag
   );
   always @(*) begin
      case(N)
         0: result = operand1 + operand2; // Addition
         1: result = operand1 - operand2; // Subtraction
         2: begin // Logic gates
               case(operation)
                  2'b00: result = operand1 & operand2; // AND
                  2'b01: result = operand1 | operand2; // OR
                  2'b10: result = operand1 ^ operand2; // XOR
                  2'b11: result = ~(operand1 & operand2); // NAND
               endcase
            end
         default: result = operand1 + operand2; // Default to addition
      endcase
   end
   // Set zero flag if result is zero
   always @(result) begin
      if (result == 0)
         zero_flag = 1;
      else
         zero_flag = 0;
   end
endmodule