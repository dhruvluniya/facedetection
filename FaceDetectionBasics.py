import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("FaceVideos/1.mp4")
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

while True:
    success, img = cap.read()
    resized = cv2.resize(img, (800, 500))
    imgRGB = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img,detection)
            # print(id,detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 6)
            cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-20),
                        cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 255), 5)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    resized = cv2.resize(img, (800, 500))
    cv2.putText(resized, f'FPS:{int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", resized)
    cv2.waitKey(20)
