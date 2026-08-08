clear all;
close all;
clc;
I = imread('eight.tif');
subplot(2,2,1);
subimage(I);title('Original');
I = imnoise(I,'salt & pepper',0.02);
subplot(2,2,2);
subimage(I);title('Salt & pepper noise');
% uint8 to double
I = im2double(I);
J = I;
blockSize = 3;
for r = 2:size(I,1) - 1
    for c = 2:size(I,2) - 1
        I(r, c) = (1*I(r,c) + I(r-1,c-1) +  1*I(r-1,c) +I(r-1,c+1) +1*I(r,c-1) +...
            1*I(r,c+1) +I(r+1,c+1) +1*I(r+1,c) +I(r+1,c-1)) / 9;
    end
end
%I = filter2(fspecial('average',3),I);
subplot(2,2,3);
subimage(I);title('3x3 Avg. filter result');
I = filter2(fspecial('average',5),J);
subplot(2,2,4);
subimage(I);title('5x5 Avg. filter result');