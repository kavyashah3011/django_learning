from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


blog_names = {
    "python-intro": "Introduction to Python programming.",
    "django-basics": "Basics of Django framework.",
    "python-oops": "Object-Oriented Programming in Python.",
    "regex": "Understanding Regular Expressions."
}

def home_page(request):
    return render(request, 'blogs/index.html')

def blogpost(request):
    list_item = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse('blog_post', args=[b])
        list_item += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
        
    res_data = f"<ul>{list_item}</ul>"
    return HttpResponse(res_data)

def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, 'blogs/post.html', {
            "blog_text": res, "blog_name": blog})
    except KeyError:
        return HttpResponseNotFound("Blog post not found.")