from pywatson.answer.answer import Answer
from pywatson.question.question import Question
import requests


class Watson(object):
    """The Watson API adapter class"""

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def ask_question(self, question_text, question=None):
        """Ask Watson a question via the Question and Answer API

        :param question_text: question to ask Watson
        :type question_text: str
        :param question: if question_text is not provided, a Question object
                         representing the question to ask Watson
        :type question: Question
        :return: Answer
        """
        if question is not None:
            q = question.__dict__
        else:
            q = Question(question_text).__dict__
        r = requests.post(self.url + '/question', json=q)
        return Answer(r.json())
