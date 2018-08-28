# info views
from django.shortcuts import render

# Create your views here.
def contact(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    return render(request, 'info/contact.html')
    
def shipping(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    return render(request, 'info/shipping.html')
    
def faq(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    return render(request, 'info/faq.html')