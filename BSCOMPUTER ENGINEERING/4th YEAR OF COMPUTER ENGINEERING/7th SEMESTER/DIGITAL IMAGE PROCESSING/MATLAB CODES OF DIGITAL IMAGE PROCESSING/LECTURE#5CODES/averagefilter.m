% Load the image
image = imread('eight.bmp'); % Replace with the correct path to your image file

% Convert the image to grayscale if it's not already
if size(image, 3) == 3
    image = rgb2gray(image);
end

% Apply the averagefilter function
% Display the original and filtered images
figure;
% Original image
subplot(1, 2, 1);
imshow(image, []);
colormap('jet'); % Apply colorful colormap
colorbar;
title('Original Image');

% Filtered image
subplot(1, 2, 2);
colormap('jet'); % Apply colorful colormap
colorbar;
title('Filtered Image with Average Filter');
