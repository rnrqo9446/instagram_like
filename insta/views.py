from django.shortcuts import render
from .models import Post
import operator

# Create your views here.
def main(request):
    posts = Post.objects.all()
    sort = request.GET.get('sort', '')
    
    if sort == 'new':
        posts = Post.objects.all()
    elif sort == 'like':
        ordered_posts = {}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key=operator.itemgetter(1), reverse=False)
        posts = []
        for post in post_list:
            print(post)
            posts.append(post[0])
        
            # 게시글만 어펜드 해준다!
        # 딕셔너리 자료형으로 바로 보낼 수 없으니 리스트로 변환해서 보내준다!! 그냥 형식 문제임!

    
    return render(request, 'insta/main.html', {'posts':posts,})


