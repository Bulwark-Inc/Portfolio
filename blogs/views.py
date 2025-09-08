from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from .models import Blog, Comment
from .forms import CommentForm
from django.db.models import Q


@require_GET
def blog_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    page_number = request.GET.get('page')

    # Filtered queryset
    blogs = Blog.objects.all().order_by('-created_at')

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    if category:
        blogs = blogs.filter(category__iexact=category)

    # Pagination
    paginator = Paginator(blogs, 6)
    page_obj = paginator.get_page(page_number)

    # Category dropdown
    categories = Blog.objects.values_list('category', flat=True).distinct().exclude(category__isnull=True)

    # AJAX response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('partials/blog_card.html', {'blogs': page_obj})
        return JsonResponse({
            'html': html,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'current_page': page_obj.number,
            'num_pages': paginator.num_pages,
        })

    context = {
        'blogs': page_obj,
        'query': query,
        'category': category,
        'categories': categories,
    }
    return render(request, 'blogs/blog_list.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(approved=True).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.name = comment.name.strip()
            comment.message = comment.message.strip()
            comment.save()
            messages.success(request, "Your comment has been submitted for review.")
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blogs/blog_detail.html', context)
