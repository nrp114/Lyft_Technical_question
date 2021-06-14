from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        string_to_cut = request.POST.get("string_to_cut", "")
        data = {
            'return_string': "",
        }
        return_string_temp = ""
        for i in range(len(string_to_cut)):
            if (i + 1) % 3 == 0:
                return_string_temp += string_to_cut[i]
        print(return_string_temp)
        data['return_string'] = return_string_temp
        return JsonResponse(data)
    else:
        data = {
            'return_string' : "Please send a POST request"
        }
        return JsonResponse(data)
