import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


_gifts = [
    (
        "(x5) Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1730953182199603618?s=20",
        "https://mouredev.link/libro-git"
    ),
    (
        "(x2) Aprende Python en un fin de semana",
        "https://x.com/MoureDev/status/1731319751589101977?s=20",
        "https://amzn.to/46F3AFg"
    ),
    (
        "(x2) Cursos de Programación en SQL",
        "https://x.com/MoureDev/status/1731674979014479924?s=20",
        "https://www.udemy.com/course/el-mejor-curso-de-sql"
    ),
    (
        "(x1) El programador pragmático",
        "https://x.com/MoureDev/status/1732038845741637724?s=20",
        "https://amzn.to/3t4lBiw"
    ),
    (
        "(x2) Patrones de diseño",
        "https://x.com/MoureDev/status/1732401556304368096?s=20",
        "https://refactoring.guru/es/design-patterns/book"
    ),
    (
        "(x2) Jetpack Compose desde 0",
        "https://x.com/MoureDev/status/1732761306120192472?s=20",
        "https://www.appcademy.dev/jetpack-compose-curso-definitivo-desde-0-2023"
    ),
    (
        "(x2) Aprendiendo JavaScript",
        "https://x.com/MoureDev/status/1733124831049064821?s=20",
        "https://carlosazaustre.es/libros/aprendiendo-javascript"
    ),
    (
        "(x1) Cracking the Coding Interview",
        "https://x.com/MoureDev/status/1733493029187506208?s=20",
        "https://amzn.to/3TbQQCT"
    ),
    (
        "(x2) Aprende SQL en un fin de semana",
        "https://x.com/MoureDev/status/1733853435106062754?s=20",
        "https://amzn.to/4abT0Iy"
    ),
    (
        "(x2) Aprende HTML desde cero",
        "https://x.com/MoureDev/status/1734220123332866337?s=20",
        "https://amzn.to/46Q1N03"
    ),
    (
        "(x2) Suscripciones de 1 mes a Hack4u",
        "https://x.com/MoureDev/status/1734581711399211052?s=20",
        "https://hack4u.io"
    ),
    (
        "(x1) Máster en Desarrollo de Apps y Programación Web",
        "https://x.com/MoureDev/status/1734936513350177167?s=20",
        "https://immune.institute/programas/master-en-desarrollo-de-apps-y-programacion-web"
    ),
    (
        "(x1) Clean JavaScript",
        "https://x.com/MoureDev/status/1735300234601812256?s=20",
        "https://amzn.to/3NkDlwX"
    ),
    (
        "(x1) Hosting anual + dominio",
        "https://x.com/MoureDev/status/1735660556357415400?s=20",
        "https://mouredev.link/raiola"
    ),
    (
        "(x1) Diseño Ágil con TDD con Python",
        "https://x.com/MoureDev/status/1736035091720098207?s=20",
        "https://savvily.es/libros/diseno-agil-con-tdd/"
    ),
    (
        "(x2) El Último Programador: La lucha contra la IA",
        "https://x.com/MoureDev/status/1736388829488066830?s=20",
        "https://amzn.to/3RroYYR"
    ),
    (
        "(x2) Ultimate Docker",
        "https://x.com/MoureDev/status/1736749139671552229?s=20",
        "https://academia.holamundo.io/courses/ultimate-docker"
    ),
    (
        "(x1) Código sostenible",
        "https://x.com/MoureDev/status/1737112235192078817?s=20",
        "https://savvily.es/libros/codigo-sostenible/"
    ),
    (
        "(x2) Flutter Móvil: De cero a experto",
        "https://x.com/MoureDev/status/1737475599076061500?s=20",
        "https://fernando-herrera.com/course/flutter-cero-experto"
    ),
    (
        "(x1) Elgato Stream Deck + (x2) SD Mobile",
        "https://x.com/MoureDev/status/1737836327562010744?s=20",
        "https://www.elgato.com/es/es/p/stream-deck-plus-black"
    ),
    (
        "(x2) Aprendiendo React",
        "https://x.com/MoureDev/status/1738199777320259618?s=20",
        "https://amzn.to/3toE0Xr"
    ),
    (
        "(x1) La artesanía del código limpio",
        "https://x.com/MoureDev/status/1738562772558905396?s=20",
        "https://amzn.to/3tlN3IK"
    ),
    (
        "(x1) Curso intensivo de Python (Edición 2024)",
        "https://x.com/MoureDev/status/1738932601774059528?s=20",
        "https://amzn.to/4azB6Q6"
    ),
    (
        "(x5) Git y GitHub desde cero: Guía de estudio teórico-práctica paso a paso más curso en vídeo",
        "https://x.com/MoureDev/status/1739289550294266340?s=20",
        "https://mouredev.link/libro-git"
    )
]

