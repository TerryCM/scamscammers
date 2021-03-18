from selenium import webdriver

import time
import numpy as np
import random
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

web = webdriver.Chrome()
web.get('https://bancaporinternet.bbva.pe.kmfpayroll.com/bdntux_pe_web/bdntux_pe_web')
time.sleep(5)

random_dni = [random_with_N_digits(9) for i in range(50)]

lines_list = open('diccionario.txt').read().splitlines()
lines_list= list(filter(lambda x: len(x)<=9 and len(x)>=6, lines_list))
lines_list = np.random.choice(lines_list, 50, replace=False)
lines_list = lines_list.tolist()

dni_picked = []
pass_picked = []


for i in range(50):
    web.switch_to.window(web.window_handles[0])
    time.sleep(5)
    dni = random.choice(random_dni)
    contra = random.choice(lines_list)
    number = 924996037
    dni_path = web.find_element_by_xpath('//*[@id="txteai_user"]')
    dni_path.send_keys(dni)
    contra_path = web.find_element_by_xpath('//*[@id="txteai_password"]')
    contra_path.send_keys(contra)
    submit = web.find_element_by_xpath('//*[@id="btnEntrar"]')
    random_dni.pop(random_dni.index(dni))
    lines_list.pop(lines_list.index(contra))
    submit.click()
    time.sleep(5)
    web.switch_to.window(web.window_handles[-1])
    try:
        number_path = web.find_element_by_xpath('//*[@id="celular"]')
        number_path.send_keys(number)
        submit_number = web.find_element_by_xpath('//*[@id="btnAddCorreoDatosPersonales"]')
        submit_number.click()
    except:
        pass
    
    
 
    



