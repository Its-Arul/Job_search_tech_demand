from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

edge_driver_path = "C:\Development\msedgedriver.exe"
tech_demand = []

service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://www.naukri.com/sap-abap-developer-jobs")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(time_to_wait=20) # gives an implicit wait for 20 seconds
close_popover = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div').click()
test = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/section[2]/div[2]')
children = test.find_elements(By.XPATH, './/article')
for n in children:
    job = n.find_elements(By.XPATH, './ul')
    for each_job in job:
        print(each_job.text)
        tech_demand.append(each_job.text)


for n in range(2, 40):
    driver.get(f"https://www.naukri.com/sap-abap-developer-jobs-{n}")
    driver.maximize_window()  # For maximizing window
    # driver.implicitly_wait(time_to_wait=20)  # gives an implicit wait for 20 seconds
    # close_popover = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div').click()
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                '//*[@id="root"]/div[3]/div[2]/section[2]/div[2]/article[20]/div[2]')))
    test = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/section[2]/div[2]')
    children = test.find_elements(By.XPATH, './/article')

    for n in children:
        job = n.find_elements(By.XPATH, './ul')
        for each_job in job:
            print(each_job.text)
            tech_demand.append(each_job.text)

tech_demand_split = []
tech_demand_final = []
for n in tech_demand:
    each_word = n.split("\n")
    tech_demand_split.append(each_word)



print(len(tech_demand))
print(tech_demand)
print(tech_demand_split)

for n in range(len(tech_demand_split)):
    for n1 in range(len(tech_demand_split[n])):
        tech_demand_final.append(tech_demand_split[n][n1].lower())

print(tech_demand_final)
print(len(tech_demand_final))
res = {}
for n in tech_demand_final:

    res[n] = tech_demand_final.count(n)

for w in sorted(res, key=res.get, reverse=True):
    print(w, res[w])

print(res)


