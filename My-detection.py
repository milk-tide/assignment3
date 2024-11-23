import jetson.inference
import jetson.utils
import IPython
from jetson.inference import detectNet
from jetson.utils import videoSource, videoOutput
from jetson.utils import loadImage, saveImage
from IPython import display
net = detectNet("ssd-mobilenet-v2", threshold=0.5)
img = loadImage("img_4.jpg")
detections = net.Detect(img)

if len(detections) > 0:
	detection = detections[0]
print(detection) 

saveImage("img_d4.jpg", img)

#camera = videoSource("/dev/video0") 
#display = videoOutput("display://0") 
#while display.IsStreaming():
# img = camera.Capture()
# if img is None: # capture timeout
#    continue
# detections = net.Detect(img)
