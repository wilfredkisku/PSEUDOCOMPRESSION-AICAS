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

## Results
