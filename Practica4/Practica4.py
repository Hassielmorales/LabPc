import base64
import sys

with open("Img1.jpg", "wb") as fh:
  fh.write(base64.urlsafe_b64decode('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'))

with open ("img2.jpg","wb") as fh:
    fh.write(base64.urlsafe_b64decode('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'))



with open('hola_mundo.c') as f:
    file_to_encode = f.read().encode('utf-8')

with open('hola_cifrado,txt', 'w') as f:
    f.write(file_to_encode.decode('utf-8'))
