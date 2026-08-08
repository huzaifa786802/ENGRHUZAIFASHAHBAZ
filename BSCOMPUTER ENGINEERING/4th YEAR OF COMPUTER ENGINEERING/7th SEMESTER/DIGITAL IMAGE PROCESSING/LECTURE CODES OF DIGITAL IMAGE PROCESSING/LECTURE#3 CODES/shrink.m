clear all;
close all;
clc;

I = imread('cameraman.tif');
figure;
imshow(I);title('Original');
I2 = imresize(I,0.5);
figure;
imshow(I2);title('shrink');