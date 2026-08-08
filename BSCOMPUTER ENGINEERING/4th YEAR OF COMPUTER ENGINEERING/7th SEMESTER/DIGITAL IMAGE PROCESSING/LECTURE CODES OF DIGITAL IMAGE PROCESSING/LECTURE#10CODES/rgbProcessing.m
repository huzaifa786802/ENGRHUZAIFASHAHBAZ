close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
imshow(I);
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);
figure;
imshow([R G B]);
% increase intensity
k = 1.75;
R = k*R;
G = k*G;
B = k*B;
figure;
imshow([R G B]);
% combine the R,G and B
I = cat(3, R, G, B);
figure;
imshow(I);