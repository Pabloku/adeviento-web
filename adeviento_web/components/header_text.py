import reflex as rx
from adeviento_web.styles.styles import Size, TextColor


def header_text(icon: str, text: str, dark=True) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.box(
            class_name=f"nes-icon is-medium {icon}"
        ),
        rx.chakra.heading(
            text,
            size="md",
            color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value
        ),
        spacing=Size.DEFAULT.value,
        padding_bottom=Size.BUTTON.value
    )
