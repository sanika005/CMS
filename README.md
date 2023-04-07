# CMS
# Inside the CMS folder you will get the manage.py file.
# To run the server command is: "python manage.py runserver"
# For accessing User CURD API's the endpoints should be like
    1. http://127.0.0.1:8000/user/create
    2. http://127.0.0.1:8000/user/read/ (provide id,and in body also provide user_id)
    3. http://127.0.0.1:8000/user/update/ (provide id)
    4. http://127.0.0.1:8000/user/delete/ (provide id)
# For accessing Post CURD API's the endpoints should be like
    1. http://127.0.0.1:8000/post/create
    2. http://127.0.0.1:8000/post/read/ (provide id)
    3. http://127.0.0.1:8000/post/update/ (provide id)
    4. http://127.0.0.1:8000/post/delete/ (provide id)
    5. http://127.0.0.1:8000/post/list (fetch all posts data with no of like for each post)
# For accessing Like CURD API's the endpoints should be like
    1. http://127.0.0.1:8000/like/create
    2. http://127.0.0.1:8000/like/read/ (provide id)
    3. http://127.0.0.1:8000/post/update/ (provide id)
    4. http://127.0.0.1:8000/like/delete/1 (provide id)

# Access to the PUT/DELETE API's for post retricted to the owner of post is done.
# GET all posts if public and there is some private post then it will be visible to owner of post only is done.
# Retrieval of both the post/blog and its likes should be completed within a single query is done.
# Also added the postman collection CMS.postman_collection.json to the repository.