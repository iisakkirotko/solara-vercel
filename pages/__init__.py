import solara


@solara.component
def Page():
    with solara.Card():
        solara.Markdown("Hello, world!")