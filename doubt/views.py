from django.shortcuts import render,HttpResponse,redirect
from .models import PostQuery,PostComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras


# Create your views here.
def queryhome(request):
    allquery = PostQuery.objects.all()
    context = {'allquery':allquery}
    return render(request,'query/queryhome.html',context)


def postquery(request):
    if request.method =='POST':
        title = request.POST['title']
        detail = request.POST['detail']
        user = request.user
        print(title,detail)
        if len(title)<2 or len(detail)<4:
            messages.error(request,"Please Ask Query correctly")
        else:
            allquery = PostQuery(title=title, detail=detail,user=user)
            allquery.save()
            messages.success(request,'Your Query has been successfully submit')
    
    return redirect("/")
    

def querypost(request, slug):
    post =  PostQuery.objects.filter(slug=slug).first()
    comments = PostComment.objects.filter(post=post,parent=None)
    replies = PostComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {"post":post,"comments":comments,"user":request.user,'replyDict':replyDict}
    return render(request,'query/querypost.html',context)

def postcomment(request):
    if request.method =='POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = PostQuery.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment = PostComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:

            parent= PostComment.objects.get(sno=parentSno)
            comment= PostComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/doubt/{post.slug}")
    
