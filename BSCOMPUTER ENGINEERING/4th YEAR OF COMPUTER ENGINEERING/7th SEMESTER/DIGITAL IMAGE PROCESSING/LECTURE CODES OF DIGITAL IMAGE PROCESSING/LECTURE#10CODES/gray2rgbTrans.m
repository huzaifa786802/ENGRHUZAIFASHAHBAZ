close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);
imshow([R G B]);
% combine the R,G and B
I_rgb = cat(3, R, G, B);
figure;
imshow(I_rgb);
