`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/30/2024 10:38:54 AM
// Design Name: 
// Module Name: statemachine
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
//////////////////////////////////////////////////////////////////////////////////
module statemachine (
    input wire clk,       
    input wire reset,     
    input wire N_B,       
    input wire [3:0] speed,
    output reg gear_up,   
    output reg gear_down  
);
reg [1:0] current_gear; 
parameter NORMAL_GEAR1_MAX = 7'd20;
parameter NORMAL_GEAR2_MAX = 7'd45;
    parameter NORMAL_GEAR3_MAX = 7'd70;
    parameter BOAST_GEAR1_MAX = 7'd30;
    parameter BOAST_GEAR2_MAX = 7'd55;
    parameter BOAST_GEAR3_MAX = 7'd80;
    always @(posedge clk or posedge reset) begin
        if (reset) 
        begin
       current_gear <= 2'd0; 
            gear_up <= 1'b0;
            gear_down <= 1'b0;
        end 
        else 
        begin
       case (N_B)
       1'b0: 
       begin
      if (speed <= NORMAL_GEAR1_MAX) 
      begin
     if (current_gear != 2'd0) begin
     gear_down <= 1'b1;
     gear_up <= 1'b0;
     end
    current_gear <= 2'd0;
    end 
    else if (speed <= NORMAL_GEAR2_MAX) 
    begin
    if (current_gear != 2'd1) 
    begin
gear_up <= (current_gear < 2'd1);
gear_down <= (current_gear > 2'd1);
end
current_gear <= 2'd1;
end 
else if (speed <= NORMAL_GEAR3_MAX) 
begin
if (current_gear != 2'd2) 
begin
gear_up <= (current_gear < 2'd2);
gear_down <= (current_gear > 2'd2);
end
current_gear <= 2'd2;
end 
else 
begin
if (current_gear != 2'd3) 
begin
gear_up <= (current_gear < 2'd3);
gear_down <= (current_gear > 2'd3);
end
current_gear <= 2'd3;
end
end
1'b1: begin
if (speed <= BOAST_GEAR1_MAX) 
begin
if (current_gear != 2'd0) 
begin
gear_down <= 1'b1;
gear_up <= 1'b0;
end                        
current_gear <= 2'd0;
end 
else if (speed <= BOAST_GEAR2_MAX) 
begin
if (current_gear != 2'd1) 
begin
gear_up <= (current_gear < 2'd1);
gear_down <= (current_gear > 2'd1);
end
current_gear <= 2'd1;
end 
else if (speed <= BOAST_GEAR3_MAX) 
begin
if (current_gear != 2'd2) 
begin
gear_up <= (current_gear < 2'd2)
gear_down <=(current_gear > 2'd2);
end
current_gear <= 2'd2;
end 
else 
begin
if (current_gear != 2'd3) 
begin
gear_up <= (current_gear < 2'd3);
gear_down <= (current_gear > 2'd3);
end
current_gear <= 2'd3;
end
end
endcase
end
end
endmodule