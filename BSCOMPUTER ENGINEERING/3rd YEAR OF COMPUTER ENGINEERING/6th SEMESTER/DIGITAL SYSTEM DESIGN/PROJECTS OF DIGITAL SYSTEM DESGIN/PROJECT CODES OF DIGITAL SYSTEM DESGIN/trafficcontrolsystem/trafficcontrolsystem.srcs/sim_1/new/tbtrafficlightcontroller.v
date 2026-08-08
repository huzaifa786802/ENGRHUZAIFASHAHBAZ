`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/29/2024 08:54:53 PM
// Design Name: 
// Module Name: tbtrafficlightcontroller
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


module tbtrafficlightcontroller();
reg clk;
reg reset;
reg sensor;
wire [1:0] light;
traffic_light_controller uut (.clk(clk),.reset(reset),.sensor(sensor),.light(light));
initial 
begin
    clk = 0;
    forever #5 clk = ~clk; 
end
initial 
begin
    reset = 1;
    sensor = 0;
    #10 reset = 0;
    #10 reset = 1;
    #20 sensor = 0; 
    #40 sensor = 0; 
    #20 sensor = 1; 
    #10 sensor = 0; 
    #20 sensor = 1; 
    #20 sensor = 0; 
    #40 sensor = 0; 
    #50 $finish;
end
initial 
begin
    $monitor("Time=%0d, Reset=%b, Sensor=%b, Light=%b", $time, reset, sensor, light);
end
endmodule