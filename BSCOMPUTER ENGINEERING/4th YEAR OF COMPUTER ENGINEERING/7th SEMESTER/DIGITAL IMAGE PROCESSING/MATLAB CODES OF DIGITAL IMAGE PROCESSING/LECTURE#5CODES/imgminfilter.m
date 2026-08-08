clear all;
close all;
clc;
I = imread('eight.tif');
figure;
imshow(I);title('Original');
I = imnoise(I,'salt & pepper',0.02);
figure;
imshow(I);title('Noisy image');
I = cast(I,'double');
% for min set filter to 1 and for max set filter to 9
filter = 1;% min filter remove all salt noise
I = ordfilt2(I,filter,ones(3,3));
%filter = 1;% max filter remove all pepper noise
%I = ordfilt2(I,filter,ones(3,3));
figure;
imshow(I,[]);title('min/max filter');