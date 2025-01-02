from js import Response, Headers
import datetime

async def on_fetch(request):
    html_content = ""

    html_style = "html, body {background-color: #000000; overflow: hidden;} .flex-container {height: 100%; width: 100%; display: flex; position: fixed; align-items: center; justify-content: center;} .flex-container > div {color: #00FF00; font-size: 200px;}"

    week_number = datetime.date.today().isocalendar()[1]
    #return Response.new(week_number)

    html_content += f"{week_number}"

    html = f"""
    <!DOCTYPE html>
        <head>
            <title>Week number</title>
            <style>{html_style}</style>
        </head>
        <body>
            <div class="flex-container">
                <div>
                    {html_content}
                </div>
            </div>
        </body>
    """

    headers = Headers.new({"content-type": "text/html;charset=UTF-8"}.items())
    return Response.new(html, headers=headers)
