close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
imshow(I);
R = 255 - I(:,:,1);
G = 255 - I(:,:,2);
B = 255 - I(:,:,3);

% combine the R,G and B
I_neg = cat(3, R, G, B);
figure;
imshow(I_neg);