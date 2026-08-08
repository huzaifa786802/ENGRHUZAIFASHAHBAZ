clear all;
close all;
clc;
I = imread('moon.tif');
I=im2double(I);
A = 1.03;
J = I;
w1 = -1;
w2 = -1;
w3 = -1;
w4 = -1;
w5 = 8 + A;
w6 = -1;
w7 = -1;
w8 = -1;
w9 = -1;
for r = 2:size(I,1) - 1
    for c = 2:size(I,2) - 1
         J(r, c) = (w1*I(r-1,c-1)  +   w2*I(r-1,c) +    w3*I(r-1,c+1) + ...
                    w4*I(r,c-1)    +   w5*I(r,c)   +    w6*I(r,c+1)  + ...
                    w7*I(r+1,c-1)  +   w8*I(r+1,c) +    w9*I(r+1,c+1));
    end
end
figure;
subplot(1,3,1);
imshow(I);title('Original Image');
subplot(1,3,2);
imshow(J);title('Sharp Image');
% high boost filter
%I = A.*I;
%K = imsubtract(I,J);
%subplot(1,3,3);
%imshow(K);title('Enhanced image');