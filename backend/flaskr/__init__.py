import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
import datetime
import pytz
from models import setup_db, Question, Category, db
import time
import flask_mail
from flask_mail import Mail, Message
from sqlalchemy import func
import json
QUESTIONS_PER_PAGE = 10

# play for question by cat
unique_list = []

# for all questions
unique_list1 = []
os.environ['SECRET_KEY'] = 'my_secter!keyNoNE=True123'
app_secrect = os.getenv('SECRET_KEY')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)

    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = app_secrect
    '''
    @TODO: Set up CORS. Allow '*' for origins.
    Delete the sample route after completing the TODOs
    '''
    CORS(app)
    cors = CORS(app, resources={r"*/*": {"origins": "*"}})
    # CORS Headers
    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    '''
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    '''

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                    'code': 404,
                    'message': 'resource not found',
                    'success': False
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                    'code': 422,
                    'message': 'unprocessable',
                    'success': False
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
                    'code': 400,
                    'message': 'bad request',
                    'success': False
        }), 400

    @app.errorhandler(405)
    def wrong_method(error):
        return jsonify({
                    'code': 405,
                    'message': 'method not allowed',
                    'success': False
        }), 405

    @app.errorhandler(409)
    def conflict(error):
        return jsonify({
                    'code': 409,
                    'message': 'duplicated question',
                    'success': False
        }), 409

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
                    'code': 500,
                    'message': "Internal server error",
                    'success': False
        }), 500

    # function to return pagination list
    def pagination_helper(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        formated_questions = [question.format() for question in selection]
        pagie_list = formated_questions[start:end]
        return pagie_list

    # function to return custom pagination list for last page
    def custom_pagination_helper(request, selection, page):
        end = page * QUESTIONS_PER_PAGE
        start = end - QUESTIONS_PER_PAGE
        formated_questions = [question.format() for question in selection]
        pagie_list = formated_questions[start:end]
        return pagie_list

    def get_last_page():
        last_page = 1
        all_questions = Question.query.order_by('id').all()
        len_questions = len(all_questions)
        if len_questions == 0:
            last_page = 1
            return last_page

        pages_count_specified_int = int(len_questions)\
            / int(QUESTIONS_PER_PAGE)
        # check if it is integer if true return
        # it no need solution 20 = 2 pages
        check_int = isinstance(pages_count_specified_int, int)
        if check_int:
            last_page = int(pages_count_specified)
            return last_page
        else:
            # my solution the round problem if it 1.1 - 1.4 it will return 1
            pages_count_specified_string = str(pages_count_specified_int)
            after_dot = int(pages_count_specified_string.split('.')[1])
            if after_dot < 5:
                # example 1.4  (4 < 5) add 1 to the round (13/10) = 1.3
                last_page = round(pages_count_specified_int) + 1
                return last_page
            else:
                last_page = round(pages_count_specified_int)
                return last_page

    # this cus of rect we did not even read it
    def check_type_and_return_list(previous_question):
        prev_questions = []
        if isinstance(previous_question, str) and '[' in previous_question:

            # if rect send string like my curl
            filter_1 = previous_question.replace('[', '')
            filter_2 = filter_1.replace(']', '')
            filter_3 = filter_2.replace(' ', '')
            solve_if_string = filter_3.split(',')
            prev_questions = solve_if_string
            return prev_questions

        elif isinstance(previous_question, list):
            # if it work as must work and sent normal list
            prev_questions = previous_question
            return prev_questions

        elif isinstance(previous_question, tuple):
            # if it send tuple
            prev_questions = list(previous_question)
            return prev_questions

        elif isinstance(previous_question, str):
            # if it normal and cure string
            prev_questions.append(previous_question)
            return prev_questions

        else:
            return prev_questions

    '''
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    '''
    @app.route('/categories')
    def get_categories():
        I_dont_like_react = []
        all_categories = Category.query.order_by('id').all()
        formated_categories = [cat.format() for cat in all_categories]
        cats = [
                'science',
                'history',
                'art',
                'sport',
                'entertainment',
                'geography'
                ]
        for item in all_categories:
            I_dont_like_react.append(item.type)

        return jsonify({
            'categories': cats,
            'the_real_categories': formated_categories,
            'success': True
            })

    # normal function return all questions order_by category
    @app.route('/')
    @app.route('/questions')
    def home():

        categories = []
        all_questions = Question.query.order_by('category').all()
        all_categories = Category.query.order_by('id').all()
        for i in all_categories:
            if i.id > 3:
                categories.append(i.type)

        formated_categories = [cat.format() for cat in all_categories]
        paginated_questions = pagination_helper(request, all_questions)
        total_questions = len(all_questions)
        if all_questions:
            # logical if depnded current category and
            # assumed there are also 10 in each cat this what should be
            get_first_cat_h3ml_eh = all_questions[0].category
            return jsonify({
                'questions': paginated_questions,
                'total_questions': total_questions,
                'current_category': get_first_cat_h3ml_eh,
                'categories': categories,
                'the_real_categories': formated_categories,
                'success': True
                })
        else:
            return jsonify({
                'questions': paginated_questions,
                'total_questions': total_questions,
                'current_category': '',
                'categories': formated_categories,
                'success': True
                })

    '''
    @TODO:
    Create an endpoint to handle GET requests
    for questions for A given category,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at
    the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    '''

    '''
    @TODO:
    Create an endpoint to DELETE question using a question ID.
    TEST: When you click the trash icon next
    to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    '''

    # delete the question with error handling
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        error = False
        question_to_delete = Question.query.filter_by(
            id=question_id).one_or_none()
        if question_to_delete:
            try:
                question_to_delete.delete()
            except TypeError:
                print(sys.exc_info())
                db.session.rollback()
                error = True
            finally:
                db.session.close()

            if not error:
                # get the new questions
                all_questions = Question.query.order_by('category').all()
                questions_length = len(all_questions)
                paginated_questions = pagination_helper(request, all_questions)
                return jsonify({
                    'questions': paginated_questions,
                    'total_questions': questions_length,
                    'success': True,
                    'deleted': question_id
                    })
            else:
                abort(400)
        else:
            abort(404)

    '''
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will
    appear at the end of the last page
    of the questions list in the "List" tab.
    '''
    # post question or search one
    @app.route('/add', methods=['POST'])
    @app.route('/questions', methods=['POST'])
    def post_questions():
        error = False
        added = None
        sys_error = ''
        body = request.get_json()
        question = body.get('question', None)
        answer = body.get('answer', None)
        category = body.get('category', None)
        difficulty = body.get('difficulty', None)
        search = body.get('searchTerm', None)
        # TDD you have 1 of two options post question
        # or search question not both in same request
        if question and search:
            # the user send body used for 2 actions confilit
            # good but i need keep the first message
            abort(422)
        if answer and search:
            abort(422)
        if category and search:
            abort(422)
        if difficulty and search:
            abort(422)

        '''
        @TODO:
        Create a POST endpoint to get questions based on a search term.
        It should return any questions for whom the search term
        is a substring of the question.

        TEST: Search by any phrase. The questions list will update to include
        only question that include that string within their question.
        Try using the word "title" to start.
        '''
        if search:
            try:
                secure_search = '%s' % search
                # my first advanced query mix of two queries in stackoverflow
                search_question = Question.query.filter(func.lower(
                    Question.question).contains(
                        func.lower(secure_search))).all()
                total_found = len(search_question)
                formated_questions = [
                    question.format() for question in search_question
                    ]
                message = 'nothing found for %s' % search
                # important note [] == False
                if search_question:
                    return jsonify({
                        'questions': formated_questions,
                        'total': total_found
                        })
                else:
                    return jsonify({
                        'message': message,
                        'questions': formated_questions,
                        'total': total_found
                        })
            except TypeError:
                # example when error accured
                abort(400)

        if question and answer and category and difficulty and search is None:
            # check if duplicated question return conflict
            check_duplicated_question = Question.query.filter(
                Question.question.ilike('%{}%'.format(question))).one_or_none()
            if check_duplicated_question:
                abort(409)
            try:
                new_question = Question(
                    question=question,
                    answer=answer,
                    category=category,
                    difficulty=difficulty
                    )
                new_question.insert()
                added = new_question.id
            except TypeError:
                print(sys.exc_info())
                sys_error = str(sys.exc_info())
                db.session.rollback()
                error = True
            finally:
                db.session.close()

            if not error and added:
                '''
                get the new questions question will appear at the end of
                the last page of the questions list to check what happend
                you have to see get_last_page() and custom_pagination_helper
                '''
                try:
                    last_page = get_last_page()
                    query_example = Question.query.order_by(Question.id).all()
                    questions_length = len(query_example)
                    last_question_page = custom_pagination_helper(
                        request, query_example, last_page)
                    return jsonify({
                        'list': last_question_page,
                        'total_questions': questions_length,
                        'success': True,
                        'added': added
                        })
                except TypeError:
                    abort(400)
            else:
                # this happend if error accured while adding
                # in database better to return json error message
                abort(500)
        else:
            # if missing rquired paramters we understand
            # the request but we can not submit
            abort(422)

    '''
    @TODO:
    Create a GET endpoint to get questions based on category.
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be here where should i return current_category
    '''

    # what if the first category contains only 3
    # and second contains 3 which will be current category for first 10
    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category_id(category_id):
        # order_by category to return all categories one by one
        # check category first
        check_category = Category.query.filter_by(id=category_id).one_or_none()

        if check_category is None:
            abort(404)
        category_name = str(check_category.type)
        if check_category and category_name:
            all_questions = Question.query.filter_by(
                category=category_name).order_by('id').all()
            all_categories = Category.query.order_by('id').all()
            formated_categories = [cat.format() for cat in all_categories]
            total_questions = len(all_questions)
            total_categories = len(all_categories)
            paginated_questions = pagination_helper(request, all_questions)
            return jsonify({
                'questions': paginated_questions,
                'total_questions': total_questions,
                'current_category': category_name,
                'categories': formated_categories,
                'success': True
                })
        else:
            abort(404)

    # aditonal Function to GET questions by category name direct
    @app.route('/categories/<string:category>/questions')
    def get_questions(category):
        # order_by category to return all categories one by one
        # check category first
        check_category = Category.query.filter_by(type=category).one_or_none()

        if check_category:
            all_questions = Question.query.filter_by(
                category=category).order_by('id').all()
            all_categories = Category.query.order_by('id').all()
            formated_categories = [cat.format() for cat in all_categories]
            total_questions = len(all_questions)
            total_categories = len(all_categories)
            paginated_questions = pagination_helper(request, all_questions)
            return jsonify({
                'questions': paginated_questions,
                'total_questions': total_questions,
                'current_category': category,
                'categories': formated_categories,
                'success': True
                })
        else:
            abort(404)

    '''
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    '''

    # time to play with set
    @app.route('/quizzes', methods=['POST'])
    @app.route('/play', methods=['POST'])
    def play_with_questions():
        error = False
        sys_error = ''
        body = request.get_json()
        # category
        category = body.get('quiz_category', None)
        previous_question = body.get('previous_questions', None)
        # if it as it must be it should be string and
        # I will able to handle it even list and tuple
        prev_questions = check_type_and_return_list(previous_question)
        check_if_questions = Question.query.first()
        if check_if_questions is None:
            return jsonify({
                'previous_question': '',
                'current_question': '',
                'message': 'there are no questions'
                })

        if category and previous_question:
            all_questions_for_cat = Question.query.filter_by(
                category=category).all()
            questions_len = len(all_questions_for_cat)
            questions_list = [
                question.format() for question in all_questions_for_cat
                ]
            for_count = 0
            for question in questions_list:
                if questions_len == 0:
                    return jsonify({
                        'previous_question': '',
                        'current_question': '',
                        'forceEnd': True,
                        'message': 'no questions to play please add one'
                        })
                    break

                if questions_len != 0:
                    random_question = random.choice(all_questions_for_cat)

                if random_question.question not in unique_list and\
                    random_question.question not in prev_questions and\
                        questions_len != 0:
                    unique_list.append(random_question.question)
                    selected_random_question = random_question.question
                    selected_random_question_answer = random_question.answer
                    myl = len(previous_question)-1
                    return jsonify({
                        'previous_question': previous_question[myl],
                        'question': selected_random_question,
                        'answer': question['answer'],
                        'visibleAnswer': selected_random_question_answer
                        })
                    break
                if questions_len == for_count and for_count != 0:
                    return jsonify({
                        'previous_question': '',
                        'current_question': '',
                        'message': 'Congrats You solved all questions'
                        })
                    break
                for_count += 1

        if previous_question and category is None:
            all_questions = Question.query.all()
            all_questions_len = len(all_questions)
            all_questions_list = [
                question.format() for question in all_questions
                ]
            for_count1 = 0
            for one_question in all_questions_list:
                if all_questions_len == 0:
                    return jsonify({
                        'previous_question': '',
                        'question': '',
                        'answer': '',
                        'forceEnd': True,
                        'message': 'no questions to play please add one'
                        })
                    break
                if all_questions_len != 0:
                    random_question1 = random.choice(all_questions)

                if random_question1.question not in unique_list1 and\
                    random_question1.question not in prev_questions and\
                        all_questions_len != 0:

                    unique_list.append(random_question1.question)
                    the_random_question = random_question1.question
                    the_random_question_answer = random_question1.answer
                    return jsonify({
                        'previousQuestions': previous_question,
                        'question': the_random_question,
                        'answer': the_random_question_answer,
                        'visibleAnswer': the_random_question_answer
                        })
                    break
                if all_questions_len == for_count1 and for_count1 != 0:
                    return jsonify({
                        'previous_question': '',
                        'current_question': '',
                        'answer': '',
                        'forceEnd': True,
                        'message': 'Congrats You solved all questions'
                        })
                    break
                for_count1 += 1
        else:
            abort(422)

    return app
