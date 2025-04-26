from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application
from support.logger import logger

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/search_results.feature
# To generate report, run:
# allure serve test_results/

def browser_init(context):
    # :param context: Behave context

    ### Chrome ###
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### Chrome HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')    #if headless fails try this instead: options.add_argument("--window-size=1920,1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### Firefox ###
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user ='jackiemettler_CJGfVT'
    # bs_key = 'REsqorKvRVziSNgxALhs'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'edge',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    logger.info(f'Started step {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
