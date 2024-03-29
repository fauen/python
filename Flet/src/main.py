import flet as ft
import requests as r
import datetime
from os import getenv
from dotenv import load_dotenv

load_dotenv('../.env')
api_key = getenv('api_key')

_current = r.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat=59.3251172&lon=18.0710935&appid={api_key}")

days = [
    "Mon",
    "Tue",
    "Wed",
    "Thur",
    "Fri",
    "Sat",
    "Sun"
]

def main(page: ft.Page) -> None:
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    # Animation
    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()

    def _current_temp():
        _current_temp = int(_current.json()['main']['temp'])
        _current_weather = _current.json()['weather'][0]['main']
        _current_description = _current.json()['weather'][0]['description']
        _current_wind = int(_current.json()['wind']['speed'])
        _current_humidity = int(_current.json()['main']['humidity'])
        _current_feels = int(_current.json()['main']['feels_like'])
        return [
            _current_temp,
            _current_weather,
            _current_description,
            _current_wind,
            _current_humidity,
            _current_feels
            ]

    def _current_extra():
        _extra_info = []
        
        _extra = [
            [
                int(_current.json()['visibility'] / 1000),
                "km",
                "Visibility",
                ft.icons.REMOVE_RED_EYE,
            ],
            [
                round(_current.json()['main']['pressure'] * 0.03, 2),
                "inHg",
                "Pressure",
                ft.icons.COMPRESS,
            ],
            [
                datetime.datetime.fromtimestamp(
                    _current.json()['sys']['sunset']
                ).strftime("%H:%M"),
                "",
                "Sunset",
                ft.icons.ARROW_DROP_DOWN
            ],
            [
                datetime.datetime.fromtimestamp(
                    _current.json()['sys']['sunrise']
                ).strftime("%H:%M"),
                "",
                "Sunrise",
                ft.icons.ARROW_DROP_UP,
            ],
        ]
        
        for data in _extra:
            _extra_info.append(
                ft.Container(
                    bgcolor='white10',
                    border_radius=22,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment='center',
                        horizontal_alignment='center',
                        spacing=25,
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Image(
                                    src=data[3],
                                    color='white',
                                ),
                                width=32,
                                height=32,
                            ),
                        ]
                    )
                ),
            ),

        return _extra_info

        pass

    def _top():
        _today = _current_temp()
        _today_extra = ft.GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )
        
        for info in _current_extra():
            _today_extra.controls.append(info)
        
        top = ft.Container(
            width=310,
            height=660 * 0.40,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=["lightgreen600", "lightgreen900"]
            ),
            border_radius=35,
            animate=ft.animation.Animation(duration=450, curve='decelerate'),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=ft.Column(
                alignment='start',
                spacing=10,
                controls=[
                    ft.Row(
                        alignment='center',
                        controls=[
                            ft.Text(
                                "Stockholm, Sweden",
                                size=16,
                                weight='w500'
                            )
                        ]
                    ),
                    ft.Container(padding=ft.padding.only(bottom=5)),
                    ft.Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        width=90,
                                        height=90,
                                    )
                                ]
                            ),
                            ft.Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    ft.Text(
                                        "Current",
                                        size=12,
                                        text_align='center',
                                    ),
                                    ft.Row(
                                        vertical_alignment='start',
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                content=ft.Text(
                                                    _today[0],
                                                   size=52 
                                                )
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "°",
                                                    size=28,
                                                    text_align='center',
                                                )
                                            )
                                        ]
                                    ),
                                    ft.Text(
                                        _today[1] + " - Bob",
                                        size=10,
                                        color='white54',
                                        text_align='center',
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Divider(
                        height=8,
                        thickness=1,
                        color='white10'
                    ),
                    ft.Row(
                        alignment='spaceAround',
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment='center',
                                    spacing=2,
                                    controls=[
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            content=ft.Icon(ft.icons.AIR, color='white'),
                                            width=20,
                                            height=20,
                                        ),
                                        ft.Text(
                                            str(_today[3]) + " m/s",
                                            size=11,
                                        ),
                                        ft.Text(
                                            "Wind",
                                            size=9,
                                            color='white54',
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment='center',
                                    spacing=2,
                                    controls=[
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            content=ft.Icon(ft.icons.WATER_DROP, color='white'),
                                            width=20,
                                            height=20,
                                        ),
                                        ft.Text(
                                            str(_today[4]) + "%",
                                            size=11,
                                        ),
                                        ft.Text(
                                            "Humidity",
                                            size=9,
                                            color='white54',
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment='center',
                                    spacing=2,
                                    controls=[
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            content=ft.Icon(ft.icons.THERMOSTAT, color='white'),
                                            width=20,
                                            height=20,
                                        ),
                                        ft.Text(
                                            str(_today[5]) + "°",
                                            size=11,
                                        ),
                                        ft.Text(
                                            "Feels like",
                                            size=9,
                                            color='white54',
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    _today_extra
                ],
            ),
        )

        return top

    _c = ft.Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=ft.Stack(
            width=300,
            height=550,
            controls=[_top()]
        )
    )

    page.add(_c)

if __name__ == "__main__":
    ft.app(target=main)