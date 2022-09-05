from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.authpage import AuthorizationPage
from Pages.homepage import HomePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from usefull_methods import check_exists_by_xpath


class TestAuthorizationPage:
    def test_visible_unauthorized_messages(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.visible_unauthorized_messages()

    def test_visible_my_lab_go_to_authorize(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.visible_my_lab_go_to_authorize()
        assert driver.find_element(
            By.XPATH, "//span[contains(text(), 'Введите свой код скидки, телефон или эл.почту')]").is_displayed()

    def test_click_hold_over(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.click_hold_over()
        assert driver.current_url == 'https://www.labirint.ru/cabinet/putorder/'

    def test_unauthorized_cart(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.click_unauthorized_cart()
        assert driver.current_url == 'https://www.labirint.ru/cart/'

class TestHomePage:

    def test_welcome_homepage(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_logo()
        assert driver.current_url == 'https://www.labirint.ru/'

    def test_books_best(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_best()
        assert driver.current_url == 'https://www.labirint.ru/best/'

    def test_books_all(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_all_books()
        assert driver.current_url == 'https://www.labirint.ru/books/'

    def test_books_bilinguals(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_bilinguals()
        assert driver.current_url == 'https://www.labirint.ru/genres/2827/'

    def test_children_all_book(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_all_books()
        assert driver.current_url == 'https://www.labirint.ru/genres/1850/'

    def test_children_leisure(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_leisure()
        assert driver.current_url == 'https://www.labirint.ru/genres/2048/'

    def test_all_manga_comics_art(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_all_manga_comics_art()
        assert driver.current_url == 'https://www.labirint.ru/genres/2993/'

    def test_only_manga_button(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_only_manga_button()
        assert driver.current_url == 'https://www.labirint.ru/genres/2684/'

    def test_youth_literature(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_youth_literature()
        assert driver.current_url == 'https://www.labirint.ru/genres/3066/'

    def test_non_fiction_all(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_non_fiction_literature_all()
        assert driver.current_url == 'https://www.labirint.ru/genres/3000/'

    def test_non_fiction_natural_sciences(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_non_fiction_natural_sciences()
        assert driver.current_url == 'https://www.labirint.ru/genres/1854/'

    def test_periodicals(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_periodicals()
        assert driver.current_url == 'https://www.labirint.ru/genres/2137/'

    def test_all_religion(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_religion()
        assert driver.current_url == 'https://www.labirint.ru/genres/2386/'

    def test_religious_studies(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_religious_studies_()
        assert driver.current_url == 'https://www.labirint.ru/genres/2395/'

    def test_all_educational_methodical_literature(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_educational_methodical_literature()
        assert driver.current_url == 'https://www.labirint.ru/genres/11/'

    def test_all_fiction_literature(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_fiction_literature()
        assert driver.current_url == 'https://www.labirint.ru/genres/1852/'

    def test_small_book_reviews(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_small_book_reviews()
        assert driver.current_url == 'https://www.labirint.ru/news/books/'

    def test_author_books(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_author_books()
        assert driver.current_url == 'https://www.labirint.ru/authors/books/'

    def test_school_russian(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_school_russian()
        assert driver.find_element(
            By.XPATH, '//*[@id="right-inner"]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/h3[1]').is_displayed()

    def test_school_six_class(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_school_six_class()
        assert driver.find_element(
            By.XPATH, '//*[@id="right-inner"]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/h3[1]').is_displayed()

    def test_school_unified_state_exam(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_school_unified_state_exam()
        assert driver.current_url == 'https://www.labirint.ru/school/?examtype[]=1#right'

    def test_all_games(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_games()
        assert driver.current_url == 'https://www.labirint.ru/games/'

    def test_all_games_and_toys(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_games_and_toys()
        assert driver.current_url == 'https://www.labirint.ru/genres/1643/'

    def test_small_toy_manufacturers(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_small_toy_manufacturers()
        assert driver.current_url == 'https://www.labirint.ru/pubhouse/games/'

    def test_all_book_accessories(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_book_accessories()
        assert driver.current_url == 'https://www.labirint.ru/genres/2302/'

    def test_body_readers_choose_today(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_body_readers_choose_today()
        assert driver.current_url == 'https://www.labirint.ru/best/'

    def test_body_you_recently_watched(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_body_you_recently_watched()
        assert driver.current_url == 'https://www.labirint.ru/cabinet/?vybor=visited'

    def test_footer_zen_yandex(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_footer_zen_yandex()
        assert driver.current_url == 'https://zen.yandex.ru/labirintru'

    def test_footer_souvenir(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_footer_souvenir()
        assert driver.current_url == 'https://www.labirint.ru/souvenir/'

    def test_footer_children_navigator(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\PyTest\\tests\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_footer_children_navigator()
        assert driver.current_url == 'https://www.labirint.ru/child-now/'