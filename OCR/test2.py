import easyocr
reader = easyocr.Reader(["en"])
result = reader.readtext('images/hello.jpeg', detail=0, paragraph=True)
print(result)

