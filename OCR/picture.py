import cv2
import easyocr
from voix import read_proprietary_text


def perform_ocr_on_image(image):
    frensh = False
    reader = easyocr.Reader(['en', 'ar'])

    results = reader.readtext(image, detail=0, paragraph=True)

    for result in results:
        if not any('\u0600' <= char <= '\u06FF' for char in result):
            frensh = True

    if frensh:
        reader = easyocr.Reader(['en', 'fr'])
        results = reader.readtext(image, detail=0, paragraph=True)
    else:
        reader = easyocr.Reader(['en', 'ar'])
        results = reader.readtext(image, detail=0, paragraph=True)

    for result in results:
        text = result.strip()
        if frensh:
            print("English/French:", text)
            read_proprietary_text(text=text, language='fr')
        else:
            read_proprietary_text(text=text, language='ar')
            print("English/Arabic:", text)


def capture_and_ocr():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame")
            break

        cv2.imshow('Press "s" to take a photo', frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite("captured_photo.jpg", frame)
            break

    cap.release()
    cv2.destroyAllWindows()

    photo = cv2.imread("captured_photo.jpg")
    perform_ocr_on_image(photo)


capture_and_ocr()
