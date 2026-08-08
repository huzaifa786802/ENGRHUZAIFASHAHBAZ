`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/29/2024 08:46:14 PM
// Design Name: 
// Module Name: module trafficlightcontroller
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


module traffic_light_controller(
    input wire clk,       // Clock signal
    input wire reset,     // Reset signal
    input wire sensor,    // Traffic sensor input
    output reg [1:0] light // Traffic light output: 00 - Green, 01 - Yellow, 10 - Red
);

// State encoding
typedef enum reg [1:0] {
    GREEN = 2'b00,
    YELLOW = 2'b01,
    RED = 2'b10
} state_t;

state_t current_state, next_state;

// State transition
always @(posedge clk or posedge reset) begin
    if (reset) begin
        current_state <= GREEN; // Default state
    end else begin
        current_state <= next_state;
    end
end

// Next state logic and output logic
always @(*) begin
    case (current_state)
        GREEN: begin
            light = 2'b00; // Green light
            if (sensor) begin
                next_state = YELLOW; // Transition to Yellow if sensor is high
            end else begin
                next_state = GREEN; // Stay in Green if sensor is low
            end
        end
        YELLOW: begin
            light = 2'b01; // Yellow light
            next_state = RED; // Transition to Red
        end
        RED: begin
            light = 2'b10; // Red light
            if (sensor) begin
                next_state = GREEN; // Transition to Green if sensor is high
            end else begin
                next_state = RED; // Stay in Red if sensor is low
            end
        end
        default: begin
            next_state = GREEN; // Default state
        end
    endcase
end

endmodule
