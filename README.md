# Compression Algorithm Verification (Python)

## Algorithm 

<ul>
  <li>[Image] := PixelArray[i,j]</li>
  <li>For [ImageRow]</li>
  <ul>
    <li>For [ImageCols]</li>
    <ul>
      <li>[ImageBlock] := [Image][nrow,ncol]</li>
      <li>min, max := [ImageBlock]</li>
      <li>bins := (max - min)/[levels]</li>
      <li>[ImageBlock] := shiftThresholds[levels]</li>
    </ul>
  </ul>
  <li>[ImageRescale]</li>
</ul>

## Usage
The main code functionality is put into the <code>optimized_algorithm.py</code> file. The inputs are the files that are to be simulated by using the compression algorithm for rescaling the images pixel intensities and then checking the variational result that we obtain with respect to the change in the PSNR degradation. Also, another change is make with respect to the variation by shifting the pixel values to the minimum pixel values in the extracted block sizes and then analysing in terms of the PNSR and the histogram mapping of the intensities.

## Results

| Processed Grayscale Image | Processed Thermal Image |
|------------|-------------|
|<p align="center"><img src="https://github.com/wilfredkisku/pseudocompression-algo/blob/main/res/processed_image_normal.png" height="200"></p>|<p align="center"><img src="https://github.com/wilfredkisku/pseudocompression-algo/blob/main/res/processed_image_thermal.png" height="200"></p>|

Status: Completed
