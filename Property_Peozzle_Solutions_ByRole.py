import email_report_selenium
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # Import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def solutions_ByRole(rolename):
    # Initialize Chrome WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Set the service object
    service = Service(ChromeDriverManager().install())

    # Initialize Chrome WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the website
    driver.get('https://www.peozzle.com/')
    time.sleep(10)

    results = {}
    # results["Background image1"] = "Present"
    results["1. Ensure Navigating to 'Peozzle website'"] = "Passed"

    # df = pd.DataFrame(columns=['A','B'])

    # df = pd.DataFrame(columns={"Element", "Test Result"})

    # ----------------------------------------------------------------
    # Next, from Product Dropdown navigate to Peozzle Campus portal

    # Wait for the element to be visible
    product_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Solutions")))

    # Perform mouseover action to Products
    ActionChains(driver).move_to_element(product_element).perform()
    time.sleep(5)
    try:
        hire = driver.find_element(By.LINK_TEXT, rolename)
        ActionChains(driver).move_to_element(hire).click().perform()
        time.sleep(5)
        print("Tc2: Navigated to 'Peozzle Solution' ")
        # results["Navigated to 'Peozzle Campus'"] = "Passed"
        results["2. Ensure Navigating to 'Peozzle solutions website'"] = "Passed"



    except NoSuchElementException:
        print("Element 'Peozzle solutions' not found.")
        # results["Navigated to 'Peozzle Campus'"] = "Failed"
        results["2. Ensure Navigating to 'Peozzle solutions website'"] = "Failed"

    # ------------------------------------

    text_contents = ["Talent Manager",
                     "Recruiter",
                     "Account Manager",
                     "Placement Officer",
                     "Volunteer",
                     "Volunteer Administrator"
                     ]

    for text_content in text_contents:
        try:
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            print(f"Text content '{text_content}' is present on the webpage.")
            results["3. Ensure text content is available"] = "passed"

        except NoSuchElementException:
            print(f"Text content '{text_content}' is not present on the webpage.")
            results["3. Ensure text content is available"] = "Failed"

    # ------------------------------------------

    text_contents = [
        "Oversee the organization’s talent acquisition process and help your clients source, hire the right talent seamlessly and build long-term relationships with stakeholders.",
        "Oversee a portfolio of your Agency customers, grow your business, establish a purpose-built partner network, and continuously engage with your candidates, partners, and clients.",
        "Help your students to realize their career goals, orchestrating your institution’s placement, alumni management, and compliance reporting process.",
        "Connect and Engage with the Non-Profits to serve the needy organization that utilizes your skills and aligns with your interests and aspirations.",
    ]

    for text_content in text_contents:
        try:
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            print(f"Text content '{text_content}' is present on the webpage.")
            results["4. Ensure text content is available"] = "passed"

        except NoSuchElementException:
            print(f"Text content '{text_content}' is not present on the webpage.")
            results["4. Ensure text content is available"] = "Failed"

    # ------------------------------------------------

    # HOme Image availability check

    try:
        # Check Home Button
        elements = driver.find_elements(By.LINK_TEXT, "Home")
        assert len(elements) > 0
        if len(elements) > 0:
            print("Home Image is found")
            results["5. Ensure Home icon is available"] = "Passed"

        else:
            print("Home Image is missing")
            results["5. Ensure Home icon is available"] = "Failed"

    except NoSuchElementException:
        print("Home Image is not found")
        results["5. Ensure Home icon is available"] = "Failed"

    # ---------------------------
    try:

        # Check Search button
        elements = driver.find_elements(By.CSS_SELECTOR, ".wgl-header-row:nth-child(2) .header_search-button")
        if len(elements) > 0:
            print("Search Image is found")
            results["6. Ensure Search icon is available"] = "Passed"

        else:
            print(" Search is missing")
            results["6. Ensure Search icon is available"] = "Failed"

    except NoSuchElementException:
        print("search Image is not found")
        results["6. Ensure Search icon is available"] = "Failed"

    # -----------------------------------------------------
    # Peozzle logo check

    # logo_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@class="default_logo"]')))

    logo_element = driver.find_elements(By.CSS_SELECTOR, ".position_left_middle .default_logo")
    try:

        # Check for Peozzle logo

        if len(logo_element) > 0:
            print(" Logo is present on the webpage.")
            results["7. Ensure Peozzle logo is available"] = "Passed"

        else:
            print("Logo is not present on the webpage.")
            results["7. Ensure Peozzle logo is available"] = "Failed"

    except NoSuchElementException:
        print("Peozzle logo is not found")
        results["7. Ensure Peozzle logo is available"] = "Failed"

    # -----------------------------------------------------
    # Phone number availability

    phonenumber = driver.find_element(By.XPATH, "//span[contains(.,\' (763) 442-8468\')]")

    try:
        if phonenumber:
            print(" Phone number (763) 442-8468  is present on the webpage.")
            results["8 Ensure Phone number is available"] = "Passed"

        else:
            print(" Phone number (763) 442-8468  is not present on the webpage.")

            results["8. Ensure Phone number is  available"] = "Failed"

    except NoSuchElementException:
        print(" Phone number is not found")
        results["8. Ensure Phone number is available"] = "Failed"

    # ---------------------------------------
    # Social media in header
    try:

        elements = driver.find_elements(By.CSS_SELECTOR, ".connectButton > .fa-twitter")
        if len(elements) > 0:
            print("Twitter logo is available in header")
        else:
            print("Twitter logo is not available in header")
        elements = driver.find_elements(By.CSS_SELECTOR, ".fa-facebook")
        if len(elements) > 0:
            print("Facebook logo is available in header")
        else:
            print("Facebook logo is not available in header")
        elements = driver.find_elements(By.CSS_SELECTOR, ".fa-linkedin:nth-child(1)")
        if len(elements) > 0:
            print("linked in logo is available in header")
        else:
            print("Linked in logo is not available in header")
        elements = driver.find_elements(By.CSS_SELECTOR, ".fa-youtube-play")
        if len(elements) > 0:
            print("Youtube logo is available in header")
        else:
            print("Youtube logo is not available in header")


    except NoSuchElementException:
        print("Issue in Header social media logo visibility")

    # --------------------------------------------------------

    # footer social media
    # text_content = "https://www.linkedin.com/company/peozzle"

    try:

        elements = driver.find_elements(By.XPATH, "//span[contains(.,\'Connect with\')]")
        if len(elements) > 0:
            print("Connect with text found")
        else:
            print("Connect with text not found")

        elements = driver.find_elements(By.XPATH, "(//a[contains(@href, \'https://twitter.com/peozzle\')])[2]")
        if len(elements) > 0:
            print("Twitter footer logo found")
        else:
            print("Twitter footer logo not found")

        elements = driver.find_elements(By.XPATH,
                                        "(//a[contains(@href, \'https://www.linkedin.com/company/peozzle\')])[2]")
        if len(elements) > 0:
            print("Linked in footer logo found")
        else:
            print("Linked in footer logo not found")
        elements = driver.find_elements(By.XPATH, "//a[contains(@href, \'https://fb.me/Peozzle\')]")
        if len(elements) > 0:
            print("Facebook footer logo found")
        else:
            print("Facebook footer logo not found")
        elements = driver.find_elements(By.XPATH,
                                        "(//a[contains(@href, \'https://www.youtube.com/@PeozzleCorp\')])[2]")
        if len(elements) > 0:
            print("Youtube footer logo found")
        else:
            print("Youtube in footer logo not found")

    except NoSuchElementException:
        print("Issue in Header social media logo visibility")
    # -------------------------------------------------
    # Find all anchor elements
    try:
        anchor_elements = driver.find_elements(By.CSS_SELECTOR, ".seofy_module_text a")

        # Iterate over each anchor element and print its href attribute
        for anchor in anchor_elements:
            print(" Link:", anchor.get_attribute("href"))

        print("Tc8: All links are present on the page.")
        results["15. Ensure all the product links are available"] = "Passed"

    except NoSuchElementException:
        print("Tc8: Links not found on the page.")
        results["15. Ensure all the product links are available"] = "Failed"

    # -------------------------------------------------------
    paragraph_element = driver.find_element(By.CSS_SELECTOR, ".text_mobile p")

    try:
        # Check if the copyright text is present
        if "Copyright © 2024 Peozzle Corporation. Patented. All Rights Reserved." in paragraph_element.text:
            print("Tc7: Copyright text is present on the page.")
            results["14. Ensure Copyright text is available"] = "Passed"

        else:
            print("Tc7: Copyright text is not present on the page.")
            results["14. Ensure Copyright text is available"] = "Failed"

    except NoSuchElementException:
        print("Issues in copyright content")

    # ---------------------------------------------------------

    # Check if the image element is present
    try:
        image_element = driver.find_element(By.CSS_SELECTOR, "img.alignnone.size-medium.wp-image-4943")
        print("google play store Image found on the page.")
        results["36. Ensure google play store Image is available"] = "passed"

    except NoSuchElementException:
        print("google play store  Image not found on the page.")
        results["36. Ensure google play store Image is available"] = "Failed"

    # Check if the image element is present
    try:
        image_element = driver.find_element(By.CSS_SELECTOR, "img.alignnone.size-medium.wp-image-4942")
        print("APP store Image found on the page.")
        results["37. Ensure APP store Image is available"] = "passed"

    except NoSuchElementException:
        print("APP store Image not found on the page.")
        results["37. Ensure APP store Image is available"] = "Failed"

    driver.quit()
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------
    df = pd.DataFrame(results.items(), columns=["Testcase", "Test Status"])
    print("Original DataFrame :")
    # result = df.to_html(index=False)
    result = df.to_html(index=False)

    # print(result)
    # write html to file
    filename = "Peozzle_Solutions_ByRole_TestResult for "+rolename+".html"
    text_file = open(filename, "w")
    text_file.write(result)
    text_file.close()


    subject = "PeozzleSolutions_ByRole "+rolename +"Test report"
    body = "PeozzleSolutions_ByRole "+rolename+" Test report attached with this email"
    sender_email = "steve.lewin2011@gmail.com"
    receiver_email = "maria@peozzle.com"
    password = "hikr jbvn yjpz wjqn"

    # filename= "Peozzle_Solutions_ByRole_TestResult.html"

    email_report_selenium.email_report(subject, body, sender_email, receiver_email, password, filename)
