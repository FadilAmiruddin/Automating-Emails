from selenium import webdriver
sendinfo()
link = link to website
def sendinfo(a,b):
    b = webdriver.Chrome(executable_path="C://Users//Real fadil//AppData//Local//Temp//Rar$EXa10172.3678//chromedriver.exe")

    b.get(link)
    b.find_element_by_name("first-name").send_keys("Fadil")
    b.find_element_by_name("last-name").send_keys("Amiruddin")
    b.find_element_by_name("email").send_keys("fadil.amiruddin1@gmail.com")
    b.find_element_by_name("phone").send_keys("571-268-1941")
    b.find_element_by_name("company").send_keys("Troop 786	")
    b.select(b)
    b.find_element_by_name("your-message").send_keys("Hello " + a + " I am working to create a project for a non profit orginzation and I will need you're donations to do so. Any amount will be appreaited thanks fadil )
    b.find_element_by_name("submit").submit()
