import boto3 
import cv2
from cvzone.HandTrackingModule import HandDetector 

cap = cv2.VideoCapture(0)

status , photo = cap.read()
print(status)


cv2.imshow("haha",photo)
cv2.waitKey(5000)
cv2.destroyAllWindows()



detector = HandDetector()
lmlist = detector.findHands(photo)
handlmlist = lmlist[0][0]

fingersup = detector.fingersUp(handlmlist)
print(fingersup)




def launchIt():
    accessKey = "AKIAYEK"  #access key of your aws credentials
    secretKey = "TC4fJ6gBuIohy/jBhoZLtupWbsR2"   #secret access key of your aws credentials
    regionName = "ap-south-1"    #region in which you want to create vms
    
    myec2 = boto3.resource( "ec2", aws_access_key_id = accessKey , aws_secret_access_key = secretKey , region_name = regionName)

    # Define instance details
    instance_type = 't2.micro'
    image_id = 'ami-0402e56c0a7afb78f' # Replace with a valid AMI ID
    
    # Launch the instance
    response = myec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
    )


    
if(fingersup == [0,0,0,0,0]):
    print("no instance has launched")
else:
    for i in fingersup:
        if i == 1:
            launchIt()
            print("launched a VM")
