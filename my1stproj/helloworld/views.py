from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    # just remembe, values could be retreived from
    # variales, forms, or database or other sources
    context = {
        "name": request.GET.get("name", ""),
        "major": "Mis",
        "gpa": 4.0,
        "students": ["mohammad", "ahmed", "sara", "khaled"],

    }
    return render(request, "hello.html", context)
