import face_recognition
import cv2
import numpy as np
import time 

username = None

class facerec_from_webcam(object):

    def faceRecognition(self, parent=None):
        video_capture = cv2.VideoCapture(0)

        # 載入樣本
        Aclassmate_image = face_recognition.load_image_file("./known_people/A_classmate.jpg")
        Aclassmate_face_encoding = face_recognition.face_encodings(Aclassmate_image)[0]

        Bclassmate_image = face_recognition.load_image_file("./known_people/B_classmate.jpg")
        Bclassmate_face_encoding = face_recognition.face_encodings(Bclassmate_image)[0]

        #建立矩陣，存放“編碼方式”
        known_face_encodings = [
            Aclassmate_face_encoding,
            Bclassmate_face_encoding
        ]
        #建立矩陣，存放“人名”
        known_face_names = [
            "Aclassmate",
            "Bclassmate"
        ]

        global username
        username = "Unknown"
        
        while True:
            
            ret, frame = video_capture.read()

            #將圖像從BGR顏色（OpenCV使用）轉換為RGB顏色（face_recognition使用）
            rgb_frame = frame[:, :, ::-1]

            #查找視頻幀中的所有人臉和編碼
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

                #查看人臉是否與已知人臉匹配
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                
                # 或是找個最類似的臉來替代
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    username = known_face_names[best_match_index]
                    print('name:'+username)
                
                #畫框
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) 

                #顯示標籤
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, username, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            if (username != "Unknown"):
                #cv2.imshow('Video', frame)
                frame = cv2.resize(frame,(640,360))
                cv2.imwrite("./NEWpic.png", frame)
                cv2.destroyAllWindows()
                video_capture.release()
                break
            # cv2.destroyAllWindows()
            # video_capture.release()
    
    def nameback(self):
        return username
