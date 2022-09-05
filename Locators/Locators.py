class Locators:
    # HOMEPAGE OBJECTS

    # Проверка кликабельности кнопки "Лабиринт" в "шапке" сайта.
    header_button_logo_lab = 'b-header-b-logo-wrapper'

    # Проверка кликабельности списка кнопки "Книги" в "шапке" сайта.
    header_button_books = '//a[@href="/books/"]'
    header_button_best = "//*[@id='header-genres']/div[1]/ul[1]/li[2]/a[1]"
    header_button_all_books = '//*[@id="header-genres"]/div[1]/ul[1]/li[3]/a[1]'
    button_books_bilinguals = "//span[contains(text(), 'Билингвы и книги на иностранных языках')]"
    only_bilinguals = "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[4]/a[1]"
    child_books = "//span[contains(text(), 'Книги для детей')]"
    children_all_books = "//*[@id='header-genres']/div[1]/ul[1]/li[5]/ul[1]/li[3]/a[1]"
    children_leisure = '//*[@id="header-genres"]/div[1]/ul[1]/li[5]/ul[1]/li[5]/a[1]'
    manga_comics_art = "//span[contains(text(), 'Комиксы, Манга, Артбуки')]"
    all_manga_comics_art = '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[3]/a[1]'
    only_manga_button = '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[7]/a[1]'
    youth_literature = "//*[@id='header-genres']/div[1]/ul[1]/li[7]/a[1]"
    non_fiction_literature = "//span[contains(text(), 'Нехудожественная литература')]"
    non_fiction_literature_all = '//*[@id="header-genres"]/div[1]/ul[1]/li[8]/ul[1]/li[3]/a[1]'
    non_fiction_natural_sciences = '//*[@id="header-genres"]/div[1]/ul[1]/li[8]/ul[1]/li[8]/a[1]'
    periodicals = '//*[@id="header-genres"]/div[1]/ul[1]/li[9]/a[1]'
    religion = "//span[contains(text(), 'Религия')]"
    all_religion = '//*[@id="header-genres"]/div[1]/ul[1]/li[10]/ul[1]/li[3]/a[1]'
    religious_studies = '//*[@id="header-genres"]/div[1]/ul[1]/li[10]/ul[1]/li[6]/a[1]'
    educational_methodical_literature = "//*[@id='header-genres']/div[1]/ul[1]/li[11]/span[1]"
    all_educational_methodical_literature = '//*[@id="header-genres"]/div[1]/ul[1]/li[11]/ul[1]/li[3]/a[1]'
    fiction_literature = "//span[contains(text(), 'Художественная')]"
    all_fiction_literature = '//*[@id="header-genres"]/div[1]/ul[1]/li[12]/ul[1]/li[3]/a[1]'
    small_book_reviews = '//*[@id="header-genres"]/div[1]/ul[1]/li[13]/span[1]/a[2]'
    authors_books = '//*[@id="header-genres"]/div[1]/ul[1]/li[13]/span[1]/a[7]'

    # Проверка кликабельности списка кнопки "Школа" в "шапке" сайта.
    header_button_school = '//a[@href="/school/"]'
    russian_languages_button = '//*[@id="header-school"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]'
    six_class = '//*[@id="header-school"]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]/a[1]'
    unified_state_exam = '//*[@id="header-school"]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[2]/a[1]'

    # Проверка кликабельности списка кнопки "Игрушки" в "шапке" сайта.
    games_button = '//a[@href="/games/"]'
    all_games = '//*[@id="header-toys"]/div[1]/ul[1]/li[2]/a[1]'
    games_and_toys = "//span[contains(text(), 'Игры и Игрушки')]"
    all_games_and_toys = '//*[@id="header-toys"]/div[1]/ul[1]/li[4]/ul[1]/li[3]/a[1]'
    small_toy_manufacturers = '//*[@id="header-toys"]/div[1]/ul[1]/li[5]/span[1]/a[5]'
    office_tools = '//a[@href="/office/"]'
    book_accessories = "//span[contains(text(), 'Аксессуары для книг')]"
    bookmarks = '//*[@id="header-office"]/div[1]/ul[1]/li[3]/ul[1]/li[4]/a[1]'

    # Проверка кликабельности ссылок в "теле" сайта.
    html = 'html'
    body_readers_choose = 'block-link-title'
    body_readers_choose_today = '//*[@id="bottom"]/div[4]/div[1]/a[1]'
    body_you_recently_watched = '//a[@href="/cabinet/?vybor=visited"]'

    # Проверка кликабельности ссылок в "подвале" сайта.
    footer_zen_yandex = '//a[@href="https://zen.yandex.ru/labirintru"]'
    footer_souvenir = '//a[@data-event-content="Сувениры"]'
    footer_children_navigator = '//a[@data-event-content="Детский навигатор"]'

    # AUTHORIZATION OBJECTS
    # Проверка выпадающих сообщений блока неавторизованного пользователя.
    unauthorized_messages = "//span[contains(text(), 'Сообщения')]"
    no_unauthorized_messages = '//*[@id="minwidth"]/div[4]/div/div[1]/div[2]/div/ul/li[3]/div/div/div/div'
    my_lab = "//span[contains(text(), 'Mой Лаб​иринт')]"
    go_to_authorize = '//a[@data-sendto-params="auth-registration"]'
    authorize_form = "//span[contains(text(), 'Введите свой код скидки, телефон или эл.почту')]"
    hold_over_stash = '//a[@href="/cabinet/putorder/"]'
    cart = "//span[contains(text(), 'Корзина')]"