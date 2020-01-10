# Road-Lane-Finding-Using-Flask


#### Advanced Lane Detection Project which includes advanced image processing to detect lanes irrespective of the road texture, brightness, contrast, curves etc. Used Image warping and sliding window approach to find and plot the lane lines.

#### Application Structure:


    ├── /camera_cal  
    ├── /static                    
    ├── /templates                 
    ├── /test_images                    
    ├── main.py                   
    ├── app.yaml
    ├── requirements.txt
    └── README.md
    

#### The Steps Involved are:

1. Computing the camera calibration matrix and distortion coefficients given a set of chessboard images. (9x6)
2. Apply a distortion correction to raw images.
3. Use color transforms, gradients, etc., to create a thresholded binary image.
4. Apply a perspective transform to rectify binary image ("birds-eye view") to get a warped image.
5. Detect lane pixels and fit to find the lane boundary.
6. Warp the detected lane boundaries back onto the original image.
