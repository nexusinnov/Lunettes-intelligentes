import cv2
import easyocr
import threading

languages = ["en",'ar','fr','af']
reader = easyocr.Reader(languages)


def capture_frames(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame")
            break
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def perform_ocr(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame")
            break
        result = reader.readtext(frame, detail=0, paragraph=True)
        print(result)


def capture_and_ocr():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Create threads for camera capture and OCR processing
    capture_thread = threading.Thread(target=capture_frames, args=(cap,))
    ocr_thread = threading.Thread(target=perform_ocr, args=(cap,))

    # Start the threads
    capture_thread.start()
    ocr_thread.start()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Wait for threads to finish
    capture_thread.join()
    ocr_thread.join()

    cap.release()
    cv2.destroyAllWindows()


capture_and_ocr()
