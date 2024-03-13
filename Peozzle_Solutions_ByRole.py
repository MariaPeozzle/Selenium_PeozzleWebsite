import Property_Peozzle_Solutions_ByRole
import pandas as pd
import time
import unittest
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Peozzle_Solutions_ByRole:
    results = {}
    role_list = ["Talent Manager",
                 "Recruiter",
                 "Account Manager",
                 "Placement Officer",
                 "Volunteer",
                 "Volunteer Administrator"
                 ]

    for role_list in role_list:
        print("Peozzle Solution By Role: " + role_list)
        Property_Peozzle_Solutions_ByRole.solutions_ByRole(role_list)


