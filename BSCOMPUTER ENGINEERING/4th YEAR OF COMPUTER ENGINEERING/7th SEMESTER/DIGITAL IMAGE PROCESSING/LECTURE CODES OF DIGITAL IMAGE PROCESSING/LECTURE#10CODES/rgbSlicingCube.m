close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
imshow(I);
w = 140;
a = [140,30,30];
for i = 1:size(I,1)
    for j = 1:size(I,2)
        for k = 1:3
            if(abs(I(i,j,k) - a(k)) > w/2)
                I(i,j,:) = 128;
            end
        end
    end
end

figure;
imshow(I);