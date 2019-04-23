# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps.

Step 1: convert the images to grayscale. The RGB color information is not used to determine lines because
light condition varies a lot due to different weather.

![alt text][image1]

Step 2: use gaussian filter to blur the image. It is useful to make next step (edge detection) result more smooth. Otherwise there will be a lot spikes on the edge and can be easily removed by max threshold.

Step 3: use canny edge detection to select image pixels that have high variance with its neighbor.

Step 4: select a polygon region of the image (the bottom) and filter out edegs in step 3 outside of this interested area. 

Step 5: use hough line detection algorithm to find lines according to selected edges points.


In order to draw a single line on the left and right lanes, I modified the draw_lines() function by examing each line, select ones that has reasonable position and slope, extend it to the bottom of the image.


### 2. Identify potential shortcomings with your current pipeline


1. The draw line function may result in a top small, bottom fat shape.
2. The interested region selection is hardcoded, if camera is moved a little, the result would be wrong.
3. Due to curves on the road, the resulting line may not be a straight line.
4. Canny function may not be stable if light condition is bad. The hard coded min and max threshold may not work.
5. Hough function max points threshold, and min line distance threshold may not work for cases like broken line mark.


### 3. Suggest possible improvements to your pipeline

1. Use linear regression to find the resulting line, rather than simply extend each line.
2. Detect the edge of sky and road, and use that as interested region separation.
3. Tune parameter of canny and hough algorithm with more input data.
