from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Notice, User, SavedNotice
from .forms import NewNoticeForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def notice_list_view(request):
    notices_list = Notice.objects.order_by('-created_at')
    paginator = Paginator(notices_list, 10)  # Show 10 notices per page

    page = request.GET.get('page')
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

 
    for notice in notices:
        notice.is_saved = SavedNotice.objects.filter(user=request.user, notice=notice).exists()

    return render(request, 'notices/home.html', {'notices': notices})


@login_required
def user_notice_list_view(request, username):
    user = get_object_or_404(User, username=username)
    notices_list = Notice.objects.filter(created_by=user).order_by('-created_at')
    paginator = Paginator(notices_list, 10)

    page = request.GET.get('page')
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

    return render(request, 'notices/notices_by_user.html', {'notices': notices, 'user': user})

@login_required
def notice_view(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    is_saved = SavedNotice.objects.filter(user=request.user, notice=notice).exists()
    return render(request, 'notices/notice_page.html', {'notice': notice, 'is_saved': is_saved})

@login_required
def save_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    SavedNotice.objects.get_or_create(user=request.user, notice=notice)
    return redirect('notices:notice_view', notice_id=notice.id)

@login_required
def remove_saved_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    SavedNotice.objects.filter(user=request.user, notice=notice).delete()
    return redirect('notices:notice_view', notice_id=notice.id)

@login_required
def saved_notice_list_view(request):
    saved_notices_list = SavedNotice.objects.filter(user=request.user).select_related('notice').order_by('-saved_at')
    paginator = Paginator(saved_notices_list, 9)

    page = request.GET.get('page')
    try:
        saved_notices = paginator.page(page)
    except PageNotAnInteger:
        saved_notices = paginator.page(1)
    except EmptyPage:
        saved_notices = paginator.page(paginator.num_pages)

    return render(request, 'notices/saved_notice_list.html', {'saved_notices': saved_notices})

@staff_member_required
def new_notice_page(request):
    if request.method == 'POST':
        form = NewNoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            return redirect('notices:notice_view', notice_id=notice.pk)
    else:
        form = NewNoticeForm()
    return render(request, 'notices/new_notice.html', {'form': form})
