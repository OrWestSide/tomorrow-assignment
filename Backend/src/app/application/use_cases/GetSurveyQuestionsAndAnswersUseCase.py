from app.application.interfaces import IAnswersRepository
from app.application.interfaces.ISurveysRepository import ISurveysRepository
from app.application.use_cases.IUseCase import IUseCase
from app.domain.operations.queries.GetSurveyQuestionsAndAnswersOperation \
    import GetSurveyQuestionsAndAnswersOperation


class GetSurveyQuestionsAndAnswersUseCase(IUseCase):
    def __init__(self,
                 survey_repo: ISurveysRepository,
                 answer_repo: IAnswersRepository
                 ):
        self.survey_repo = survey_repo
        self.answer_repo = answer_repo

    def _parse_questions(self, survey_questions):
        _questions = []
        _q = {}
        for i in survey_questions:
            answers = self.answer_repo.get_by_question_id(
                i[0].dict()['question_id']
            )

            _q = {
                'question_id': i[1].dict()['id'],
                'question_type': i[1].dict()['question_type'],
                'question_text': i[1].dict()['question_text'],
                'answers': [answer.dict()['answer_text'] for answer in answers]
            }

            _questions.append(_q)

        return _questions

    def handle(self, operation: GetSurveyQuestionsAndAnswersOperation):
        sq = self.survey_repo.get_survey_questions(operation.survey_id)
        return self._parse_questions(sq)
