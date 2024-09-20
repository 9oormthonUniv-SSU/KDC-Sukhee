from django.test import TestCase
from .models import GuessNumbers

class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)

        # default로 6개 숫자 x 5set = 30개의 숫자가 생성됨을 확인
        self.assertTrue(len(g.lottos) > 20)
