% Load the image
imagePath = 'CAR_IMAGE.jpg'; % Replace with your image path
originalImage = imread(imagePath);

% Pre-processing
grayImage = rgb2gray(originalImage); % Convert to grayscale
filteredImage = medfilt2(grayImage, [3 3]); % Median filtering to remove noise
enhancedImage = imadjust(filteredImage); % Contrast enhancement

% Edge Detection
edges = edge(enhancedImage, 'Canny'); % Edge detection using Canny method

% Morphological operations to close gaps in edges
se = strel('rectangle', [5, 5]);
closedEdges = imclose(edges, se);

% Region of Interest Extraction
% Find connected components
cc = bwconncomp(closedEdges);
stats = regionprops(cc, 'BoundingBox', 'Area');

% Filter out small regions based on area
minArea = 500; % Adjust this threshold as needed
licensePlateRegions = stats([stats.Area] > minArea);

% Assuming the license plate is the largest region
[~, idx] = max([licensePlateRegions.Area]);
boundingBox = licensePlateRegions(idx).BoundingBox;

% Crop the license plate area
licensePlateImage = imcrop(enhancedImage, boundingBox);

% Character Segmentation
% Binarize the license plate image
binaryPlate = imbinarize(licensePlateImage);
binaryPlate = imcomplement(binaryPlate); % Invert colors: characters should be white

% Remove small objects that are not characters
binaryPlate = bwareaopen(binaryPlate, 50);

% Label connected components
[labeledPlate, numChars] = bwlabel(binaryPlate);

% Extract character images
characterImages = cell(1, numChars);
for k = 1:numChars
    charRegion = ismember(labeledPlate, k);
    characterImages{k} = imcrop(binaryPlate, regionprops(charRegion, 'BoundingBox').BoundingBox);
end

% Optical Character Recognition (OCR)
recognizedText = '';
for k = 1:numChars
    % Resize character image to a fixed size, e.g., 42x24 pixels
    resizedChar = imresize(characterImages{k}, [42, 24]);
    % Use OCR to recognize the character
    ocrResult = ocr(resizedChar, 'CharacterSet', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789');
    recognizedText = [recognizedText, ocrResult.Text];
end

% Display the recognized license plate number
disp(['Recognized License Plate Number: ', recognizedText]);

% Display Results
figure;
subplot(2, 3, 1), imshow(originalImage), title('Original Image');
subplot(2, 3, 2), imshow(enhancedImage), title('Enhanced Grayscale Image');
subplot(2, 3, 3), imshow(edges), title('Edge Detection');
subplot(2, 3, 4), imshow(closedEdges), title('Closed Edges');
subplot(2, 3, 5), imshow(licensePlateImage), title('License Plate Region');
subplot(2, 3, 6), imshow(binaryPlate), title(['Recognized Text: ', recognizedText]);
