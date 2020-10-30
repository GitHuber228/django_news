from django.shortcuts import render
from django.views.generic import DetailView, ListView

from comments.forms import PostCommentForm
from email_notification.forms import MailUsForm
from news import services


def handler404(request, exception):
    return render(request, 'news/page_not_found.html', status=404)


class PostView(DetailView):
    template_name = 'news/post.html'
    context_object_name = 'post'

    def get_queryset(self):
        return services.get_post_by_slug(self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_post'] = services.get_previous_post(context['post'])
        context['next_post'] = services.get_next_post(context['post'])
        context['related_post_list'] = services.get_related_post_list(context['post'])
        context['comment_form'] = PostCommentForm(self.request.POST)
        services.update_number_field(self.object, field='views', value=1, ip=self.request.META.get('REMOTE_ADDR'))
        return context


class PostCategoryView(ListView):
    template_name = 'news/category.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return services.get_post_by_category(self.kwargs['slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = services.get_category_by_slug(self.kwargs['slug'])
        return context


class PostTagView(ListView):
    template_name = 'news/tag.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return services.get_post_by_tag(self.kwargs['slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tag'] = services.get_tag_by_slug(self.kwargs['slug'])
        return context


def site_about_view(request):
    return render(request, 'news/about.html')


class SiteContactsView(ListView):
    template_name = 'news/contacts.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return services.get_site_settings()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = MailUsForm()
        return context


class PostAuthorView(ListView):
    template_name = 'news/author.html'
    context_object_name = 'post_list'
    slug_field = 'username'
    paginate_by = 5

    def get_queryset(self):
        return services.get_post_by_author(self.kwargs['slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['author'] = services.get_author_by_slug(self.kwargs['slug'])
        return context


class PostListView(ListView):
    context_object_name = 'post_list'
    template_name = 'news/index.html'
    paginate_by = 5

    def get_queryset(self):
        return services.get_post_list(start=2)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pinned_post_list'] = services.get_pinned_post_list()
        context['pinned_post_list_count'] = services.get_pinned_post_list().count()
        context['recent_post_list'] = services.get_recent_post_list(end=2)
        return context


class SearchPostView(ListView):
    context_object_name = 'post_list'
    template_name = 'news/search.html'
    paginate_by = 5

    def get_queryset(self):
        return services.get_post_list_by_search_filter(self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&"
        context['user_search'] = self.request.GET.get('search')
        return context
