## What are images?
- An image is a matrix of data points which have a relationship to each other on a 2D or 3D grid
- Each data point is a pixel in the image
    - The point contians the value of the color in the color space that the pixel is using

## Pixels
- Each pixel represents a point in an image and hold values for the color in that pixel
    - Depending on the color space, a pixel will contain 1 or 3 values
        - One for each color channel: Red, Blue, Green
            - There are several other color spaces that use 3 channels, but you won't come across them often
        - Grayscale contains on one color
- The maximum value for any color is 255
    - The value is limited to a single byte in storage
    - A byte is made up of 8 bits
        - A bit can be 1 of 2 values (0, 1)
        - Therefore a byte is 2^8 = 256
        - Including the 0 value, the max is 255

## Analyzing images
- By applying mathematical operations to an image we can identify structures or modify an image
- For example if we compare the value of a pixel to that of its neighbors we might be able to identify a line 

### Neighborhoods
- There are two pixel 'neighborhoods' to consider when analyzing an image
    - 4 neighbor
    - 8 neighbor

### Resizing an image
- Reducing the size of an image is fairly simple, pixel values are removed and a smaller collection of pixels is recorded
    - This is done to make thumbnails
- Increasing the size of an image is more complex because information must be inferred
    - A simple way to increase the size of an image is called nearest-neighbor interpolation
        - New pixel values are copied from their nearest neighbor
        - This creates square artifiacts in the image that make it look pixelated
    - More complex ways use 'convolution' to interpolate the missing values
        - 'Convolution', when in the context of data science, means that a region of data is fed into a function to create a value
        - Gives a more realistic and smoother appearance
