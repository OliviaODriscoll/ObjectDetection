# Object Detection
1. Download this repository
2. Create dataset 
    * I used YoloLabel, available here: https://github.com/developer0hye/Yolo_Label
    * put your images in /path/to/Yolov3-Training-Tool-Detector/JPEGImages
    * put .txt files in /path/to/Yolov3-Training-Tool-Detector/labels
3. Create train/test split using command `python3 splitTrainAndTest.py /path/to/Yolov3-Training-Tool-Detector/JPEGImages`
4. Download darknet
     ```batch
         cd ~
         git clone https://github.com/pjreddie/darknet
         cd darknet
         make 
      ```
      * compile darknet with GPU and CUDNN settings configured to match your system (default is no GPU)
5. Download pre-trained model
    * ```batch
      cd ~/darknet
      wget https://pjreddie.com/media/files/darknet53.conv.74 -O ~/darknet/darknet53.conv.74
      ```
6. Modify darknet.data as necessary
    ```data
      classes = 1
      train  = /path/to/tool_train.txt
      valid  = /path/to/tool_test.txt
      names = /path/to/classes.names
      backup = /path/to/weights/
    ```
7. Modify darknet-yolov3.cfg as necessary
    * you may need to modify batch size, image dimensions, etc...
8. Train 
```batch
      cd ~/darknet
      ./darknet detector train /path/to/images/darknet.data /path/to/images/darknet-yolov3.cfg ./darknet53.conv.74 > /path/to/images/train.log
```
9. Test model using command `python3 object_detection_yolo.py --image=snowmanImage.jpg`

