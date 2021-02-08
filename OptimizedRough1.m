%FOR BURGLAR AND THERMAL IMAGE OF ANIMAL
cdata = rgb2gray(cdata)
moon1 = cdata

%FOR CAR IMAGE
%moon1 = rgb2gray(Moon1)
sz = size(moon1)

% we need to feed sublength,subwidth,and compression .
%(1)Considering mooon11
sublength=32         %feed the value of block length
subwidth=32          % feed the value of block width
compression = 95     % feed the value in percentage
levels = ((100-compression)/100)*(sublength*subwidth)
levels = round(levels) % the levels into which comparison shall take place

for(L=0:sublength:sz(1,1)-sublength)
for(W=0:subwidth:sz(1,2)-subwidth)
for(r=W+1:W+subwidth)
    for(c=L+1:L+sublength)
mooon11(r-W,c-L) = moon1(r,c)

    end
end
mooon11;
%(1) Performing algorithm on mooon11


% Finding the no. of bins from the required compression
%compression = 75     % feed the value in percentage
%levels = ((100-compression)/100)*(sublength*subwidth)
%levels = round(levels)
sz11 = size(mooon11)
Highest11 = max(mooon11)
Overalhighest11 = max(Highest11)
Lowest11 = min(mooon11)
Overallowest11 = min(Lowest11)
Diff11 = Overalhighest11 - Overallowest11
Diff11 = double(Diff11)
bin11 = Diff11/levels


%converting to double for mathematical calculations
mooon11 = double(mooon11);
for (r=1:subwidth) %sz11(1,1)
      for (c=1:sublength) %sz11(1,2)
  
for (n=1:1:levels)
if mooon11(r,c)< Overallowest11 + n*bin11
mooonnew11(r,c)= Overallowest11 + (n-1)*bin11
break;
end
end
end
end

mooonnew11 = uint8(mooonnew11)
for(R=W+1:W+sublength)
for(C=L+1:L+subwidth)
mooonnewmerged11(R,C) = mooonnew11(R-W,C-L)

end
end
end
end
imshow(mooonnewmerged11 , [0 255])
figure,imshow(moon1)
%function PSNR = psnr(mooonnewmerged11, moon1)
moon1 = double(moon1);
mooonnewmerged11 = double(mooonnewmerged11);
[M,N] = size(moon1);
error = moon1 - mooonnewmerged11;
MSE = sum(sum(error.*error))/(M*N);
if(MSE > 0)
PSNR = 10*log(255*255/MSE)/ log(10);
else
    PSNR = 99;
end
PSNR