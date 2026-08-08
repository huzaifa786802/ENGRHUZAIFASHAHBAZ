clear all;
close all;
clc;

I = imread('cameraman.tif');
figure;
imshow(I);title('Original');

c = 1;
r = 0.05;

I_power = c * realpow(cast(I,'double'),r);
figure;
imshow(I_power,[]);title('PowerLaw Transformation');