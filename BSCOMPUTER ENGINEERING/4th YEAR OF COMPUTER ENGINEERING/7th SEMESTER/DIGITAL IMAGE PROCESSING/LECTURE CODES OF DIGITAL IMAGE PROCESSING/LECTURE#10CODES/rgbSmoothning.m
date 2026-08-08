close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
% add noise
I = imnoise(I,'salt & pepper',0.12);
figure;
subplot(1,2,1);
imshow(I);
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);

%average Filter Coefficient
Avg = [1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;1,1,1,1,1];
Avg = 1/25.* Avg;

%Convolution of image by Gaussian Coefficient
R=conv2(R, Avg, 'same');
G=conv2(G, Avg, 'same');
B=conv2(B, Avg, 'same');

% combine the R,G and B
I = cat(3, R, G, B);

subplot(1,2,2);
imshow(uint8(I));


figure;
imshow([R G B],[]);