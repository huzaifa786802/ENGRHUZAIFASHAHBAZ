clear all;
close all;
clc;

I = imread('cameraman.tif');
figure;
imshow(I);title('Original');

r_min = 96;
r_max = 180;
c = 200;

for i = 1:size(I,1)
    for j = 1:size(I,2)
        if(I(i,j) > r_min && I(i,j) < r_max)            
            I(i,j) = c;
        else
            I(i,j) = 50;
        end
    end
end

figure;
imshow(I);title('Level Thresholding Transformation');