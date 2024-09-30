#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:39:26 2024

@author: alejoGironza
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import glob
import time


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



"""from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
    "download.default_directory" : "/Users/stephaniecardona/Documents/ALEJANDRO/PythonDownloads"
    } )
"""

driver = webdriver.Chrome()

#pagina a la cual tomaremos los datos
driver.get("https://community.secop.gov.co/Public/App/AnnualPurchasingPlanManagementPublic/Index?currentLanguage=en&Page=login&Country=CO&SkinName=CCE")



#para hacer la pantalla de chrome completa
driver.maximize_window()

#se setean los valores iniciales para comenzar la descarga
pagina_inicial=0
inicial = pagina_inicial*5
final = inicial + 5 

#directorio en el que se guardaran los archivos
path_archivos = '/Users/stephaniecardona/Documents/ALEJANDRO/PythonDownloads'


#funcion para descargar los archivos
def descargar(inicial, final):
    for j in range(inicial, final):
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
                                                      
        driver.find_element(By.XPATH,'//*[@id="lnkGridAppDownloadLink_'+str(j)+'"]').click()
        time.sleep(12)
    
    
        filename = max(glob.glob(path_archivos), key=os.path.getctime)
        print(filename)
        
 
#llamada incial de descarga para la primera página        
descargar(inicial, final)  
time.sleep(1)


while True:
    
    pagina_inicial= pagina_inicial + 1
    inicial = pagina_inicial*5
    final = inicial + 5 
    
       
    if not pagina_inicial%2==0:
        print("pagina siguinte ---")
        driver.find_element(By.XPATH,'//*[@id="grdGridAPP_Paginator_goToPage_Next"]').click()
        time.sleep(2)
        descargar(inicial, final)
        
    else:
        print("3 puntos ---")
        driver.find_element(By.XPATH,'//*[@id="grdGridAPP_Paginator_goToPage_MoreItems"]').click()
        time.sleep(2)
        descargar(inicial, final)
        

print("Finished")

driver.close()
