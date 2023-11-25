from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    entry = util.get_entry(title.capitalize())
    if entry != None:
        entry_send = markdown2.markdown(entry)
        print(entry_send)
        return render(request, "encyclopedia/entry_page.html", {
            "title": title.capitalize(),
            "entry": entry_send
        })
    else:
        entry = util.get_entry(title.upper())
        if entry != None:
            entry_send = markdown2.markdown(entry)
            return render(request, "encyclopedia/entry_page.html", {
                "title": title.upper(),
                "entry": entry_send
            })
        else:
            return render(request, "encyclopedia/entry_page.html", {
                
                "entry": ' the requested page was not found'
            })


