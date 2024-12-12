# Importing Required Libraries
import cv2                                              ## python -m pip install opencv-python==4.10.0.84
from deepface import DeepFace                           ## python -m pip install deepface==0.0.92

# Access System Camera
cam = cv2.VideoCapture(0)

while True:
    # Getting Camera Frame
    ret, frame = cam.read()

    if ret:

        try:
            # Mirroring the camera frame
            frame = cv2.flip(frame,1)

            # Extracting coordinates for face bounding box using DeepFace
            res = DeepFace.extract_faces(frame)

            # Extracting face confidence value from the result
            confidence = "Face Confidence : " + str(int(res[0]['confidence']*100)) + "%"
            #print(confidence)

            # Extracting bounding box origin and width & height of the face
            #print(res[0]['facial_area'])
            x = res[0]['facial_area']['x']
            y = res[0]['facial_area']['y']
            w = res[0]['facial_area']['w']
            h = res[0]['facial_area']['h']

            # Drawing Text and Bounding Box on the Frame
            cv2.rectangle(frame, (50,35),(250,55),(0,0,0),-1)
            cv2.putText(frame, confidence, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)      
            cv2.rectangle(frame, (x,y),(w+x,h+y),(0,255,0),2)

            # Display Window using OpenCV
            cv2.imshow("Face Detection using DeepFace ", frame)

        except:
            # If the face is not front face then the text will be displayed
            cv2.putText(frame, "Face Front ", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)

    if cv2.waitKey(1) & 0xFF == ord('q'):      # Press "q" to stop the face detection
        break

# Release the camera and destory all the windows used by OpenCV
cam.release()
cv2.destroyAllWindows()

