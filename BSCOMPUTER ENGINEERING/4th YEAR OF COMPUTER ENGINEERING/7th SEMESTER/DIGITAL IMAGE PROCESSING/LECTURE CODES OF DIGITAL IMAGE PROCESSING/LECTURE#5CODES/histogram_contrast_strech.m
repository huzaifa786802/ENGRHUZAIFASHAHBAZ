clear all;
close all;
clc;

I = imread('pout.tif');
figure;
imshow(I);title('Original');
figure;
histogram(I);title('Original Hist');
r_min = min(I(:));
r_max = max(I(:));
I = cast(I,'double');
r_min = cast(r_min,'double');
r_max = cast(r_max,'double');

I_equ = (I - r_min)*(255)*(1/(r_max - r_min));

figure;
imshow(I_equ,[]);title('Contrast streching using Histrogram');
figure;
histogram(I_equ);title('Contrast streching using Histrogram');