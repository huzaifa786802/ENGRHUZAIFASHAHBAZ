clear all;
close all;
clc;

I = imread('moon.tif');
I = imnoise(I,'salt & pepper',0.02);
I = im2double(I);

J = zeros(size(I,1),size(I,2));
R1 = zeros(size(I,1),size(I,2));
R2 = zeros(size(I,1),size(I,2));

w1 = 0;
w2 = 0;
w3 = 0;
w4 = 0;
w5 = -1;
w6 = -1;
w7 = 0;
w8 = 1;
w9 = 1;

TH = 0;
% convert for double 
TH = TH/255;

for r = 2:size(I,1) - 1
    for c = 2:size(I,2) - 1
          R1(r,c) = w5*I(r,c) + w9*I(r+1,c+1);
          R2(r,c) = w8*I(r+1,c) + w6*I(r,c+1);
          if(R1(r,c) < TH)
              R1(r,c) = 0;
          end
          if(R2(r,c) < TH)
              R2(r,c) = 0;
          end
          J(r,c) = sqrt(R1(r,c)^2 + R2(r,c)^2);
    end
end

subplot(1,5,1);
imshow(I);title('Original Image');
subplot(1,5,2);
imshow(R1);title('Robert cross top-down');
subplot(1,5,3);
imshow(R2);title('Robert cross down-top');
subplot(1,5,4);
imshow(J);title('Robert cross combine');

% K = imsubtract(I,J);
% subplot(1,5,5);
% imshow(K);title('Enhanced image');