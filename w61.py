from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

# from secrets import username, password


class TinderBot():

    _COORD_LIST = ('518|368', '517|367', '517|369', '515|369', '514|368', '514|367', '512|367', '511|369', '518|375',
                   '517|375', '507|365', '505|377', '508|377', '507|374', '512|368', '513|367', '512|366', '514|366', '514|386',
                   '507|397', '507|399', '511|402', '504|393', '504|386', '503|378', '500|378', '495|378', '497|381',
                   '498|380', '497|368', '499|372', '495|374', '496|363', '495|366', '493|358', '497|359', '498|358', '498|357',
                   '501|359', '502|360', '503|359', '504|361', '509|358', '508|359', '507|358', '507|363', '504|370', '531|393'

                   )

    _COORD_LIST_2 = (
        '501|366', '500|367', '495|364', '491|366', '490|366', '491|373', '488|373', '485|372', '487|375', '488|376',
        '488|377', '485|377', '488|379', '483|369', '483|370', '485|362', '486|361', '486|369', '488|369', '487|367'
    )
    _COORD_LIST_3 = ('522|359', '523|360', '522|360', '522|363', '521|364', '521|365', '520|365', '523|365', '524|363', '525|363',
                     '526|362', '524|366', '522|367', '520|367', '526|368', '522|369', '522|370', '523|371', '521|371', '523|373',
                     '520|374', '526|369', '527|369', '527|370', '526|371', '527|371', '525|377', '521|381', '522|382', '525|377',
                     '527|377', '528|377', '529|375', '523|384', '529|383', '528|388', '523|387', '524|389', '523|390', '528|391',
                     '521|388', '529|390', '521|384', '532|363', '535|363', '535|364', '536|367', '537|365', '537|363', '534|369',
                     '534|370', '535|371', '536|371', '536|374', '537|374', '534|381', '536|381', '530|393', '529|391', '526|392',  # , '537|375'
                     '527|393'
                     )
    TOWNS = (
        'https://es61.guerrastribales.es/game.php?village=17666&screen=place'  # Agualongo
        'https://es61.guerrastribales.es/game.php?village=18270&screen=place',  # tupak amaru
        'https://es61.guerrastribales.es/game.php?village=19182&screen=place',  # tzilacatzin
        'https://es61.guerrastribales.es/game.php?village=11492&screen=place',  # mapuches
        'https://es61.guerrastribales.es/game.php?village=17996&screen=place',   # Athahualpa
        'https://es61.guerrastribales.es/game.php?village=18631&screen=place',  # galvarino
        'https://es61.guerrastribales.es/game.php?village=18773&screen=place',  # guerrero jaguar
        'https://es61.guerrastribales.es/game.php?village=17292&screen=place',  # Quillasingas
    )

    INDEX = 0

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

        in_user.send_keys('metano21')
        in_pasword.send_keys('Cris1234')
        button_login.click()

        sleep(3)

        entry_words = self.driver.find_elements_by_class_name(
            'world_button_active')
        print(len(entry_words))
        print(entry_words[0])
        word = entry_words[0]
        word.click()
        sleep(3)
        self.driver.get(
            self.TOWNS[self.INDEX]  # Quillasingas
        )
        sleep(3)

        coord_join = self._COORD_LIST + self. _COORD_LIST_2 + self._COORD_LIST_3
        print('Number of tows', len(coord_join))
        for coord in coord_join:
            sleep(2)
            self.attack(coord)

    def attack(self, coord):

        input_coord = self.driver.find_element_by_class_name(
            'target-input-autocomplete')
        atack_button = self.driver.find_element_by_id('target_attack')
        in_units = self.driver.find_element_by_id('unit_input_light')

        sleep(4)
        input_coord.send_keys("")
        sleep(1)
        input_coord.send_keys(Keys.RETURN)
        sleep(1)
        input_coord.send_keys(coord)
        print('before enter')
        sleep(2)
        input_coord.send_keys(Keys.ENTER)
        print('after enter')
        sleep(3)

        label_units = self.driver.find_element_by_id('units_entry_all_light')
        element_text_village = {}
        error = False
        try:
            element_text_village = self.driver.find_element_by_class_name(
                'village-info')
        except:
            print('************')
            element_text_village = 'SAS: AS: 501'
            error = True
        number_units = self.transformText(label_units)
        points_village = self.valitate_points(element_text_village, error)

        units_atack = self.relation_point(points_village)

        # validate units and point in towns

        if number_units < units_atack:
            units_atack = number_units
            self.INDEX = self.INDEX + 1
            self.driver.get(
                self.TOWNS[self.INDEX]  # Quillasingas
            )
            sleep(3)

     #   Repit code start

            input_coord = self.driver.find_element_by_class_name(
                'target-input-autocomplete')
            atack_button = self.driver.find_element_by_id('target_attack')
            in_units = self.driver.find_element_by_id('unit_input_light')

            sleep(4)
            input_coord.send_keys("")
            sleep(1)
            input_coord.send_keys(Keys.RETURN)
            sleep(1)
            input_coord.send_keys(coord)
            print('before enter')
            sleep(2)
            input_coord.send_keys(Keys.ENTER)
            print('after enter')
            sleep(3)

            label_units = self.driver.find_element_by_id(
                'units_entry_all_light')
            element_text_village = {}
            error = False
            try:
                element_text_village = self.driver.find_element_by_class_name(
                    'village-info')
            except:
                print('************')
                element_text_village = 'SAS: AS: 501'
                error = True
            number_units = self.transformText(label_units)
            points_village = self.valitate_points(element_text_village, error)

            units_atack = self.relation_point(points_village)


#   Repit code end

        in_units.send_keys(units_atack)

        sleep(4)
        atack_button.click()

        sleep(4)
        confim_atack = self.driver.find_element_by_id('troop_confirm_go')
        confim_atack.click()
        sleep(3)

    def transformText(self, element):
        text = element.text
        text = text.replace("(", "")
        text = text.replace(")", "")
        return int(text)

    def valitate_points(self, element, error):
        text = ''
        print(error)
        if error:
            text = element
        else:
            text = element.text
        print(text)
        text = text.split(":")[2]
        text = text.replace(".", "")
        text = text.strip()
        return int(text)

    def relation_point(self, point):
        if point < 300:
            return 15
        if point < 400:
            return 20
        if point < 500:
            return 25
        if point < 600:
            return 35
        if point < 700:
            return 40
        else:
            return 35


bot = TinderBot()
bot.login()
