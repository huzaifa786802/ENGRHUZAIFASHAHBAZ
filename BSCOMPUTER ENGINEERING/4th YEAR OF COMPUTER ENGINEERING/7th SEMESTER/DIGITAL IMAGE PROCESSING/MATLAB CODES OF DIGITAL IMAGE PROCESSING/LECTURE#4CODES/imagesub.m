I = imread('rice.png');
%Estimate the background.
background = imopen(I,strel('disk',15));
imshow(background)
%Subtract the background from the image.
J = imsubtract(I,background);
%Display the original image and the processed image.
imshow(I)