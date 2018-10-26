from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

"""
测试代码出错，算了，以后再学，人工排查也好提升我对代码理解  2018/10/25
"""
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
                    只要时间是未来的问卷，返回False
                """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # 将时间增加一个月，传进Question类
        self.assertIs(future_question.was_published_recently(), False)
        # 调用assertIs方法，返回值不是设定值False则报错

    def test_was_published_recently_with_old_question(self):
        """
            只要是超过1天的问卷，返回False
        """
        time = timezone.now() - datetime.timedelta(days=1,  minutes=1) #一天时除天数外还需要加时间可选参数，否则报错，为什么
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
                一天以内的问卷，返回True
                """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text,pub_date = time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are availbale.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_past_question(self):
        create_question(question_text="Past question.", days = -30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_questions(self):
        create_question(question_text="Future question.", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are availbale.")

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_future_question_and_past_question(self):
        create_question(question_text = "Past question.",days=-30)
        create_question(question_text="Future question.",days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_question(self):
        create_question(question_text = "Past question 1.",days=-30)
        create_question(question_text="Past question 2.",days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
