clear ;
close all;
clc;
% read image
I = imread('cameraman.tif');
[r,c] = size(I);
zoom = 3;
r2 = r*zoom;
c2 = c*zoom;
I2 = zeros(r2,c2);
I2(1:zoom:r2, 1:zoom:c2) = I;
for i = 1:zoom:r2
    for j = 1:zoom:c2
		I2(i+1,j) = I2(i,j);
		I2(i,j+1) = I2(i,j);         
		I2(i+1,j+1) = I2(i,j);            
    end
end

figure;
imshow(I);
title('Original');
figure;
imshow(I2,[]);
title('Pixel replication zoomed');