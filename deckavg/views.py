from django.shortcuts import render

def generic_page(request, header_title, page_header, template, extra_context=None):
    context = {'header_title': header_title, 'page_header': page_header, }
    if extra_context:
        context.update(extra_context)
    return render(request, template, context)

def index(request):
    return generic_page(request,
                        'Deck Averages',
                        'Deck Averages',
                        'deckavg/index.html',
                        extra_context={
                            'mtgtop8': 'https://www.mtgtop8.com/format?f=LE'
                        }
                        )
