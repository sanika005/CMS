import json
from django.shortcuts import render
from .models import UserModel, PostModel, LikeModel
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request,'home/index.html')

# User CURD API's
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        req = json.load(request)
        username = req['username']        
        email = req["email"]
        password = req["password"]
        user = UserModel(username=username,email=email,password=password)
        user.save()
        saved_data = {
            "id":user.id,
            "username":user.username,
            "email":user.email,
            "password":user.password,
        }
        return JsonResponse({"status":"success","payload":saved_data,"message":"User saved successfully"},status=200)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)
    
def read_user(request,pk):
    if request.method == 'GET':
        specific_user_data = UserModel.objects.get(id=pk)
        req = json.load(request)
        if int(req['user_id']) == int(specific_user_data.id):
            retrieved_data = {
                "id":specific_user_data.id,
                "username":specific_user_data.username,
                "email":specific_user_data.email,
                "password":specific_user_data.password,
            }
            return JsonResponse({"status":"success","retrieved_data":retrieved_data,"message":f"Corresponsing data for id:{pk}"},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized"}, status=401)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)

@csrf_exempt
def update_user(request,pk):
    try:
        specific_user_data = UserModel.objects.get(pk=pk)
    except:
        return JsonResponse({"status":"User not found","status":404})
    
    if request.method == "PUT":
        # try:
        req = json.load(request)
        if int(req['user_id']) == int(specific_user_data.id):
            specific_user_data.username = req.get("username",specific_user_data.username)
            specific_user_data.email = req.get("email",specific_user_data.email)
            specific_user_data.password = req.get("password",specific_user_data.password)
            specific_user_data.save()
            updates_data = {
                "id":specific_user_data.id,
                "username":specific_user_data.username,
                "email":specific_user_data.email,
                "password":specific_user_data.password,
            }
            return JsonResponse({"status":"success","updated_data":updates_data},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized"}, status=401)
        
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)
@csrf_exempt    
def delete_user(request,pk):
    try:
        specific_user_data = UserModel.objects.get(pk=pk)
    except:
        return JsonResponse({"status":"User not found"},status=404)
    
    if request.method == "DELETE":
        # try:
        req = json.load(request)
        if int(req['user_id']) == int(specific_user_data.id):
            specific_user_data.delete()
            return JsonResponse({"status":"success","message":"User deleted successfully"},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized"}, status=401)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)

# Post CURD API's
@csrf_exempt
def create_post(request):
    if request.method == "POST":
        req = json.load(request)
        user_id = int(req["user_id"])
        title = req["title"]
        description = req["description"]
        content = req["content"]
        creation_date = req["creation_date"]
        is_public = req["is_public"]
        post = PostModel(user_id=user_id,title=title,description=description,content=content,creation_date=creation_date,is_public=is_public)
        post.save()
        saved_data = {
            "id":post.id,
            "user_id":post.user_id,
            "title":post.title,
            "description":post.description,
            "content":post.content,
            "creation_date":post.creation_date,
            "is_public":post.is_public
        }
        return JsonResponse({"status":"success","payload":saved_data,"message":"Post saved successfully"},status=200)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)
    
def read_post(request,pk):
    specific_user_data = PostModel.objects.filter(pk=pk).values()
    req = json.load(request)
    if specific_user_data[0]['is_public']==True:
        result=specific_user_data[0]
    else:
        if int(req['user_id']) == int(specific_user_data[0]['user_id']):
            result=specific_user_data[0]
            return JsonResponse({"status":"success","payload":result,"message":"Post read successfully"},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized request"},status=401)
    return JsonResponse({"status":"success","retrieved_data":result,"message":f"Corresponsing data for id:{pk}"},status=200)

@csrf_exempt
def update_post(request, pk):
    req = json.load(request)
    if request.method == "PUT":
        try:
            specific_post_data = PostModel.objects.get(pk=pk)
        except:
            return JsonResponse({"status":"Post not found","status":404})
        
        if int(req['user_id']) == int(specific_post_data.user_id):
            try:
                specific_post_data.user_id = req.get("user_id",specific_post_data.user_id)
                specific_post_data.title = req.get("title",specific_post_data.title)
                specific_post_data.description = req.get("description",specific_post_data.description)
                specific_post_data.content = req.get("content",specific_post_data.content)
                specific_post_data.creation_date = req.get("creation_date",specific_post_data.creation_date)
                specific_post_data.is_public = req.get("is_public",specific_post_data.is_public)
                specific_post_data.save()
                updates_data = {
                    "id":specific_post_data.id,
                    "title":specific_post_data.title,
                    "description":specific_post_data.description,
                    "content":specific_post_data.content,
                    "creation_date":specific_post_data.creation_date,
                    "is_public":specific_post_data.is_public,
                }
                return JsonResponse({"status":"success","updated_data":updates_data},status=200)
            except json.decoder.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON provided'}, status=400)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized request"},status=401)
@csrf_exempt        
def delete_post(request, pk):
    try:
        specific_post_data = PostModel.objects.get(pk=pk)
    except:
        return JsonResponse({"status":"Post not found"},status=404)
    
    if request.method == "DELETE":
        req = json.load(request)
        if int(req['user_id']) == int(specific_post_data.user_id):
            specific_post_data.delete()
            return JsonResponse({"status":"success","message":"Post deleted successfully"},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized"}, status=401)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)
    
def list_post(request):
    result=[]
    try:
        posts = PostModel.objects.all().filter(is_public=True).values('id','title')
        req = json.load(request)
        for i in posts:
            likes = LikeModel.objects.filter(post_id=i['id']).count()
            i['likes']=likes
            result.append(i)
        posts = PostModel.objects.all().filter(is_public=False,user_id=req['user_id']).values('id','title')
        for i in posts:
            likes = LikeModel.objects.filter(post_id=i['id']).count()
            i['likes']=likes
            result.append(i)
        return JsonResponse({"status":"success","payload":result}, status=200)
    except Exception as e:
        return JsonResponse({"message":str(e)}, status=500)
    
# like CURD API's
@csrf_exempt
def create_like(request):
    if request.method == "POST":
        req = json.load(request)
        user_id = req["user_id"]
        post_id = req["post_id"]
        like = LikeModel(user_id=user_id,post_id=post_id)
        like.save()
        saved_data = {
            "id":like.id,
            "user_id":like.user_id,
            "post_id":like.post_id
        }
        return JsonResponse({"status":"success","payload":saved_data,"message":"Like saved successfully"},status=200)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)
    

def read_like(request,pk):
    specific_like_data = LikeModel.objects.filter(pk=pk).values()
    req = json.load(request)
    post_data = PostModel.objects.filter(id=specific_like_data[0]['post_id'])
    user_data = UserModel.objects.filter(id=specific_like_data[0]['user_id'])

    if post_data.is_public==True:
        result = {
            "post_title":post_data.title,
            "user_name":user_data.username,
        }
        return JsonResponse({"status":"success","payload":result},status=200)
    else:
        if int(req['user_id']) == int(user_data.id):
            result = {
                 "post_title":post_data.title,
                "user_name":user_data.username,
            }
            return JsonResponse({"status":"success","payload":result},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized request"},status=401)

@csrf_exempt
def update_like(request,pk):
    req = json.load(request)
    if request.method == "PUT":
        try:
            specific_like_data = LikeModel.objects.get(pk=pk)
            specific_post_data = PostModel.objects.filter(id=specific_like_data.post_id).values()
        except:
            return JsonResponse({"status":"Like not found","status":404})
        if int(req['user_id']) == int(specific_like_data.user_id):
            try:
                specific_like_data.post_id = req.get("post_id",specific_like_data.post_id)
                specific_like_data.save()
                updated_data = {
                    "id":specific_like_data.id,
                    "post_title":specific_post_data[0]['title'],
                }
                return JsonResponse({"status":"success","updated_data":updated_data},status=200)
            except json.decoder.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON provided'}, status=400)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized request"},status=401)
        
@csrf_exempt
def delete_like(request,pk):
    try:
        specific_like_data = LikeModel.objects.get(pk=pk)
    except:
        return JsonResponse({"status":"Like not found"},status=404)
    
    if request.method == "DELETE":
        # try:
        req = json.load(request)
        if int(req['user_id']) == int(specific_like_data.user_id):
            specific_like_data.delete()
            return JsonResponse({"status":"success","message":"Like deleted successfully"},status=200)
        else:
            return JsonResponse({"status":"Fail","message":"Unauthorized"}, status=401)
    else:
        return JsonResponse({"status":"Fail","message":"Bad request"}, status=400)
    