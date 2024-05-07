import reflex as rx
from adeviento_web.styles.styles import Size, Color


def day(number: int, text: str = "", url: str = "", finished=False) -> rx.Component:
    return rx.chakra.box(
        rx.cond(
            url != "",
            rx.chakra.link(
                rx.chakra.image(
                    src=f"calendar/{number}.png",
                    alt=text,
                    padding=Size.SMALL.value
                ),
                href=url,
                is_external=True,
                position="absolute"
            )
        ),
        rx.cond(
            url == "",
            rx.chakra.image(
                src="gift.png",
                alt=f"Regalo asociado al día {number}",
                position="absolute",
                padding=Size.SMALL.value
            )
        ),
        rx.chakra.text(
            number,
            padding=Size.DEFAULT.value,
            position="absolute"
        ),
        bg=Color.ACCENT.value if finished else Color.TERTIARY.value if url != "" else Color.SECONDARY.value,
        aspect_ratio="1",
        position="relative"
    )
