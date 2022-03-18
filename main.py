from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


edge_driver_path = "C:\Development\msedgedriver.exe"

website = "https://www.naukri.com/firmware-engineer-jobs"
tech_demand = []

service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)


def extract_jobs(page_no):

    driver.get(f"{website}-{page_no}")
    driver.maximize_window()  # For maximizing window:
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    if n == 1:
        WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                    '/html/body/div[3]/div/div[1]/div[1]/div')))

        button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/div')
        driver.implicitly_wait(10)
        button.click()

    else:

        WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                    '//*[@id="root"]/div[3]/div[2]/section[2]/div[2]/'
                                                                    'article[20]/div[2]')))
    test = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/section[2]/div[2]')
    children = test.find_elements(By.XPATH, './/article')
    return children


def extract_technology_from_job(page_number):
    children = extract_jobs(page_number)
    for child in children:
        job = child.find_elements(By.XPATH, './ul')
        for each_job in job:
            print(each_job.text)
            tech_demand.append(each_job.text)

#----------------------------------------------START----------------------------------------------------------------#


# Loop through each page
for n in range(1, 30):
    extract_technology_from_job(page_number=n)


#-------------------------------------ENHANCING DATA ----------------------------------------------------------------#
tech_demand_split = []
tech_demand_final = []

# Split the demand list into each word
for n in tech_demand:
    each_word = n.split("\n")
    tech_demand_split.append(each_word)

# Create a new list with all the technologies demanded
for n in range(len(tech_demand_split)):
    for n1 in range(len(tech_demand_split[n])):
        tech_demand_final.append(tech_demand_split[n][n1].lower())

print(len(tech_demand_final))

# Sorting the list from highest to lowest
res = {}
for n in tech_demand_final:
    res[n] = tech_demand_final.count(n)

sorted_dict = {}
for w in sorted(res, key=res.get, reverse=True):
    sorted_dict[w] = res[w]

print(sorted_dict)

#-------------------------------------------FINISH------------------------------------------------------------------#
