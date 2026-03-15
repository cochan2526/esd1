from django.shortcuts import redirect , render
from .models import StoryEntry
from .helper import build_story , build_context

# Create your views here.
def story_page ( request ):

    raw_temperature = request.GET.get ("temp", "").strip ()

    context = build_context ( raw_temperature )

    return ( render(request , "temp_stories/index.htm", context ) )

def save_story ( request ):

    if request.method != "POST":
        return ( redirect ("story_page") )

    raw_temperature = request.POST.get ("temp", "").strip ()

    if not raw_temperature :
        return ( redirect ("story_page") )

    tempInt = int ( raw_temperature )

    try:
        story = build_story ( tempInt )
        StoryEntry.objects.create ( temperature = tempInt , story = story )
    except ValueError :
        return ( redirect ("story_page") )

    return ( redirect (f"/?temp={raw_temperature}") )


