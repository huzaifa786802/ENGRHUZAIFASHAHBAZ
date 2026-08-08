clear all;
close all;
clc;

I1 = imread('cameraman.tif');

I2 = imread('rice.png');

subplot(3,3,1);
subimage(I1);title('Original I1');

subplot(3,3,2);
subimage(I2);title('Original I2');

I3 = imadd(I1,I2,'uint8');

I4 = imsubtract(I1,I2);

I5 = immultiply(I1,2);


I6 = imdivide(I1,2);

subplot(3,3,3);
subimage(I3);title('I1 + I2');

subplot(3,3,4);
subimage(I4);title('I1 - I2');

subplot(3,3,5);
subimage(I5);title('I1 * 2');

subplot(3,3,6);
subimage(I6);title('I1 / 2');