clear all;
close all;
clc;
I = imread('cameraman.jpg');
figure;
imshow(I);title('Original');
r_min = 96;
r_max = 160;
c = 32;
for i = 1:size(I,1)
    for j = 1:size(I,2)
        if(I(i,j) < r_min)
            I(i,j) = I(i,j) - c;
        elseif(I(i,j) > r_max)
            I(i,j) = I(i,j) - c;       
        end
    end
end
figure;
imshow(I,[]);title('Level Thresholding Transformation');