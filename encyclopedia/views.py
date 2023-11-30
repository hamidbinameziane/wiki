from django.shortcuts import render
import markdown2
from django import forms

from . import util
import random

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
                        "random_entry":random_page(),
                    })
                elif query in entry.lower():
                    lst.append(entry)
            return render(request, "encyclopedia/search_page.html", {
                "lst": lst,
                "random_entry":random_page(),
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm(),
        "random_entry":random_page(),
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
                        "random_entry":random_page(),
                    })
                elif query in entry.lower():
                    lst.append(entry)
            return render(request, "encyclopedia/search_page.html", {
                "lst": lst,
                "random_entry":random_page(),
            })

    entry = util.get_entry(title.capitalize())
    if entry != None:
        entry_send = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry_page.html", {
            "title": title.capitalize(),
            "entry": entry_send,
            "random_entry":random_page(),
        })
    else:
        entry = util.get_entry(title.upper())
        if entry != None:
            entry_send = markdown2.markdown(entry)
            return render(request, "encyclopedia/entry_page.html", {
                "title": title.upper(),
                "entry": entry_send,
                "random_entry":random_page(),
            })
        else:
            return render(request, "encyclopedia/entry_page.html", {
                
                "message": ' the requested page was not found!',
                "random_entry":random_page(),
            })
        
def create_page(request):
    if request.method == "POST":
        if request.POST.get("md_text") and request.POST.get("title"):
            entry = request.POST.get("title")
            md_text = request.POST.get("md_text")
            entries = [x.lower() for x in util.list_entries()]
            if entry.lower() in entries:
                return render(request, "encyclopedia/create_page.html", {
                "title": entry,
                "md_text": md_text,
                "message": "Title already exists!",
                })
            else:
                util.save_entry(entry, md_text)
                entry_t = util.get_entry(entry)
                entry_send = markdown2.markdown(entry_t)
                return render(request, "encyclopedia/entry_page.html", {
                    "title": entry,
                    "entry": entry_send,
                    "random_entry":random_page(),
                })

            

    return render(request, "encyclopedia/create_page.html", {
        "random_entry":random_page(),
    })

def edit_page(request, title):
    
    if request.method == "POST":
        md_text = request.POST.get("md_text")
        util.save_entry(title, md_text)
        entry_t = util.get_entry(title)
        entry_send = markdown2.markdown(entry_t)
        return render(request, "encyclopedia/entry_page.html", {
            "title": title,
            "entry": entry_send,
            "random_entry":random_page(),
        })
    entry = util.get_entry(title)
    return render(request, "encyclopedia/edit_page.html", {
                "md_text": entry,
                "title": title,
                "random_entry":random_page(),
            })

def random_page():
    entries = util.list_entries()
    entry = random.choice(entries)
    return entry
    