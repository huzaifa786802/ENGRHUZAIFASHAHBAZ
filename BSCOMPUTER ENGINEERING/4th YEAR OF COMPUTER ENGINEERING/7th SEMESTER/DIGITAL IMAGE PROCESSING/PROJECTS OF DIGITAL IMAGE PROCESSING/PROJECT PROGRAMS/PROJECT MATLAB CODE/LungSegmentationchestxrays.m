% Read the input image
img = imread('Lung Segmentation chest x-rays.jpg');
if size(img, 3) > 1
    img = rgb2gray(img);
end
img = im2double(img);

% Preprocessing and Noise Removal
% Apply Gaussian filter for noise reduction
img_denoised = imgaussfilt(img, 2);

% Histogram Equalization
img_histeq = adapthisteq(img_denoised);

% Normalization
img_normalized = (img_histeq - min(img_histeq(:))) / (max(img_histeq(:)) - min(img_histeq(:)));

% Bone Suppression using morphological operations
se_bone = strel('disk', 15);
background = imopen(img_normalized, se_bone);
img_bone_suppressed = img_normalized - background;

% Global Thresholding
level = graythresh(img_bone_suppressed);
img_global_thresh = imbinarize(img_bone_suppressed, level);

% Adaptive Thresholding
img_adaptive_thresh = imbinarize(img_bone_suppressed, 'adaptive', 'Sensitivity', 0.4);

% Edge Detection using different methods
% Canny Edge Detection
img_canny = edge(img_bone_suppressed, 'Canny');

% Sobel Filter
img_sobel = edge(img_bone_suppressed, 'Sobel');

% Prewitt Filter
img_prewitt = edge(img_bone_suppressed, 'Prewitt');

% Morphological Operations
se = strel('disk', 3);

% Dilation
img_dilated = imdilate(img_adaptive_thresh, se);

% Erosion
img_eroded = imerode(img_adaptive_thresh, se);

% Opening (Erosion followed by Dilation)
img_opened = imopen(img_adaptive_thresh, se);

% Closing (Dilation followed by Erosion)
img_closed = imclose(img_adaptive_thresh, se);

% Display results
figure('Position', [100 100 1200 800]);

subplot(4,4,1), imshow(img), title('Original Image')
subplot(4,4,2), imshow(img_denoised), title('Denoised')
subplot(4,4,3), imshow(img_histeq), title('Histogram Equalized')
subplot(4,4,4), imshow(img_normalized), title('Normalized')
subplot(4,4,5), imshow(img_bone_suppressed), title('Bone Suppressed')
subplot(4,4,6), imshow(img_global_thresh), title('Global Threshold')
subplot(4,4,7), imshow(img_adaptive_thresh), title('Adaptive Threshold')
subplot(4,4,8), imshow(img_canny), title('Canny Edge')
subplot(4,4,9), imshow(img_sobel), title('Sobel Edge')
subplot(4,4,10), imshow(img_prewitt), title('Prewitt Edge')
subplot(4,4,11), imshow(img_dilated), title('Dilated')
subplot(4,4,12), imshow(img_eroded), title('Eroded')
subplot(4,4,13), imshow(img_opened), title('Opened')
subplot(4,4,14), imshow(img_closed), title('Closed')

% Save processed images
imwrite(img_denoised, 'denoised.png');
imwrite(img_histeq, 'histogram_equalized.png');
imwrite(img_normalized, 'normalized.png');
imwrite(img_bone_suppressed, 'bone_suppressed.png');
imwrite(img_global_thresh, 'global_threshold.png');
imwrite(img_adaptive_thresh, 'adaptive_threshold.png');
imwrite(img_canny, 'canny_edge.png');
imwrite(img_sobel, 'sobel_edge.png');
imwrite(img_prewitt, 'prewitt_edge.png');
imwrite(img_dilated, 'dilated.png');
imwrite(img_eroded, 'eroded.png');
imwrite(img_opened, 'opened.png');
imwrite(img_closed, 'closed.png');