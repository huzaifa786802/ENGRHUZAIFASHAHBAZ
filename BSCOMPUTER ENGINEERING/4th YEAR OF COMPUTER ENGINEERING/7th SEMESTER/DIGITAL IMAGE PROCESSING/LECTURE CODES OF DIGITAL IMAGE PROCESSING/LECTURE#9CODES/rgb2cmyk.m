close all;
clear all;
clc;
% read rgb image
I = imread('rgb_mix.jpg');
imshow(I);
% I = im2double(I);
CMY = I;
R = I(:,:,1);
G = I(:,:,2);
B = I(:,:,3);
m = max(max(R,G), B);
% red
CMY(:,:,1) = 255.*(m - R)./m;
% green
CMY(:,:,2) = 255.*(m - G)./m;
% blue
CMY(:,:,3) = 255.*(m - B)./m;

K = 255 - m;
figure;
imshow(CMY);