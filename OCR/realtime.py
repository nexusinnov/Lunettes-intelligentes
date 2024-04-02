import cv2
import easyocr
import threading

from OCR.voix import read_proprietary_text


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
    frensh = False
    reader = easyocr.Reader(['en', 'ar'])
    results = 0
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame")
            break
        if i == 0:
            results = reader.readtext(frame, detail=0, paragraph=True)
            i = 1
        for result in results:
            if not any('\u0600' <= char <= '\u06FF' for char in result):
                frensh = True
        if frensh:
            reader = easyocr.Reader(['en', 'fr'])
            results = reader.readtext(frame, detail=0, paragraph=True)
        else:
            reader = easyocr.Reader(['en', 'ar'])
            results = reader.readtext(frame, detail=0, paragraph=True)
        for result in results:
            text = result.strip()
            if frensh:
                print("English/French:", text)
                read_proprietary_text(text=text, language='fr')
            else:
                print("English/Arabic:", text)
                read_proprietary_text(text=text, language='ar')
        frensh = False


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

    capture_thread.start()
    ocr_thread.start()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture_thread.join()
    ocr_thread.join()

    cap.release()
    cv2.destroyAllWindows()


capture_and_ocr()
