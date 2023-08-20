
import pytesseract
import cv2
PATH_IMAGE="images/"
IMAGE="02-V.jpeg"
#IMAGE="01-V.jpeg"
#IMAGE="01-V-T.jpg"

#IMAGE="01-V-V.jpg"
imagem = cv2.imread(PATH_IMAGE+IMAGE)
imagem2=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
custom_oem_psm_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
#texto = pytesseract.image_to_osd(imagem)

texto = pytesseract.image_to_string(imagem, lang="por",config=custom_oem_psm_config) #
#print(pytesseract.image_to_boxes(Image.open(PATH_IMAGE+IMAGE)))

#print(pytesseract.get_languages(config=''))
#print(texto)

print(texto)

#Identificando Cores antes de aplicar o filtro de gray.
#O Filtro é melhor aplicado para versos de cartões que estão na cor amarelo.
# https://acervolima.com/identificacao-de-cores-em-imagens-usando-python-opencv/
# Site mostrando como identificar cores.