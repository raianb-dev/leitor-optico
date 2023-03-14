from textblob import TextBlob
import re, pytesseract, cv2

# carregar a imagem
imagem = cv2.imread('Capture.jpg')

# pré-processamento da imagem
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
binarized = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
resized = cv2.resize(binarized, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# extrair o texto da imagem
texto = pytesseract.image_to_string(resized, lang="por")



# criar um objeto TextBlob com o texto
blob = TextBlob(texto)

# extrair nomes próprios do texto usando o TextBlob
'''
nomes_proprios = [palavra.title() for palavra, tipo in blob.tags if tipo == 'NNP']
nomes_completos = " ".join(nomes_proprios)
# buscar as datas no texto usando regex
datas = re.findall(r"\d{2}/\d{2}/\d{4}", texto)
'''

print(texto)

