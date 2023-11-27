from django.shortcuts import render
import markdown2
from django import forms

from . import util

class SearchForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput({ "placeholder": "Search Encyclopedia",'class': 'search'}))


def index(request):
    if request.method == "POST":
        lst = []
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["search"].lower()
            entries = util.list_entries()
            for entry in entries:
                if query == entry.lower():
                    entry_t = util.get_entry(entry)
                    entry_send = markdown2.markdown(entry_t)
                    return render(request, "encyclopedia/entry_page.html", {
                        "title": entry,
                        "entry": entry_send,
                        "form": SearchForm()
                    })
                elif query in entry.lower():
                    lst.append(entry)
            return render(request, "encyclopedia/search_page.html", {
                "lst": lst,
                "form": SearchForm()
            })




    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })

def entry_page(request, title):
    if request.method == "POST":
        lst = []
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["search"].lower()
            entries = util.list_entries()
            for entry in entries:
                if query == entry.lower():
                    entry_t = util.get_entry(entry)
                    entry_send = markdown2.markdown(entry_t)
                    return render(request, "encyclopedia/entry_page.html", {
                        "title": entry,
                        "entry": entry_send,
                        "form": SearchForm()
                    })
                elif query in entry.lower():
                    lst.append(entry)
            return render(request, "encyclopedia/search_page.html", {
                "lst": lst,
                "form": SearchForm()
            })

    entry = util.get_entry(title.capitalize())
    if entry != None:
        entry_send = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry_page.html", {
            "title": title.capitalize(),
            "entry": entry_send,
            "form": SearchForm()
        })
    else:
        entry = util.get_entry(title.upper())
        if entry != None:
            entry_send = markdown2.markdown(entry)
            return render(request, "encyclopedia/entry_page.html", {
                "title": title.upper(),
                "entry": entry_send,
                "form": SearchForm()
            })
        else:
            return render(request, "encyclopedia/entry_page.html", {
                
                "entry": ' the requested page was not found',
                "form": SearchForm()
            })
        
def create_page(request):
    return render(request, "encyclopedia/create_page.html", {
                "form": SearchForm()
            })