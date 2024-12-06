from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'Acessar o site joga junto')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org")
    time.sleep(2)

@when(u'insiro meus dados')
def step_impl(context):
    context.driver.find_element(By.NAME , "email").send_keys("michaelgomesde.s4@gmail.com")
    
  


@then(u'clicar no botão entrar')
def step_impl(context):
    context.driver.find_element(By.NAME , "password").send_keys("Tapioca@2"+Keys.RETURN)
    time.sleep(3)

