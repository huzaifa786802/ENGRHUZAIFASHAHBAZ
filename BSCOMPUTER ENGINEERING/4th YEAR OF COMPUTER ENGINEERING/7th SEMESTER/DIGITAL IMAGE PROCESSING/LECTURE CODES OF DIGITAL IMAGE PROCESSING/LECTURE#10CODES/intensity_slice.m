close all;
clear all;
clc;
% read rgb image
I = imread('cameraman.tif');
imshow(I);
I_rgb = zeros(size(I,1), size(I,2),3);
for i = 1:size(I,1)
    for j = 1:size(I,2)
        if(I(i,j) >= 0 && I(i,j) < 32)    
            I_rgb(i,j,1) = 64;  
            I_rgb(i,j,3) = 64;
        elseif(I(i,j) >= 32 && I(i,j) < 64)
            I_rgb(i,j,2) = 64;  
            I_rgb(i,j,3) = 64;
        elseif(I(i,j) >= 64 && I(i,j) < 96)
            I_rgb(i,j,1) = 96;  
            I_rgb(i,j,3) = 96;
        elseif(I(i,j) >= 96 && I(i,j) < 128)
            I_rgb(i,j,2) = 96;  
            I_rgb(i,j,3) = 96;
        elseif(I(i,j) >= 128 && I(i,j) < 160)
            I_rgb(i,j,1) = 128;  
            I_rgb(i,j,3) = 128;
        elseif(I(i,j) >= 160 && I(i,j) < 192)
            I_rgb(i,j,1) = 255;
        elseif(I(i,j) >= 192 && I(i,j) < 224)
            I_rgb(i,j,2) = 255;
        elseif(I(i,j) >= 224 && I(i,j) < 256)
            I_rgb(i,j,3) = 255;
        end
    end
end
figure;
imshow(uint8(I_rgb));
