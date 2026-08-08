%clear all;
%close all;
clc;

I = imread('eight.tif');
figure;
imshow(I);title('Original');
I = imnoise(I,'salt & pepper',0.02);
figure;
imshow(I);title('Noisy image');
I=im2double(I);
J = I;
for r = 2:size(I,1) - 1
    for c = 2:size(I,2) - 1
         J(r, c) = (1*I(r-1,c-1)  +   2*I(r-1,c) +    1*I(r-1,c+1) + ...
                    2*I(r,c-1)    +  4*I(r,c)   +    2*I(r,c+1)  + ...
                    1*I(r+1,c-1)  +   2*I(r+1,c) +    1*I(r+1,c+1)) / 16;
    end
end

figure;
imshow(J,[]);title('Weighted avg. filter');