_current_day = len(_gifts) - 1


def calendar() -> rx.Component:
    return rx.chakra.vstack(
        header_text(
            "heart",
            "Calendario 2023 (finalizado). ¡Muchas gracias por participar!"
        ),
        # rx.chakra.vstack(
        #     rx.chakra.text(
        #         "El regalo de hoy",
        #         class_name="title",
        #         color=TextColor.ACCENT.value
        #     ),
        #     rx.chakra.flex(
        #         rx.chakra.box(
        #             day(
        #                 _current_day + 1,
        #                 _gift_name(_current_day),
        #                 _gift_url(_current_day),
        #             ),
        #             height="14em",
        #             width="14em",
        #             aspect_ratio="1",
        #             margin_right=Size.BIG.value
        #         ),
        #         rx.chakra.vstack(
        #             rx.chakra.span(
        #                 f"Día {_current_day + 1}"),
        #             rx.chakra.link(
        #                 _gift_name(_current_day),
        #                 href=_gift_info(_current_day),
        #                 is_external=True
        #             ),
        #             rx.chakra.spacer(),
        #             rx.chakra.flex(
        #                 button(
        #                     "Participa",
        #                     _gift_url(_current_day)
        #                 ),
        #                 button(
        #                     f"Día {_current_day}",
        #                     _gift_url(_current_day - 1)
        #                 ),
        #                 align_items="start",
        #                 direction=styles.FLEX_DIRECTION
        #             ),
        #             align_items="start",
        #             margin_top=Size.BIG.value
        #         ),
        #         direction=styles.FLEX_DIRECTION
        #     ),
        #     width="100%",
        #     class_name="nes-container is-dark with-title",
        #     align_items="start"
        # ),
        rx.chakra.responsive_grid(
            *[
                day(
                    number + 1,
                    _gift_name(number),
                    _gift_url(number),
                    True,  # finalizado
                    # False if len(_gifts) - 1 == number else True),
                )
                for _, number in enumerate(range(0, _current_day + 1))
            ],
            # *[
            #     day(number)
            #     for _, number in enumerate(range(_current_day + 2, 25))
            # ]
            columns=[3, 3, 4, 5, 6],
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_y=Size.BIG.value
        ),
        rx.chakra.vstack(
            rx.chakra.hstack(
                rx.chakra.text(
                    # "Próximo regalo y ganadores en",
                    "Calendario 2024 en",
                    margin_right=Size.DEFAULT.value
                ),
                rx.chakra.text(
                    id="countdown",
                    margin_left=Size.ZERO.value
                ),
                align_items="start",
                flex_direction=styles.FLEX_DIRECTION
            ),
            # button(
            #     "Recordar",
            #     constants.DISCORD_EVENT_URL
            # ),
            rx.chakra.span(
                "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
            ),
            rx.chakra.span(
                "• Puedes seleccionar cada regalo para conocer a los ganadores una vez se haya publicado el nuevo sorteo (aparecerá en rojo)."
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%"
        ),
        rx.script(src="/js/countdown.js"),
        style=styles.max_width_style
    )


def _gift_name(gift) -> str:
    gift_index = gift
    if len(_gifts) > gift_index:
        return _gifts[gift_index][0]
    return ""


def _gift_url(gift) -> str:
    gift_index = gift
    if len(_gifts) > gift_index:
        return _gifts[gift_index][1]
    return ""


def _gift_info(gift) -> str:
    gift_index = gift
    if len(_gifts) > gift_index:
        return _gifts[gift_index][2]
    return ""
