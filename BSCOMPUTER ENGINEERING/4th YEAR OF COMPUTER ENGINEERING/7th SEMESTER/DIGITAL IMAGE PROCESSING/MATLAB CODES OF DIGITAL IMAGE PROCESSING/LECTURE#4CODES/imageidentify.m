I = imread('cameraman.tif');
[r c] = size(I);
I_1 = zeros(r,c);
for i=1:r
    for j=1:c
    	I_1(i,j) = I(i,j);
    end
end