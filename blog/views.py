from django.shortcuts import render, redirect
from blog.models import Post, Restaurant

# Create your views here.

def index(request):
    # 전체 포스팅을 가져올 준비(아직 가져오지는 않음)
    post_qs = Post.objects.all().order_by('-id')  #qs : querySet

    return render(request, "blog/index.html", {
        "post_list" : post_qs,
    })


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)  # pk 가 10인 값
    return render(request, "blog/single_post_page.html", {
        "post" : post,
    })



from django.views.generic import CreateView
from blog.forms import PostForm, ResForm

# post_new = CreateView.as_view(
#     form_class =PostForm,
#     model=Post,
#     success_url = "/blog/"
# )


def post_new(request):
    # print("methode = " ,request.method)
    # print("POST = ", request.POST)
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():  # 모든 유효성 검사를 진행한다.
            #유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save()  #ModelForm에서 지원 - 즉시 db로 저장하는 코드

            # return redirect("/blog/")  #import 해야해
            # return redirect(f'/blog/{post.pk}/')
            # return redirect(post.get_absolute_url())
            return redirect(post)

    return render(request, "blog/post_form.html", {
        "form" : form, 
    })

def restaurant(request):
        # 전체 포스팅을 가져올 준비(아직 가져오지는 않음)
    res_qs = Restaurant.objects.all().order_by('-id')  #qs : querySet

    return render(request, "blog/restaurant.html", {
        "res_list" : res_qs,
    })

def res_single_page(request, pk):
    res = Restaurant.objects.get(pk=pk)  # pk 가 10인 값
    return render(request, "blog/res_single_page.html", {
        "res" : res,
    })

def res_new(request):
    # print("methode = " ,request.method)
    # print("POST = ", request.POST)
    if request.method == 'GET':
        res_form = ResForm()
    else:
        res_form = ResForm(request.POST)
        if res_form.is_valid():  # 모든 유효성 검사를 진행한다.
            #유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            rest = res_form.save()  #ModelForm에서 지원 - 즉시 db로 저장하는 코드

            # return redirect("/blog/")  #import 해야해
            # return redirect(f'/blog/{post.pk}/')
            # return redirect(post.get_absolute_url())
            return redirect(rest)

    return render(request, "blog/res_new.html", {
        "res_form" : res_form, 
    })