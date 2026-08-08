close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
I = 0.25.*I;
imshow(I);
figure;
histogram(I);title('Original Hist');
% I_whole = histeq(I);
[H S V] = rgb2hsv(I);
V = histeq(V);
I_histeq = hsv2rgb(H,S,V);
figure;
imshow(I_histeq);
figure;
histogram(I_histeq);title('Value Hist');
