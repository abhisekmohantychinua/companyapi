from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page called")
    friends = [
        'abhisek',
        'subhransu',
        'jaga',
        'saroj'
    ]
    return JsonResponse(friends, safe=False)
