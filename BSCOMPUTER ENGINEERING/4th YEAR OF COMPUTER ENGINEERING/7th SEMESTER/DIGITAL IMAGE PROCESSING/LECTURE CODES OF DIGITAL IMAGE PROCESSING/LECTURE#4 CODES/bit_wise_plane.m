clear all;
close all;
clc;

I = imread('eight.tif');
figure;
imshow(I,[]);title('Original');

for i=1:8
    bitPlane(i).level = zeros(size(I));
end

figure;
for i=1:8
    bitPlane(i).level = bitget(I,i);
    subplot(2,4,i);
    imshow(bitPlane(i).level,[]);
end


