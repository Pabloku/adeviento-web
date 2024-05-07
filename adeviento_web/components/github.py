import reflex as rx
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size


def github() -> rx.Component:
    return rx.chakra.link(

        rx.chakra.vstack(
            rx.chakra.vstack(
                rx.chakra.span(
                    "Proyecto"
                ),
                rx.chakra.span(
                    "en GitHub"
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value
            ),
            rx.chakra.box(
                rx.chakra.span(
                    constants.VERSION,
                    class_name="is-error"
                ),
                class_name="nes-badge"
            )
        ),
        rx.chakra.box(
            class_name="nes-octocat animate"
        ),
        href=constants.GITHUB_REPO_URL,
        is_external=True,
        align_items="end",
        display="flex",
        margin_top=Size.ZERO.value
    )
