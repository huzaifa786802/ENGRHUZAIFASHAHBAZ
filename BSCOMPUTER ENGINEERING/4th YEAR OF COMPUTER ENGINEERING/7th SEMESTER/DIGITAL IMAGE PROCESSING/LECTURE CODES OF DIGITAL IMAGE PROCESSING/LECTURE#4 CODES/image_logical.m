clear all;
close all;
clc;

I1 = imread('003_F.png');
I1 = rgb2gray(I1);

I2 = imread('003_B.png');
I2 = rgb2gray(I2);

subplot(3,3,1);
subimage(I1);title('Original I1');

subplot(3,3,2);
subimage(I2);title('Original I2');

I3 = bitand(I1,I2);

I4 = bitor(I1,I2);

I5 = imcomplement(I1);

subplot(3,3,3);
imshow(I3);title('I1 & I2');

subplot(3,3,4);
imshow(I4);title('I1 || I2');

subplot(3,3,5);
imshow(I5);title('~I1');
