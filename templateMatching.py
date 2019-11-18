# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True, help="Path to the source image")
ap.add_argument("-t", "--template", required=True, help="Path to the template image")
args = vars(ap.parse_args())

#load source and template image
source = cv2.imread(args["source"])
template = cv2.imread(args["template"])
(tempH, tempW) = template.shape[:2]

#find template in source image
result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF)
(minVal, maxVal, minLoc, (x, y)) = cv2.minMaxLoc(result)

#draw bounding box on source image
cv2.rectangle(source, (x, y), (x + tempW, y + tempH), (0, 255, 0), 2)

#show the images
cv2.imshow("Source", source)
cv2.imshow("Template", template)
cv2.waitKey(0)
