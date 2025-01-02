from js import Response, Headers
import datetime

async def on_fetch(request):
    week_number = datetime.date.today().isocalendar()[1]
    return Response.new(week_number)
