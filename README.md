# Full Stack API Final Project

# Trivia-API  (Python API)

### Udacity Project (Advanced Track)
!['udacity logo'](https://github.com/MahmoudHegazi/your_library_api/blob/main/download.png?raw=true)


# Introduction:

* The Triva is Python API Not Rect app organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes.
* you can use this API TO create, read , questions there are 6 cateogries and you can play question game and searck for a question this is A python API not any other thing Like this Lesson Name API, The code adheres to the PEP 8 style guide
* get full pagination list of the questions 


## how to set up the local development for FLASK API

* I have removed the modules to setup it npm install then npm start the frontend react app working on localhost:3000/ if u react developer use it
* npm install only once to install dependency 
* npm start
* on Windows: Download GitBash, open it, ```cd [project_folder]``` run these 3 commands 
* ``` export FLASK_APP=flaskr ```
* ``` export FLASK_ENV=development ```
* ``` flask run ```
* For Linux users, you can use the same three commands to start the API

# Errors:
* Your Library API May return 4 types of errors [404, 422, 400, 405, 409]

### 404 Resource Not Found:

* example of the response : 
    ```json
       {
        'code':404,
        'message':'resource not found',
        'success':False
        }
    ```
    
### 422 Unprocessable:

* JSON response will return and this error happens if Your API request unprocessable That's mean The API received your request but it could not handle your request
* -- For example, if you delete a question that does not exist, 
* An example of a response: 
    ```json
       {
        'code':422,
        'message':'unprocessable',
        'success':False
        }
    ```
    
### 400 Bad Request:

* JSON response will return and this error happens if you send A bad request the API could not understand it 
* -- For example,  send Not JSON body to the POST / Patch endpoints,
* An example of a response: 
    ```json
       {
        'code':400,
        'message':'bad request',
        'success':False
        }
    ```
    
### 405 Method not allowed:
* It's an HTTP response status code that indicates that the request method is known by the server but is not supported by the target resource
* -- For example,  send post request to endpoint that accept only Patch or GET requests
* JSON response will return and this error happens if used A wrong Method in your request 

* An example of a response: 
    ```json
       {
        'code':405,
        'message':'method not allowed',
        'success':False
        }
    ```
    
    
### 409 conflict:
* It's an HTTP response status code returned when you try create a question that already exist

* An example of a response: 
    ```json
        {
        'code':409,
        'message':'the question cannot be added, because it already exists',
        'success':False
       }
    ``` 
    
    # GET All Questions [GET]
    * path: localhost:5000/questions  || localhost:5000/questions?page={page-number}
    
            * return all questions paginated list of the questions start from page 1 each page contains 10 questions 
            * this path accept one query paramter which is the page
            * example:  curl http://localhost:5000/questions
            
    
    ```
        {
          "categories": [
            "history",
            "entertainment",
            "geography",
            "sport",
            "science",
            "art"
          ],
          "current_category": "5",
          "questions": [
            {
              "answer": "becuase I forced to use it",
              "category": "5",
              "difficulty": 1,
              "id": 114,
              "question": "why react is bad"
            },
            {
              "answer": "True",
              "category": "art",
              "difficulty": 2,
              "id": 56,
              "question": "3-leonardo da vinci is famous painter?"
            },
            {
              "answer": "more than 300",
              "category": "art",
              "difficulty": 5,
              "id": 57,
              "question": "4-how many michelangelo paintings are there?"
            },
            {
              "answer": "true",
              "category": "art",
              "difficulty": 5,
              "id": 65,
              "question": "12-drawing was the first discoverd art"
            },
            {
              "answer": "true",
              "category": "art",
              "difficulty": 5,
              "id": 64,
              "question": "11-without music no good code?"
            },
            {
              "answer": "true",
              "category": "art",
              "difficulty": 5,
              "id": 63,
              "question": "10-music and drawing exist in nutrial before human use?"
            },
            {
              "answer": "piano",
              "category": "art",
              "difficulty": 1,
              "id": 62,
              "question": "9-which easiet music tool to play?"
            },
            {
              "answer": "7",
              "category": "art",
              "difficulty": 5,
              "id": 61,
              "question": "8-how many cords in music?"
            },
            {
              "answer": "True",
              "category": "art",
              "difficulty": 3,
              "id": 60,
              "question": "7-music help to relax?"
            },
            {
              "answer": "False",
              "category": "art",
              "difficulty": 3,
              "id": 59,
              "question": "6-we can not draw paint with one color?"
            }
          ],
          "success": true,
          "total_questions": 109
       }
   ```
     * Example OF query with page paramter
     *  curl http://localhost:5000/questions?page=999999
      
      ```
          {
            "categories": [
              "history",
              "entertainment",
              "geography",
              "sport",
              "science",
              "art"
            ],
            "current_category": "5",
            "questions": [],
            "success": true,
            "total_questions": 109
          }
      ```

     
    # DELETE Questions  [POST]
    * path: localhost:5000/questions/<question_id>
    * You can use this path to delete a question using question ID
    * Curl example : ```curl -X DELETE http://localhost:5000/questions/59```
    
    ```
        {
         "deleted": 59,
         "questions": [
           {
             "answer": "becuase I forced to use it",
             "category": "5",
             "difficulty": 1,
             "id": 114,
             "question": "why react is bad"
           },
           {
             "answer": "True",
             "category": "art",
             "difficulty": 1,
             "id": 54,
             "question": "1-screem is famous paint?"
           },
           {
             "answer": "true",
             "category": "art",
             "difficulty": 5,
             "id": 65,
             "question": "12-drawing was the first discoverd art"
           },
           {
             "answer": "true",
             "category": "art",
             "difficulty": 5,
             "id": 64,
             "question": "11-without music no good code?"
           },
           {
             "answer": "true",
             "category": "art",
             "difficulty": 5,
             "id": 63,
             "question": "10-music and drawing exist in nutrial before human use?"
           },
           {
             "answer": "piano",
             "category": "art",
             "difficulty": 1,
             "id": 62,
             "question": "9-which easiet music tool to play?"
           },
           {
             "answer": "7",
             "category": "art",
             "difficulty": 5,
             "id": 61,
             "question": "8-how many cords in music?"
           },
           {
             "answer": "True",
             "category": "art",
             "difficulty": 3,
             "id": 60,
             "question": "7-music help to relax?"
           },
           {
             "answer": "more than 300",
             "category": "art",
             "difficulty": 5,
             "id": 57,
             "question": "4-how many michelangelo paintings are there?"
           },
           {
             "answer": "True",
             "category": "art",
             "difficulty": 2,
             "id": 56,
             "question": "3-leonardo da vinci is famous painter?"
           }
         ],
         "success": true,
         "total_questions": 108
       }     
    ```
     * example of errors:
     * [Bad-Request: 400, resource-not-found 404]
     * Delete item that is not exist:
     * ``` curl -X DELETE http://localhost:5000/questions/666 ``` [resource-not-found]
      ```
          }    
      
          "code": 404,
      
          "message": "resource not found",
      
          "success": false
      
          }
   
     ```
     
    # GET Questions By category ID  [GET]
    * path: http://localhost:5000/categories/<category_id>/questions
    * this path used to return questions using category id with pagenation list each request return 10 questions
    * it will search for the category in the database if it exist it will return list of the questions else will return 404 error
    * IT required to use the category id or it will return 404 error
    * example of CURL request: ``` curl -X GET http://localhost:5000/categories/1/questions ```
    ```
      {
           "categories": [
           {
             "id": 1,
             "type": "html"
           },
           {
             "id": 2,
             "type": "python"
           },
           {
             "id": 3,
             "type": "javascript"
           },
           {
             "id": 4,
             "type": "history"
           },
           {
             "id": 5,
             "type": "entertainment"
           },
           {
             "id": 6,
             "type": "geography"
           },
           {
             "id": 7,
             "type": "sport"
           },
           {
             "id": 8,
             "type": "science"
           },
           {
             "id": 9,
             "type": "art"
           }
         ],
         "current_category": "html",
         "questions": [
           {
             "answer": "h1",
             "category": "html",
             "difficulty": 1,
             "id": 3,
             "question": "what is larget HTML heading"
           },
           {
             "answer": "ol",
             "category": "html",
             "difficulty": 1,
             "id": 4,
             "question": "which tag is used to define ordered list?"
           },
           {
             "answer": "<ul>",
             "category": "html",
             "difficulty": 1,
             "id": 5,
             "question": "which tag is used to define bulleted list?"
           },
           {
             "answer": "True",
             "category": "html",
             "difficulty": 2,
             "id": 6,
             "question": "you can insert SVG directly to HTML?"
           },
           {
             "answer": "<br>",
             "category": "html",
             "difficulty": 2,
             "id": 7,
             "question": "which tag used to add line break in html?"
           },
           {
             "answer": "w3schools",
             "category": "html",
             "difficulty": 4,
             "id": 8,
             "question": "Where Did Python King Learned HTML?"
           }
         ],
         "success": true,
         "total_questions": 6
       }   
    
    ```
     * Errors from this path:
      ``` curl -X GET http://localhost:5000/categories/999/questions ```
      
     
     ```
      {
        "code": 404,
        "message": "resource not found",
        "success": false
      }

      ```
      
      
    
    # GET Questions By category type  [GET]
    * path:  http://localhost:5000/categories/<category>/questions
    * curl example: ```curl -X GET http://localhost:5000/categories/art/questions
    
    ```
        {  
            "categories": [
           {
             "id": 1,
             "type": "html"
           },
           {
             "id": 2,
             "type": "python"
           },
           {
             "id": 3,
             "type": "javascript"
           },
           {
             "id": 4,
             "type": "history"
           },
           {
             "id": 5,
             "type": "entertainment"
           },
           {
             "id": 6,
             "type": "geography"
           },
           {
             "id": 7,
             "type": "sport"
           },
           {
             "id": 8,
             "type": "science"
           },
           {
             "id": 9,
             "type": "art"
           }
         ],
         "current_category": "art",
         "questions": [
           {
             "answer": "True",
             "category": "art",
             "difficulty": 1,
             "id": 54,
             "question": "1-screem is famous paint?"
           },
           {
             "answer": "False",
             "category": "art",
             "difficulty": 1,
             "id": 55,
             "question": "2-monalisa is non famous paint?"
           },
           {
             "answer": "True",
             "category": "art",
             "difficulty": 2,
             "id": 56,
             "question": "3-leonardo da vinci is famous painter?"
           },
           {
             "answer": "more than 300",
             "category": "art",
             "difficulty": 5,
             "id": 57,
             "question": "4-how many michelangelo paintings are there?"
           },
           {
             "answer": "True",
             "category": "art",
             "difficulty": 3,
             "id": 60,
             "question": "7-music help to relax?"
           },
           {
             "answer": "7",
             "category": "art",
             "difficulty": 5,
             "id": 61,
             "question": "8-how many cords in music?"
           },
           {
             "answer": "piano",
             "category": "art",
             "difficulty": 1,
             "id": 62,
             "question": "9-which easiet music tool to play?"
           },
           {
             "answer": "true",
             "category": "art",
             "difficulty": 5,
             "id": 63,
             "question": "10-music and drawing exist in nutrial before human use?"
           },
           {
             "answer": "true",
             "category": "art",
             "difficulty": 5,
             "id": 64,
             "question": "11-without music no good code?"
           },
           {
             "answer": "true",
             "category": "art",
             "difficulty": 5,
             "id": 65,
             "question": "12-drawing was the first discoverd art"
           }
         ],
         "success": true,
         "total_questions": 10
      }
    ```
    
    example of errors:
       `` curl http://localhost:5000/categories/or/questions ```
       
       ```
         {      
           "code": 404,
           "message": "resource not found",
           "success": false
         }
  
       ```
    
    
    # Play Questions Game  [POST]
    * path: http://localhost:5000/play  || http://localhost:5000/quizzes
    * this path for play questions game it take a list of previous question or string contains the privous question or tuple and the category
    * the previous question is required else it will return 422 error if not provided, how it works it take the previous question and category if any
    * then return new question with the answer and the previous question
    * example curl 
    *  ``` curl -d '{"previous_questions":"2-what are the second planet?"}' -H "Content-Type: application/json" -X POST http://localhost:5000/quizzes ```

    ```
        {
          "answer": "True",
          "previousQuestions": "2-what are the second planet?",
          "question": "9-basketball is famous is footbal in USA?",
          "visibleAnswer": "True"
        }
    ```
    
    
    * or send category with previousQuestions question
     ```
      curl -d '{"previous_questions":"9-basketball is famous is footbal in USA?","quiz_category":"python"}'\
      -H "Content-Type: application/json" -X POST     http://localhost:5000/quizzes
    ```  
      
     ```
       {
         "answer": "False",
         "previous_question": "?",
         "question": "in python, for loop used to define a var?",
         "visibleAnswer": "False"
       }
     ```
     
     errors may retunred:
     
     `` curl -d '{""}' -H "Content-Type: application/json" -X POST http://localhost:5000/quizzes ```
     
     ```
        { 
          "code": 400,
          "message": "bad request",
          "success": false
        }
 
     ```
     
     ``` curl -d '{"error":"true"}' -H "Content-Type: application/json" -X POST http://localhost:5000/quizzes ```
     
     ```
       {   
       "code": 422,
       "message": "unprocessable",
       "success": false
       }

     ```
     
     

# POST New Questions Or Search Question  [POST]
* path: localhost:5000/add  ||  localhost:5000/questions 
* This endpoint handle to requests first one for creating new question and the other one for search a question
* if your request body not contains searchTerm or ['question', 'answer', 'category', 'difficulty'] it will return error code [422]
* !Note this endpoint will not duplicate the questions it will return Confilt error [409] id You DID 
* example of create request

 ``` curl -d '{"question":"in python, def keyword define to define var?", "answer":"True","category":"python", "difficulty":"4" }'\
 -H "Content-Type: application/json" -X POST http://localhost:5000/questions ```


      ```
          "added": 115,
          "list": [
            {
              "answer": "True",
              "category": "entertainment",
              "difficulty": 1,
              "id": 107,
              "question": "12-Can country focus in movies and leave the poepole without work or learn?"
            },
            {
              "answer": "True",
              "category": "entertainment",
              "difficulty": 2,
              "id": 108,
              "question": "13-Ahmed el ska good actor?"
            },
            {
              "answer": "True",
              "category": "entertainment",
              "difficulty": 5,
              "id": 109,
              "question": "14-Karim abdl el aziz good actor?"
            },
            {
              "answer": "hls",
              "category": "entertainment",
              "difficulty": 3,
              "id": 110,
              "question": "15-What is top trending in Youtube egypt?"
            },
            {
              "answer": "True",
              "category": "entertainment",
              "difficulty": 3,
              "id": 111,
              "question": "16-does programing consider entertainment?"
            },
            {
              "answer": "True but will be bad",
              "category": "entertainment",
              "difficulty": 3,
              "id": 112,
              "question": "17-can one actor make movie alone?"
            },
            {
              "answer": "True",
              "category": "entertainment",
              "difficulty": 5,
              "id": 113,
              "question": "18-iam legend is good movie?"
            },
            {
              "answer": "becuase I forced to use it",
              "category": "5",
              "difficulty": 1,
              "id": 114,
              "question": "why react is bad"
            },
            {
              "answer": "True",
              "category": "python",
              "difficulty": 4,
              "id": 115,
              "question": "in python, def keyword define to define var?"
            }
          ],
          "success": true,
          "total_questions": 109
        }
      ```
      ```
* example of request to create a question that exist:


  ```
   curl -d '{"question":"in python, def keyword define to define var?", "answer":"True","category":"python", "difficulty":"4" }'\
   -H "Content-Type: application/json" -X POST http://localhost:5000/questions
   ``` 


    ```
    
      {   
       "code": 409,
       "message": "the question cannot be added, because it already exists",
       "success": false
      }
 
    
    ```
    
    * second error
     curl -d '{""}' -H "Content-Type: application/json" -X POST http://localhost:5000/questions
     
     ```
      {    
        "code": 400,
        "message": "bad request",
        "success": false
      }

     ```
    
     * third error:
     *  curl -d '{"question":"Do not Create?"}' -H "Content-Type: application/json" -X POST http://localhost:5000/questions  [Missing required parameters]
  
  ```
       {
      
       "code": 422,
      
       "message": "unprocessable",
      
       "success": false
      
       } 
  ```

     * if there internal error in the system it may return 500 [I added extra column name and value while adding to database]
 
      {
        "code": 500,
        "message": "Internal server error",
        "success": false
      }

```

 # search example
 * http://localhost:5000/questions/searchTerm=[question]
 * Insensitive "searchTerm" will search for the search term if it is a substring of an existing question
 * example: ``` curl -d '{"searchTerm":"html"}' -H "Content-Type: application/json" -X POST http://localhost:5000/questions ```
 
        ```
 
        {
          "questions": [
           {
             "answer": "h1",
             "category": "html",
             "difficulty": 1,
             "id": 3,
             "question": "what is larget HTML heading"
           },
           {
             "answer": "True",
             "category": "html",
             "difficulty": 2,
             "id": 6,
             "question": "you can insert SVG directly to HTML?"
           },
           {
             "answer": "<br>",
             "category": "html",
             "difficulty": 2,
             "id": 7,
             "question": "which tag used to add line break in html?"
           },
           {
             "answer": "w3schools",
             "category": "html",
             "difficulty": 4,
             "id": 8,
             "question": "Where Did Python King Learned HTML?"
           },
           {
             "answer": "w3schools",
             "category": "history",
             "difficulty": 1,
             "id": 32,
             "question": "Where did Python King Learned HTML?"
           },
           {
             "answer": "True",
             "category": "html",
             "difficulty": 4,
             "id": 116,
             "question": "in HTML, def keyword define to define var?"
           },
           {
             "answer": "True",
             "category": "html",
             "difficulty": 4,
             "id": 117,
             "question": "in HTML, def keyword define to define loop?"
           }
         ],
         "title": [
           "my first advanced query"
         ],
         "total": 7
       }
 
      ```

      
#unitest


* There are 15 tests to make sure every thing is working fine, Please read the comments above every test IT will guide you how to run successfull tests
* Notes: You can not add duplicated category or questions, make sure you search to use cateogry id that already exist

# test functions:

1. test_success_categories
    * [Test GET categories IT must have category You can uncomment to create one Do not duplicate ]

2. test_get_all_questions
    * [Normal test to check the questions same it must have questions to get]

3. test_success_questions_with_parameter
    * [test get questions using the page query pramters]
    
4. test_missing_question
    * [test GET with invalid path adding 1000 to questions]

5. test_success_delete
    * [test delete question full dynamic]

6. test_success_post_question
    * [test adding new question Important note add 1 to HTML question there it must have same question in unsuccess_post_question]

7. test_unsuccess_post_question
    * [this test for check there are no duplicated question it must have same question used in test_success_post_question add 1 to HTML]

8.  test_unprocessable_post_request
     * [test invalid post request]
    
9.  test_conflict_post_request
     * [OUR API do not accept both requests from the same resource to make 2 actions Like search and create new question in same time] 
    
10.  test_success_search
      * [Test successfull search the searchTerm must be a substring in question]

11.  test_unsuccess_search
     *  [test unsuccess search make sure the search function will return questions which have the term in it always use mass word]

12.  test_success_categories_by_id
      *  [test geting the categgry by id]
 
13.  test_quiz_success_without_category
      *  [test the quiz game endpoint without sending category in body]

14.  test_quiz_success_with_category
     *  [ test the quiz within category in the request body ]

15. test_success_questions
     *  [this extra endpoint test it test getting category by type it must have the category and the test Database]

  


# Acknowledgements:

* https://udacity.com (advanced track)
* https://stackoverflow.com/questions



# Working with react APP:

!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/this.JPG)
!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/image.JPG)
!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/ok_test.JPG)
!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/this.JPG)

# pip8 tests
!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/no_errors3.JPG?raw=true)
!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/no_errors2.JPG?raw=true)
!['screenshoot'](https://github.com/MahmoudHegazi/Trivia-API/blob/main/no_errors3.JPG?raw=true)

