import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO

class ObjectDetection:
   
      def __init__(self, capture_index):
            self.capture_index = capture_index
            self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
            print('using device: ',self.device)

            self.model = self.load_model()
            
      def load_model(self):
            model = YOLO('yolov8x-oiv7.pt')
            model.fuse()
            return model
      
      def predict(self, frame):
            results = self.model(frame)
            return results
      
      def plot_bboxes(self, results):
            xyxys = []
            confidences = []
            class_ids = []
            

            for result in results:
                  boxes = result.boxes.cpu().numpy()
                  xyxys.append(boxes.xyxy)
                  confidences.append(boxes.conf)
                  class_ids.append(boxes.cls)
            for result in results:
              class_names = result.names
              for ids in class_ids:
                 for idx, class_id in enumerate(ids):
                    class_name = class_names[int(class_id)]
                    print(f"{class_name} detected with confidence: {confidences[0][idx]}")
    
            return results[0].plot(), xyxys, confidences, class_ids
           
      def __call__(self):

        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
      
        while True:
          
            start_time = time()
            
            ret, frame = cap.read()
            assert ret
            
            results = self.predict(frame)
            plotted_frame, xyxys, confidences, class_ids = self.plot_bboxes(results)
            
            
            
            
            end_time = time()
            fps = 1/np.round(end_time - start_time, 2)
             
            cv2.putText(plotted_frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow('YOLOv8 Detection', plotted_frame)
            if cv2.waitKey(5) & 0xFF == 27:
                
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
        
    
detector = ObjectDetection(capture_index=0)
detector()