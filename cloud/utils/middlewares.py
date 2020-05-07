# date : 2019/11/27 12:05     

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect



class M1(MiddlewareMixin):


    def process_request(self, request):

        path = request.path
        username = str(request.user)
        if path in ['/delete_file/', '/upload_file/', '/mkdir/', '/delete_folder/', '/rename_file/', '/rename_folder/']:
            if username != 'admin':
                return redirect('/')
            else:
                return None
        else:
            return None


