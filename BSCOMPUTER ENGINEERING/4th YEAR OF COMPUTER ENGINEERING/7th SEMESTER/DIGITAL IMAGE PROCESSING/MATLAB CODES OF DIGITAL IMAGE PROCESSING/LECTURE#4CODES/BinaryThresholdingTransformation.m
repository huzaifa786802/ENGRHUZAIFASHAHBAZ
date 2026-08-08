clear all;
close all;
clc;
I = imread('cameraman.tif');
figure;
imshow(I);title('Original');
limit = 100;
for i = 1:size(I,1)
    for j = 1:size(I,2)
        if(I(i,j) > limit)
            I(i,j) = 255;
        else
            I(i,j) = 0;
        end
    end
end
figure;
imshow(I,[]);title('Binary Thresholding Transformation');