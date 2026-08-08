BW = zeros(8,8);
BW(2:4,2:3) = 1;
BW(5:7,4:5) = 1;
BW(2,6:8) = 1;
BW(3,7:8) = 1;
BW

cc4 = bwconncomp(BW,4)

cc8 = bwconncomp(BW)

L4 = labelmatrix(cc4)

L8 = labelmatrix(cc8)

RGB_label = label2rgb(L4,@copper,"c","shuffle");
imshow(RGB_label)