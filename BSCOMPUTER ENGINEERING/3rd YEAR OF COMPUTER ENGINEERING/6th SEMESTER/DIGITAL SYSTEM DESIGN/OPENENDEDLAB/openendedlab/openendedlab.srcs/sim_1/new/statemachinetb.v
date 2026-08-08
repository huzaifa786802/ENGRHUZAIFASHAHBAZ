`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/30/2024 11:21:26 AM
// Design Name: 
// Module Name: statemachinetb
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
module statemachinetb();
reg clock;
reg reset;
reg N_B;
reg [3:0]speed;
wire gear_down;
wire gear_up;
statemachine uut(.clk(clk),.reset(reset),.N_B(N_B),.speed(speed),.gear_up(gear_up),.gear_down(gear_down));
initial
begin
    clk = 0;
    forever #5 clk = ~clk; // 10ns clock period
end
initial 
begin
    reset = 1;
    N_B = 0;
    speed = 0;
    #10;
    reset = 0;
    N_B = 0;
    #20 speed = 18; 
    #20 speed = 35; 
    #20 speed = 57; 
    #20 speed = 79; 
    #20 speed = 68; 
    #20 speed = 40; 
    #20 speed = 14; 
    #10 N_B = 1;
    #20 speed = 28; 
    #20 speed = 39; 
    #20 speed = 69; 
    #20 speed = 95; 
    #20 speed = 73; 
    #20 speed = 53; 
    #20 speed = 28; 
    #10 $stop;
end
endmodule    