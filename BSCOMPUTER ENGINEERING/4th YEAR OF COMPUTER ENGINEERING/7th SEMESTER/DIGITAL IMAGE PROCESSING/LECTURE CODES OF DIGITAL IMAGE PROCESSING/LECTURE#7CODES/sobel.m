clear all;
close all;
clc;

I = imread('moon.tif');
I=im2double(I);

J = zeros(size(I,1),size(I,2));
K = zeros(size(I,1),size(I,2));

w1 = -1;
w2 = -2;
w3 = -1;
w4 = 0;
w5 = 0;
w6 = 0;
w7 = 1;
w8 = 2;
w9 = 1;

z1 = -1;
z2 = 0;
z3 = 1;
z4 = -2;
z5 = 0;
z6 = 2;
z7 = -1;
z8 = 0;
z9 = 1;

for r = 2:size(I,1) - 1
    for c = 2:size(I,2) - 1                         
         R1(r, c) = abs(w1*I(r-1,c-1)  +   w2*I(r-1,c) +    w3*I(r-1,c+1) + ...
                    w7*I(r+1,c-1)  +   w8*I(r+1,c) +    w9*I(r+1,c+1));
                    
         R2(r, c) = abs(z3*I(r-1,c+1)  +  z6*I(r,c+1) +    z9*I(r+1,c+1) + ...
                    z1*I(r-1,c-1)  +   z4*I(r,c-1) +    z7*I(r+1,c-1));
                
         J(r,c) = R1(r,c) + R2(r,c);
    end
end

% subplot(1,5,1);
figure;
imshow(I);title('Original Image');
% subplot(1,5,2);
% imshow(R1);title('Sobel horizontal');
% subplot(1,5,3);
% imshow(R2);title('Sobel vertical');
% subplot(1,5,4);
figure;
imshow(J);title('Sobel combine');

K = imsubtract(I,J);
% subplot(1,5,5);
% imshow(K);title('Enhanced image');