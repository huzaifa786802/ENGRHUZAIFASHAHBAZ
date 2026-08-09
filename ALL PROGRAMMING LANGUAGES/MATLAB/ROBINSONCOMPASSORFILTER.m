% Robinson Compass Edge Detection Implementation
clear all;
close all;
clc;
% Read the input image
img = imread('moon.jpg');  % Make sure your image is in the current directory
% Convert to grayscale if needed
if size(img,3) == 3
    img = rgb2gray(img);
end
% Convert to double for calculations
img = double(img);
% Define the Robinson compass masks (8 directions)
masks = cell(1,8);
% North
masks{1} = [-1 0 1; -2 0 2; -1 0 1];
% North West
masks{2} = [0 1 2; -1 0 1; -2 -1 0];
% West
masks{3} = [1 2 1; 0 0 0; -1 -2 -1];
% South West
masks{4} = [2 1 0; 1 0 -1; 0 -1 -2];
% South
masks{5} = [1 0 -1; 2 0 -2; 1 0 -1];
% South East
masks{6} = [0 -1 -2; 1 0 -1; 2 1 0];
% East
masks{7} = [-1 -2 -1; 0 0 0; 1 2 1];
% North East
masks{8} = [-2 -1 0; -1 0 1; 0 1 2];
% Create figure for original and processed images
figure('Name', 'Robinson Edge Detection Results', 'Position', [100 100 1200 800]);
% Display original image
subplot(3,4,1);
imshow(uint8(img));
title('Original Image');
axis on;
% Initialize arrays for results
directional_edges = cell(1,8);
enhanced_directional = cell(1,8);
all_edges = zeros(size(img));
% Process each direction and display results
for i = 1:8
    % Apply Robinson operator
    directional_edges{i} = abs(conv2(img, masks{i}, 'same'));
    % Normalize edge detection result
    normalized_edge = directional_edges{i} / max(directional_edges{i}(:)) * 255;
    
    % Display edge detection result
    subplot(3,4,i+1);
    imshow(uint8(normalized_edge));
    title(['Direction ' num2str(i)]);
    axis on;
    
    % Accumulate edges for combined result
    all_edges = all_edges + directional_edges{i};
end

% Normalize combined edges
combined_edges = all_edges / max(all_edges(:)) * 255;

% Create enhanced image
enhanced_image = img + combined_edges;
enhanced_image = enhanced_image / max(enhanced_image(:)) * 255;

% Display combined edges
subplot(3,4,10);
imshow(uint8(combined_edges));
title('Combined Edges');
axis on;

% Display enhanced image
subplot(3,4,11);
imshow(uint8(enhanced_image));
title('Enhanced Image');
axis on;

% Display Laplacian filter result (for comparison)
laplacian_filter = [0 1 0; 1 -4 1; 0 1 0];
laplacian_result = abs(conv2(img, laplacian_filter, 'same'));
laplacian_result = laplacian_result / max(laplacian_result(:)) * 255;

subplot(3,4,12);
imshow(uint8(laplacian_result));
title('Laplacian Filter');
axis on;

% Add color bars to all subplots
for i = 1:12
    subplot(3,4,i);
    colorbar;
end

% Adjust figure properties
set(gcf, 'Color', 'white');
sgtitle('Robinson Compass Edge Detection Analysis');

% Save the results
imwrite(uint8(combined_edges), 'combined_edges.jpg');
imwrite(uint8(enhanced_image), 'enhanced_image.jpg');

% Display processing complete message
disp('Edge detection processing complete. Results have been displayed and saved.');