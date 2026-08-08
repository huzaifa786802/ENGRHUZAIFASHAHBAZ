close all;
clear all;
clc;
% read rgb image
I = imread('onion.png');
imshow(I);
% I = im2double(I);
CMY = I;
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);

% red
CMY(:,:,1) = 255 - R;
% green
CMY(:,:,2) = 255 - G;
% blue
CMY(:,:,3) = 255 - B;
figure;
imshow(CMY);