clear all;
close all;
clc;

%Input image
img = imread('moon.tif');

% image to double
img = double (img);

%Show input image
figure;
imshow(img,[]);title('Original image');

%Value for Thresholding
T_Low = 50/255;
T_High = 70/255;

%Gaussian Filter Coefficient
B = [2, 4, 5, 4, 2; 4, 9, 12, 9, 4;5, 12, 15, 12, 5;4, 9, 12, 9, 4;2, 4, 5, 4, 2 ];
B = 1/159.* B;

%Convolution of image by Gaussian Coefficient
A=conv2(img, B, 'same');

%Show gradiant image
figure;
imshow(A,[]);title('Smooth image');

%Filter for horizontal and vertical direction
KGx = [-1, 0, 1; -2, 0, 2; -1, 0, 1];
KGy = [1, 2, 1; 0, 0, 0; -1, -2, -1];

%Convolution by image by horizontal and vertical filter
Filtered_X = conv2(A, KGx, 'same');
Filtered_Y = conv2(A, KGy, 'same');

% combine filter image
Filtered_XY = abs(Filtered_X) + abs(Filtered_Y);
figure;
imshow(Filtered_XY,[]);title('Filter image');

%Calculate directions/orientations
edge_dir = atan2 (Filtered_Y, Filtered_X);
% radians to degree
edge_dir = edge_dir*180/pi;

rows=size(A,1);
col=size(A,2);

%Adjustment for negative directions, making all directions positive
for i=1:rows
    for j=1:col
        if (edge_dir(i,j) < 0) 
            edge_dir(i,j) = 360 + edge_dir(i,j);
        end
    end
end

edge_dir2=zeros(rows, col);
%Adjusting directions to nearest 0, 45, 90, or 135 degree
for i = 1  : rows
    for j = 1 : col
        if ((edge_dir(i, j) >= 0 ) && (edge_dir(i, j) < 22.5) ||...
            (edge_dir(i, j) >= 157.5) && (edge_dir(i, j) < 202.5) ||...
            (edge_dir(i, j) >= 337.5) && (edge_dir(i, j) <= 360))
        
            edge_dir2(i, j) = 0;
        elseif ((edge_dir(i, j) >= 22.5) && (edge_dir(i, j) < 67.5) ||...
                (edge_dir(i, j) >= 202.5) && (edge_dir(i, j) < 247.5))
            
            edge_dir2(i, j) = 45;
        elseif ((edge_dir(i, j) >= 67.5 && edge_dir(i, j) < 112.5) ||...
                (edge_dir(i, j) >= 247.5 && edge_dir(i, j) < 292.5))
            
            edge_dir2(i, j) = 90;
        elseif ((edge_dir(i, j) >= 112.5 && edge_dir(i, j) < 157.5) ||...
                (edge_dir(i, j) >= 292.5 && edge_dir(i, j) < 337.5))
            
            edge_dir2(i, j) = 135;
        end
    end
end
figure;
imagesc(edge_dir2); colorbar;title('Edge Direction');

%Calculate magnitude
magnitude = (Filtered_X.^2) + (Filtered_Y.^2);
magnitude2 = sqrt(magnitude);
BW = zeros (rows, col);

%Non-Maximum Supression
for i=2:rows-1
    for j=2:col-1
        if (edge_dir2(i,j)==0)
            BW(i,j) = (magnitude2(i,j) == max([magnitude2(i,j), magnitude2(i-1,j), magnitude2(i+1,j)]));
        elseif (edge_dir2(i,j)==45)
            BW(i,j) = (magnitude2(i,j) == max([magnitude2(i,j), magnitude2(i-1,j-1), magnitude2(i+1,j+1)]));
        elseif (edge_dir2(i,j)==90)
            BW(i,j) = (magnitude2(i,j) == max([magnitude2(i,j), magnitude2(i,j-1), magnitude2(i,j+1)]));
        elseif (edge_dir2(i,j)==135)
            BW(i,j) = (magnitude2(i,j) == max([magnitude2(i,j), magnitude2(i+1,j-1), magnitude2(i-1,j+1)]));
        end
    end
end
BW = BW.*magnitude2;
figure;
imshow(BW);title('Non-maximum suppression');

%Hysteresis Thresholding
T_Low = T_Low * max(max(BW));
T_High = T_High * max(max(BW));
H_TH = zeros (rows, col);
for i = 1  : rows
    for j = 1 : col
        if (BW(i, j) < T_Low)
            H_TH(i, j) = 0;
        elseif (BW(i, j) > T_High)
            H_TH(i, j) = 0;
        %Using 8-connected components
        elseif ((BW(i, j) > T_Low && BW(i, j) < T_High) && ...
                (BW(i-1,j-1)> T_High || BW(i-1,j) > T_High || BW(i-1,j+1) > T_High ||...
                 BW(i,j-1)  > T_High                       || BW(i,j+1)   > T_High ||...
                 BW(i+1,j-1)> T_High || BW(i+1,j) > T_High || BW(i+1, j+1)> T_High))
            H_TH(i,j) = 1;
        end
    end
end

%Show final edge detection result
figure;
imshow(H_TH,[]);title('Hysterisis thresholding');
