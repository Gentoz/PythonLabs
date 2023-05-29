import unittest
from main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Анкета'.encode('utf-8'), response.data)

    def test_submit(self):
        data = {
            'Как вас зовут?': 'Иван',
            'Сколько вам лет?': '25',
            'Какой у вас любимый цвет?': 'синий'
        }
        response = self.app.post('/submit', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Результаты'.encode('utf-8'), response.data)
        with open('answers.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.assertIn(','.join(data.values()) + 'n', lines)


if __name__ == '__main__':
    unittest.main()
