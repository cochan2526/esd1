from .models import StoryEntry

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

def build_context ( raw_temperature ) :

    context = None
    story = None
    error = None
    stories = StoryEntry.objects.order_by ( "temperature"  )

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

    return ( context )


