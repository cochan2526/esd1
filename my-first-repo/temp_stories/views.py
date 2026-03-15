from django.shortcuts import redirect , render
from .models import StoryEntry

stories = None

# Create your views here.
def story_page ( request ):

    raw_temperature = request .GET.get ("temp", "").strip ()
    story = None
    error = None

    if raw_temperature :
        try :
            story = build_story ( int( raw_temperature ) )
        except ValueError :
            error = "Error ! Please enter a whole number temperature!"

    context = {
    "temp" : raw_temperature ,
    "error" : error ,
    "story" : story ,
    "stories" : stories ,
    }
    return render(request , "temp_stories/index.htm", context )

def build_story ( temperature ) :

    tempstr = str ( temperature )

    if temperature > 99 :
        story = "The temperature is " + tempstr + " , welcome to the hell."
    elif temperature > 30 :
        story = "The temperature is " + tempstr + " , what a hot day."
    elif temperature > 12 :
        story = "The temperature is " + tempstr + " , what a warm day."
    elif temperature > 0 :
        story = "The temperature is " + tempstr + " , what a cold day."
    else :
        story = "The temperature is " + tempstr + " , better stay at home and turn on the hearting."

    return ( story )

def save_story ( request ):

    if request .method != "POST":
        return redirect ("story_page")

    raw_temperature = request.POST.get ("temp", "").strip ()
    tempInt = int ( raw_temperature )

    if not raw_temperature :
        return redirect ("story_page")

    try:
        story = build_story ( tempInt )
        stories = StoryEntry ( tempInt , build_story( tempInt ) )

    except ValueError :
        return redirect ("story_page")

    return ( redirect (f"/?temp={raw_temperature}") )


