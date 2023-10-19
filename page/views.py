from django.shortcuts import render


# Отображение главной страницы.
def page_index(request):
    return render(request, 'page/page_index.html')
