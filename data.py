import requests


class Question_bank:
    def __init__(self, number_of_questions):
        self.number_of_questions = number_of_questions
        self.question_data = self.request_question_bank()

    def request_session_token(self):
        while True:
            t = requests.get(
                "https://opentdb.com/api_token.php?command=request").json()
            if t['response_code'] == 0:
                session_token = t['token']
                break
        return session_token

    def request_question_bank(self):
        token = self.request_session_token()
        payload = {'amount': self.number_of_questions,
                   'type': 'boolean', 'token': token}
        while True:
            response = requests.get(
                "https://opentdb.com/api.php", params=payload).json()
            if response['response_code'] != 0:
                token = self.request_session_token()
            else:
                return response['results']
