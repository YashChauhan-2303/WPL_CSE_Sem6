from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import models
from .models import Category, Page
from .forms import CategoryForm, PageForm


# Category Views
class CategoryListView(ListView):
    """Display all categories"""
    model = Category
    template_name = 'directory/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10


class CategoryDetailView(DetailView):
    """Display pages in a specific category"""
    model = Category
    template_name = 'directory/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = self.object.pages.all()
        return context


class CategoryCreateView(CreateView):
    """Create a new category"""
    model = Category
    form_class = CategoryForm
    template_name = 'directory/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, f'Category "{form.cleaned_data["name"]}" created successfully!')
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    """Update a category"""
    model = Category
    form_class = CategoryForm
    template_name = 'directory/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, f'Category "{form.cleaned_data["name"]}" updated successfully!')
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    """Delete a category"""
    model = Category
    template_name = 'directory/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Category deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Page Views
class PageListView(ListView):
    """Display all pages"""
    model = Page
    template_name = 'directory/page_list.html'
    context_object_name = 'pages'
    paginate_by = 15


class PageDetailView(DetailView):
    """Display page details"""
    model = Page
    template_name = 'directory/page_detail.html'
    context_object_name = 'page'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.views += 1
        self.object.save()
        self.object.category.visits += 1
        self.object.category.save()
        return response


class PageCreateView(CreateView):
    """Create a new page"""
    model = Page
    form_class = PageForm
    template_name = 'directory/page_form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        messages.success(self.request, f'Page "{form.cleaned_data["title"]}" created successfully!')
        return super().form_valid(form)


class PageUpdateView(UpdateView):
    """Update a page"""
    model = Page
    form_class = PageForm
    template_name = 'directory/page_form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        messages.success(self.request, f'Page "{form.cleaned_data["title"]}" updated successfully!')
        return super().form_valid(form)


class PageDeleteView(DeleteView):
    """Delete a page"""
    model = Page
    template_name = 'directory/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Page deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Like functionality
def like_category(request, pk):
    """Increment likes for a category"""
    category = get_object_or_404(Category, pk=pk)
    category.likes += 1
    category.save()
    messages.success(request, f'You liked "{category.name}"! ❤️')
    return redirect('category_detail', pk=category.pk)


# Dashboard view
def index(request):
    """Dashboard view showing statistics"""
    categories_count = Category.objects.count()
    pages_count = Page.objects.count()
    total_visits = Category.objects.values_list('visits', flat=True).aggregate(sum=models.Sum('visits'))['sum'] or 0
    total_likes = Category.objects.aggregate(sum=models.Sum('likes'))['sum'] or 0
    
    context = {
        'categories_count': categories_count,
        'pages_count': pages_count,
        'total_visits': total_visits,
        'total_likes': total_likes,
        'categories': Category.objects.all()[:5],
        'pages': Page.objects.all()[:5],
    }
    return render(request, 'directory/index.html', context)
