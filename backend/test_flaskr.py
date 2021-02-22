import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'noob', '123', 'localhost:5432', self.database_name
            )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO (each true test add . to result)
    Write at least one test for each test
    for successful operation and for expected errors.
    """

    # test categories success
    def test_success_categories(self):
        # use this once take care when add add
        # new cate one_or_none do not accept 2 categories
        # new_cat = Category(type='yor_category_here3')
        # new_cat.insert()
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # In Python, empty lists evaluate
        # to False and non-empty lists evaluate to True
        self.assertTrue(data['categories'])

    # test questions  success without query parameters
    def test_get_all_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])

    # test categories success without query parameters
    def test_success_questions_with_parameter(self):

        res = self.client().get('/categories/html/questions?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])
        self.assertEqual(data['current_category'], 'html')

    # Test delete missing question
    def test_missing_question(self):

        res = self.client().delete('/questions/10000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Test delete missing question
    def test_success_delete(self):
        # dynamic delete
        question_to_delete = Question(
            question='How we add Line break in HTML?',
            answer='<br />', category='html', difficulty=5
            )
        question_to_delete.insert()
        q_id = question_to_delete.id
        res = self.client().delete('/questions/{id}'.format(id=q_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], q_id)

    # ------------- POST TEST ---------
    """
    Before use this test Notes
    Make sure to use the same question
    in test_success and test_unsuccess
    functions just add 1 to the html
    """
    def test_success_post_question(self):

        success_and_unsucess_post_question = 'is there HTML57 version?'
        res = self.client().post('/questions', json={
            'question': success_and_unsucess_post_question,
            'answer': 'False',
            'category': 'html',
            'difficulty': 1
            })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test Repeated Question To Do that You need
    # to use success_and_unsucess_post_question var as your question
    # this used to check if the repeated question can be submited
    def test_unsuccess_post_question(self):

        success_and_unsucess_post_question = 'is there HTML57 version?'
        res = self.client().post('/questions', json={
            'question': success_and_unsucess_post_question,
            'answer': 'False',
            'category': 'html',
            'difficulty': 1
            })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 409)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'duplicated question')
    """
    the previous 2 functions are premade used togther
    """

    # test bad post request question can not asked
    def test_unprocessable_post_request(self):

        res = self.client().post('/questions', json={
                'question': 'IS Flask Bad?',
                'answer': False,
                'category': 'python',
                'difficulty': 1
                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # ########## Search Tests ###############

    # test search conflict with adding new question
    # 1 action can happend per request
    def test_conflict_post_request(self):

        res = self.client().post('/questions', json={
            'question': 'Can we Search and add new question in same request?',
            'answer': 'False',
            'category': 'python',
            'difficulty': 1,
            'searchTerm': 'Make confilit in Search'
            })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # test success earch
    def test_success_search(self):
        res = self.client().post('/questions', json={
            'searchTerm': 'html'
            })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        # empty lists return false by default
        self.assertTrue(data['questions'])

    # test unsuccess earch
    def test_unsuccess_search(self):
        res = self.client().post('/questions', json={
            'searchTerm': 'rnsnufh1rkhytuwh'
            })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['message'])
        # empty lists return false by default
        self.assertEqual(data['questions'], [])

    #  ########## last tests #########################

    # test success category by id
    def test_success_categories_by_id(self):
        # do not add duplicated category
        new_cat = Category(type='test_cat5')
        new_cat.insert()
        cat_id = new_cat.id
        cat_type = 'test_cat5'
        print(cat_id)
        question_to_delete = Question(
            # do not add duplicated question
            question='How we add Line break in HTML8?',
            answer='<br />',
            category='test_cat5',
            difficulty=5
            )
        question_to_delete.insert()
        res = self.client().get(
            '/categories/{cat_paramter}/questions'.format(cat_paramter=cat_id)
            )
        # get_that_cat = Category.query.filter_by(id=1).one_or_none()
        # if get_that_cat:
        #    get_that_cat = get_that_cat.type
        # else:
        #    get_that_cat = None
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertEqual(data['current_category'], cat_type)

    # test success quizzes without category
    def test_quiz_success_without_category(self):

        res = self.client().post('/quizzes', json={
            "previous_questions": "['what is larget HTML heading']"
            })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question'])
        self.assertTrue(data['visibleAnswer'])
        self.assertTrue(data['answer'])

    # test success quizzes without category
    def test_quiz_success_with_category(self):

        res = self.client().post('/quizzes', json={
                "previous_questions": "['what is larget HTML heading']",
                "quiz_category": "html"
                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question'])
        self.assertTrue(data['visibleAnswer'])
        self.assertTrue(data['answer'])

    # test questions success with string query paramters
    def test_success_questions(self):

        res = self.client().get('/categories/html/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])
        self.assertEqual(data['current_category'], 'html')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
