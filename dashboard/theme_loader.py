def load_css(theme):

    if theme == "dark":
        css_file = "dashboard/styles/dark.css"
    else:
        css_file = "dashboard/styles/light.css"

    with open(css_file) as f:
        return f"<style>{f.read()}</style>"