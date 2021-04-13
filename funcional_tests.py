from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith ouviu falar de uma nova aplicação online interessante para
        #lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        #Ela percebe que o titulo da página e o cabeçalho mencioname listas de 
        #tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_name('h1').text
        self.assertIn('To-Do', header_text)
        

        #Ela é convidada a inserir um item de tarefa imediatamente
        inpuxbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa
        #de texto (o hobby de edith é fazer iscas para pesca com fly)
        inputbox.send_keys('Buy peacock feathers')

        #Quando ela tecla enter, a pagina é atualizada, e agora a página lista 
        #"1: Buy peacock feathers" como um item em uma lista de tarefas
        input.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        #Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        #item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavão
        #para fazer um fly - Edith é bem metódica)

        self.fail('Finish the test!')
        #A pagina é atualizada novamente e agora mostra dois itens em sua lista

        #Edith se pergunta se o site lembrará da sua lista. Então ela nota
        #que o site gerou um URL único para ela -- há um pequeno
        #texto explicativo para isso

        #Ela acessa esse URL - sua lista de tarefas continua lá.

        #Satisfeita, ela volta a dormir

        # browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')