close all;
clear all;
clc;
% read rgb image
Img = imread('rgb_mix.jpg');
Img = im2double(Img);
imshow(Img);

R = Img(:,:,1);
G = Img(:,:,2);
B = Img(:,:,3);

% Hue
H = acos((1/2*(R - G + R - B))./(sqrt((R-B).^2 + (R - G).*(G - B))));
H(B > G) = 2*pi - H(B > G);
H = H/(2*pi);

% intensity
I = 1/3.*(R + G + B);

% saturation
minRGB = min(min((R), (G)), (B));
S = 1 - 3.*(minRGB)./(R + G + B);
figure;
imshow([H S I]);