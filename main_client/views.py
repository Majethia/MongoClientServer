from django.http import JsonResponse
from pymongo import MongoClient
import json

# Create your views here.
def say_hello(request):
    print(request)
    return JsonResponse({"data":"Hello world"})


def mongo_get_databases(request):
    database_url = request.GET['dburi']
    client = MongoClient(database_url, tls=True)
    dbs = client.list_databases()
    return JsonResponse ({'data': list(dbs)})

def mongo_get_collections(request):
    database_url = request.GET['dburi']
    database = request.GET['dbname']
    client = MongoClient(database_url, tls=True)
    cols = client[database].list_collection_names()
    return JsonResponse ({'data': list(cols)})

def mongo_get_all(request):
    database_url = request.GET['dburi']
    database = request.GET['dbname']
    collection = request.GET['col']
    client = MongoClient(database_url, tls=True)
    indexes = client[database][collection].find()
    return JsonResponse ({'data': list(indexes)})
    
def edit_doc(request):
    database_url = request.GET['dburi']
    database = request.GET['dbname']
    collection = request.GET['col']
    data = request.GET['data']
    data = json.loads(data)
    docid = data['_id']
    client = MongoClient(database_url, tls=True)
    try:
        client[database][collection].update_one({'_id':docid}, {"$set": data}, upsert=False)
        return JsonResponse({"data":data})
    except Exception as e:
        return JsonResponse({"data":str(e)})

def add_doc(request):
    database_url = request.GET['dburi']
    database = request.GET['dbname']
    collection = request.GET['col']
    data = request.GET['data']
    data = json.loads(data)
    print(data)
    client = MongoClient(database_url, tls=True)
    try:
        client[database][collection].insert_one(data)
        return JsonResponse({"data":data})
    except Exception as e:
        return JsonResponse({"data":str(e)})

def delete_doc(request):
    database_url = request.GET['dburi']
    database = request.GET['dbname']
    collection = request.GET['col']
    data = request.GET['data']
    data = json.loads(data)
    client = MongoClient(database_url, tls=True)
    try:
        client[database][collection].delete_one(data)
        return JsonResponse({"data":data})
    except Exception as e:
        return JsonResponse({"data":str(e)})