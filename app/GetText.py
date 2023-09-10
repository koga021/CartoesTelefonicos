
import pytesseract
import cv2
import GetInfo as g

PATH_IMAGE="images/"
#IMAGE="02-V.jpeg"
#IMAGE="01-V.jpeg"
#IMAGE="01-V-T.jpg"
IMAGE="04-V.jpeg"

def GetTextFromImage(image_file):
    #IMAGE="01-V-V.jpg"
    imagem = cv2.imread(PATH_IMAGE+image_file)
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
    ## Limiarização de imagens, pode ser feito aqui.
    # https://www.youtube.com/watch?v=1lkOTltVsQ8&list=PLZ3V9XyVA52_rzo8EeR07To8tvLk7JXlS&index=25
    # limiarizacao simples ou automatica.
    # Automatica = metodo de Otsu

    unidades=g.SearchUnidades(texto)
    print(unidades)

    data={'unidades':unidades}
    #print(data)
    return(data)