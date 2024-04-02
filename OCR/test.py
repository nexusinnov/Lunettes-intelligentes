import easyocr
from voix import read_proprietary_text

reader = easyocr.Reader(["fr"])
results = reader.readtext('captured_photo.jpg', detail=0, paragraph=True)
for result in results:
    read_proprietary_text(text=result.strip(), language='fr')
    print(result.strip())
