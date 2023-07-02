from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

# Create your views here.
def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.save()
            return redirect('comments:comments')
    else:
        form = CommentForm()
    comments_all = Comment.objects.all()
    return render(request, 'comments/comments.html', {'form' : form, 'comments' : comments_all})