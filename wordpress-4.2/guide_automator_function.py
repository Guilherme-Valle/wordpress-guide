from guide_automator_constants import popperCss
from selenium import webdriver
from IPython.display import display
from selenium.webdriver.support.wait import WebDriverWait
import requests
import time
import io
from PIL import Image

wd = webdriver.Chrome()
wd.maximize_window()
listOfSelectors = []


# Get method. Access websites using the url by parameter
def get(url):
    wd.get(url);

# Fill in method. Insert text inside elements, using the element CSS selector
def fillIn(selector, text):
    elem = wd.find_element_by_css_selector(selector)
    elem.send_keys(text)

## Click on element of screen, using the element CSS selector
def click(selector):
    elem = wd.find_element_by_css_selector(selector)
    elem.click()

## Submit a element, using the element CSS selector
def submit(selector):
    elem = wd.find_element_by_css_selector(selector)
    elem.submit()

## Take screenshot of entire screen and display it
def takeScreenshot():
    sleep(3)
    display(Image.open(io.BytesIO(wd.get_screenshot_as_png())))
    removeAllHighlights()

## Take Screenshot of a specified element of the page and display it
def takeScreenshotOf(selector):

    element = wd.find_element_by_css_selector(selector)
    wd.execute_script('arguments[0].scrollIntoView()', element)
    ratio = wd.execute_script("return window.devicePixelRatio;")
    bounds = wd.execute_script("return arguments[0].getBoundingClientRect();", element)
    img = wd.get_screenshot_as_png()
    pilimg = Image.open(io.BytesIO(img))
    region = pilimg.crop((bounds['left'] * ratio, bounds['top'] * ratio, bounds['right'] * ratio, bounds['bottom'] * ratio,))
    display(region)
    removeAllHighlights()


# Highlight a element with a red border, using the element CSS selector
def highlight(selector):
    element = wd.find_element_by_css_selector(selector)
    wd.execute_script('arguments[0].setAttribute("style", "outline: 3px solid red")', element)
    listOfSelectors.append(selector)

# Remove the highlight of a element, using the element CSS selector
def removeHighlight(selector):
    element = wd.find_element_by_css_selector(selector)
    wd.execute_script('arguments[0].setAttribute("style", "outline: 0px solid red")', element)

# Remove all the highlights
def removeAllHighlights():
    global listOfSelectors
    for selector in listOfSelectors:
        removeHighlight(selector)
    listOfSelectors = []

## Make the program wait the time defined by parameter, on seconds
def sleep(sleepTime):
    time.sleep(sleepTime);

## Close the browser window
def close():
    wd.quit()

## Create a popper on the screen, next to an element, with text and direction based on the parameter
def pop(selector, text, direction):
    wd.set_script_timeout(2000);

    myString = """
    var s=window.document.createElement('style');
    s.type = 'text/css';
    s.innerHTML = `{0}`;
    window.document.head.appendChild(s);
    s.onload = arguments[0];
    """
    myString = myString.format(popperCss)
    wd.execute_async_script(myString)

    myString = """
    var mypopper = window.document.createElement('div');
    mypopper.id='popper';
    mypopper.setAttribute("class","popper");
    mypopper.innerHTML = "{0}";
    
    var mypopperArrow = window.document.createElement('div');
    mypopperArrow.setAttribute("class", "popper__arrow");
    mypopperArrow.setAttribute("x-arrow", "");
    mypopper.appendChild(mypopperArrow);
    window.document.body.appendChild(mypopper);
    """;

    myString = myString.format(text);
    wd.execute_script(myString);

    wd.execute_async_script("""
    var s=window.document.createElement('script');
    s.src='https://unpkg.com/popper.js/dist/umd/popper.min.js';
    window.document.head.appendChild(s);
    s.onload = arguments[0];
    """);

    myString = """
    var popper = new Popper(document.querySelector('{0}'),
    document.getElementById('popper'),
    {{ placement: '{1}' }});
    """;
    myString = myString.format(selector, direction);

    wd.execute_script(myString);


