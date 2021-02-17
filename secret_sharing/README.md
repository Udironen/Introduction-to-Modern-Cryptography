This code implements visual secret sharing for images:
Select 3 black and white images A, B and C of the same dimensions.
The code will generates two encoded images ~A and ~B whose dimensions are twice those of the original images. Let ~C be
the encoded image that results from placing ~A and ~B on top of each other when white pixels are
transparent. That is, each pixel in ~C is white if and only if the pixels of ~A and ~B in the same location
are both white. Each encoded image should resemble the original image, but contain no information
about the two other images.
