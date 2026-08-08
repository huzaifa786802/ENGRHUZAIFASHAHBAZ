close all;
clear all;
clc;
% read rgb image
I = imread('rgb_mix.jpg');
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);
figure;
imshow([R G B]);
figure;% combine the R,G and B
I_rgb = cat(3, R, G, B);
% [X,cmap] = imread('rgb_mix.jpg');
imshow(I_rgb);