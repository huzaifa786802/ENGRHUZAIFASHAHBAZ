close all;
clear all;
clc;
% read rgb image
I = imread('fruit.jpg');
imshow(I);

for i = 1:size(I,1)
    for j = 1:size(I,2)
        if(I(i,j,2) > 40 && ...
            I(i,j,3) > 40) 
            I(i,j,:) = 128;
        end
    end
end

figure;
imshow(I);