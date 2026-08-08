clear all;
close all;
clc;

I = imread('cameraman.tif');
figure;
imshow(I);title('Original');

I_neg = 255 - I;
figure;
imshow(I_neg);title('Negative');