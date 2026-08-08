clc;
clear all;
close all;
I = imread('fruit.png');
imshow(I);
I_igs_r = quantize(I(:,:,1),4,'igs');
I_igs_g = quantize(I(:,:,2),4,'igs');
I_igs_b = quantize(I(:,:,3),4,'igs');
I_no_igs_r = quantize(I(:,:,1),4);
I_no_igs_g = quantize(I(:,:,2),4);
I_no_igs_b = quantize(I(:,:,3),4);
% combine the R,G and B
I_igs = cat(3, I_igs_r, I_igs_g, I_igs_b);
figure;
imshow(I_igs);
% combine the R,G and B
I_no_igs = cat(3, I_no_igs_r, I_no_igs_g, I_no_igs_b);
figure;
imshow(I_no_igs);
imwrite(I_igs,'fruit_color_igs.png');
imwrite(I_no_igs,'fruit_color_no_igs.png');
fileinfo = dir('fruit.png');
filesizeOriginal = fileinfo(1).bytes;
fileinfo = dir('fruit_color_igs.png');
filesizeIGS = fileinfo(1).bytes;
fileinfo = dir('fruit_color_no_igs.png');
filesizeNoIGS = fileinfo(1).bytes;