from selenium import webdriver
from time import sleep

# from secrets import username, password


class TinderBot():

    _COORD_LIST = ('444|552', '446|552', '446|551', '445|553', '447|546', '447|548', '447|549', '442|551', '441|551', '445|547',
                   '443|552', '442|552', '442|553', '443|553', '441|552', '442|550', '442|549', '441|548', '445|548', '446|547',
                   '441|544', '442|544', '443|545', '444|544', '447|553', '447|543', '447|542', '446|540', '439|552')

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://guerrastribales.es')

        sleep(2)

        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        # fb_btn.click()
        in_user = self.driver.find_element_by_xpath('//*[@id="user"]')
        in_pasword = self.driver.find_element_by_xpath('//*[@id="password"]')
        button_login = self.driver.find_element_by_class_name('btn-login')

        in_user.send_keys()
        in_pasword.send_keys()
        button_login.click()

        sleep(3)

        entry_words = self.driver.find_elements_by_class_name(
            'world_button_active')
        print(len(entry_words))
        print(entry_words[3])
        word = entry_words[3]
        word.click()
        sleep(3)
        self.driver.get(
            'https://esc1.guerrastribales.es/game.php?village=4673&screen=place')
        sleep(3)

        for coord in reversed(self._COORD_LIST):
            sleep(2)
            self.attack(coord)

    def attack(self, coord):

        input_coord = self.driver.find_element_by_class_name(
            'target-input-autocomplete')
        atack_button = self.driver.find_element_by_id('target_attack')
        in_units = self.driver.find_element_by_id('unit_input_light')
        sleep(4)
        input_coord.send_keys(coord)
        # sleep(3)
        # input_coord.send_keys(Keys.ENTER)

        sleep(4)
        in_units.send_keys(10)
        sleep(4)
        atack_button.click()
        sleep(4)
        confim_atack = self.driver.find_element_by_id('troop_confirm_go')
        confim_atack.click()
        sleep(3)

        # map = self.driver.find_elements_by_class_name('map2')
        # entry_words[2].click()

        # switch to login popup
    #     base_window = self.driver.window_handles[0]
    #     self.driver.switch_to_window(self.driver.window_handles[1])

    #     email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
    #     email_in.send_keys('username')

    #     pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
    #     pw_in.send_keys('password')

    #     login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
    #     login_btn.click()

    #     self.driver.switch_to_window(base_window)

    #     popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    #     popup_1.click()

    #     popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    #     popup_2.click()

    # def like(self):
    #     like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
    #     like_btn.click()

    # def dislike(self):
    #     dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
    #     dislike_btn.click()

    # def auto_swipe(self):
    #     while True:
    #         sleep(0.5)
    #         try:
    #             self.like()
    #         except Exception:
    #             try:
    #                 self.close_popup()
    #             except Exception:
    #                 self.close_match()

    # def close_popup(self):
    #     popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
    #     popup_3.click()
    # def close_match(self):
    #     match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    #     match_popup.click()
bot = TinderBot()
bot.login()
