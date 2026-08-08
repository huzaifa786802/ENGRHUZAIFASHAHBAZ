% clear all;
% close all;
% clc;
fac = 2;
im0=imread('cameraman.tif');
im=cast(im0,'int16'); 
imshow(cast(im,'uint8'));title('Original');
[h,v]=size(im);
for i=1:h
    for j=1:v
      im1(1+(i-1)*fac,1+(j-1)*fac,:)=im(i,j,:); 
    end   
end
%bilinear interpolation
for i=1:1+(h-2)*fac     %row number
    for j=1:1+(v-2)*fac %column number
       if ((rem(i-1,fac)==0) && (rem(j-1,fac)==0)) 
       else  
           h00=im1( ceil(i/fac)*fac-fac+1,ceil(j/fac)*fac-fac+1,:); 
           h10=im1( ceil(i/fac)*fac-fac+1+fac,ceil(j/fac)*fac-fac+1,:);
           h01=im1( ceil(i/fac)*fac-fac+1,ceil(j/fac)*fac-fac+1+fac,:);
           h11=im1( ceil(i/fac)*fac-fac+1+fac,ceil(j/fac)*fac-fac+1+fac,:);
           x=rem(i-1,fac); %coordinates of calculating pixel.
           y=rem(j-1,fac);  
           dx=x/fac; %localizeing the  pixel being calculated to the nearest four know pixels.
           dy=y/fac;   
           b1=h00;    %constants of bilinear interpolation.
           b2=h10-h00;
           b3=h01-h00;
           b4=h00-h10-h01+h11;           
           im1(i,j,:)=b1+b2*dx+b3*dy+b4*dx*dy; %equation of bilinear interpolation.
         end
    end
end
figure; 
imshow(cast(im1,'uint8'));title('Bilinear Interpolation');