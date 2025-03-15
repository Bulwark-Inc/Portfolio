from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Blog, Comment
from .forms import CommentForm
from django.db.models import Q



@require_GET
def blog_list(request):
    """
    Handles both normal and AJAX blog list requests:
    - Filters by search query and category
    - Paginates results
    - Returns JSON if AJAX, or renders full template if normal request
    """

    # Get query params
    query = request.GET.get('q')
    category = request.GET.get('category')
    page_number = request.GET.get('page')

    # Start base queryset
    blogs = Blog.objects.all()

    # Filter by search query
    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # Filter by category
    if category:
        blogs = blogs.filter(category=category)

    # Pagination setup (6 blogs per page)
    paginator = Paginator(blogs, 6)
    page_obj = paginator.get_page(page_number)

    # Get distinct categories (for dropdown)
    categories = Blog.objects.values_list('category', flat=True).distinct()

    # Handle AJAX request separately
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            'partials/blog_card.html',
            {'blogs': page_obj}  # use paginated blogs!
        )
        return JsonResponse({'html': html})

    # Regular page render
    context = {
        'blogs': page_obj,
        'query': query,
        'category': category,
        'categories': categories
    }

    return render(request, 'blogs/blog_list.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(approved=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = CommentForm()
    
    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blogs/blog_detail.html', context)
