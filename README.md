# Road-Lane-Finding-Using-Flask


#### Advanced Lane Detection Project which includes advanced image processing to detect lanes irrespective of the road texture, brightness, contrast, curves etc. Used Image warping and sliding window approach to find and plot the lane lines.

#### Deployment:

The Flask Application is deployed over Google Cloud Platform. https://lane-finding.appspot.com

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

#### Packages Used:

1. Flask==1.1.0
2. gunicorn==19.6.0
3. pandas==0.22.0
4. numpy==1.11.2
5. scipy==0.18.1
6. scikit-learn>=0.18
7. opencv-python==3.1.0.4


#### Pipeline:

##### Camera Calibration:

The first step in the pipeline is to undistort the camera. Some images of a 9x6 chessboard are given and are distorted. Our task is to find the Chessboard corners an plot them. For this, after loading the images we calibrate the camera. Open CV functions like findChessboardCorners(), drawChessboardCorners() and calibrateCamera() help us do this.

##### Undistortion of Input Image:

The images uploaded are initially undistorted using cv2.undistort() which takes in an image and returns the undistorted one.

#### Screenshots:


##### Upload Form:

![Screenshot from 2020-01-10 11-05-51](https://user-images.githubusercontent.com/34116562/72128639-928dc980-3399-11ea-9e6a-429f6dff8042.png)
![Screenshot from 2020-01-10 11-06-02](https://user-images.githubusercontent.com/34116562/72128642-93bef680-3399-11ea-9158-928453101e2a.png)

##### Success Form:

![Screenshot from 2020-01-10 11-07-24](https://user-images.githubusercontent.com/34116562/72128644-9588ba00-3399-11ea-9d55-802e535dbde1.png)
![Screenshot from 2020-01-10 11-07-32](https://user-images.githubusercontent.com/34116562/72128646-97527d80-3399-11ea-9eae-404c9b3acc5f.png)

##### Input Image:

![Screenshot from 2020-01-10 11-07-37](https://user-images.githubusercontent.com/34116562/72128648-991c4100-3399-11ea-82c4-3367aceb3b4c.png)

##### Output Image:

![Screenshot from 2020-01-10 11-07-42](https://user-images.githubusercontent.com/34116562/72128649-99b4d780-3399-11ea-974c-17640eb19489.png)

##### Source Code:

![Screenshot from 2020-01-10 11-07-50](https://user-images.githubusercontent.com/34116562/72128652-9c173180-3399-11ea-9759-503b79727b25.png)
