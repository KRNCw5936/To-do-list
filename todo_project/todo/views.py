from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.utils.dateparse import parse_date

def index(request):
    search_query = request.GET.get('search', '')
    priority_filter = request.GET.get('priority_filter', '')
    
    items = TodoItem.objects.all()
    
    if search_query:
        items = items.filter(title__icontains=search_query)
    
    if priority_filter:
        items = items.filter(priority=priority_filter)
    
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(items, 10)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'todo/index.html', {'page_obj': page_obj})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = parse_date(request.POST.get('due_date'))
        category = request.POST.get('category')
        is_completed = request.POST.get('is_completed') == 'on'
        TodoItem.objects.create(title=title, description=description, priority=priority, due_date=due_date, category=category, is_completed=is_completed)
        return redirect('index')
    return render(request, 'todo/add.html')

def edit(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        item.priority = request.POST.get('priority')
        item.due_date = parse_date(request.POST.get('due_date'))
        item.category = request.POST.get('category')
        item.is_completed = request.POST.get('is_completed') == 'on'
        item.save()
        return redirect('index')
    return render(request, 'todo/edit.html', {'item': item})

def delete(request, id):
    item = get_object_or_404(TodoItem, id=id)
    item.delete()
    return redirect('index')