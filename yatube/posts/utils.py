#def pagination_process(request, posts):
#    paginator = Paginator(posts, SELECT_LIMIT)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    return page_obj
# Не работает при импорте в views, функция работает только внутри самого views
