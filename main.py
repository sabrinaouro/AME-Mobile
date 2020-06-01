from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "br.com.dudstecnologia.cadastrodeclientes"
caps["appActivity"] = "br.com.dudstecnologia.cadastrodeclientes.MainClientes"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

allow_button = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
allow_button.click()

def abrirNovoCadastro():
    TouchAction(driver).tap(x=946, y=1640).perform()
    time.sleep(3)
    TouchAction(driver).tap(None, 949, 1150, 1).perform()

def cadastro():
    nome = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editNome")
    nome.send_keys("Sabrina Ouro")
    rg = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editRg")
    rg.send_keys("215215152")
    cpf = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editCpf")
    cpf.send_keys("00202020202")
    data_nasc = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editData")
    data_nasc.send_keys("04071990")
    endereco = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editEndereco")
    endereco.send_keys("Rua D")
    casa = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editNumero")
    casa.send_keys("2202")
    bairro = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editBairro")
    bairro.send_keys("Sao Lazaro")
    cep = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editCep")
    cep.send_keys("69000000")
    cidade = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editCidade")
    cidade.send_keys("Manaus")
    TouchAction(driver).tap(x=916, y=992).perform()
    time.sleep(2)
    TouchAction(driver).tap(x=873, y=1253).perform()
    save_button = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/btnSalvar")
    save_button.click()
    confirm = driver.find_element_by_id("android:id/button1")
    confirm.click()

def exportarExcel():
    TouchAction(driver).tap(x=946, y=1635).perform()
    el2 = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/floating_exportar")
    el2.click()
    TouchAction(driver).tap(x=504, y=290).perform()

def backup():
    TouchAction(driver).tap(x=891, y=1072).perform()
    TouchAction(driver).tap(x=947, y=1635).perform()
    TouchAction(driver).tap(x=510, y=412).perform()

def excluirCadastro():
    cliente = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/nomeLista")
    cliente.click()
    exclude_btn = driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/btnExcluir")
    exclude_btn.click()
    confirm = driver.find_element_by_id("android:id/button1")
    confirm.click()

def restaurarBackup():
    TouchAction(driver).tap(x=891, y=1072).perform()
    TouchAction(driver).tap(x=944, y=1286).perform()
    TouchAction(driver).tap(x=515, y=545).perform()

abrirNovoCadastro()
cadastro()
driver.back()
exportarExcel()
driver.back()
excluirCadastro()
driver.back()
backup()
driver.back()
restaurarBackup()


driver.quit()