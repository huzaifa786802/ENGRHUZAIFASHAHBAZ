% clear all;
% close all;
% clc;

I = imread('cameraman.tif');
figure;
imshow(I);title('Original');
I2 = imresize(I,4);
figure;
imshow(I2);title('Bicubic interpolation');