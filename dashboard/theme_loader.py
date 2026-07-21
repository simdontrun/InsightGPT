import os

def load_css(theme: str) -> str:
    base = os.path.dirname(__file__)
    files = [
        os.path.join(base, "styles", f"{theme}.css"),
        os.path.join(base, "styles", "sidebar.css"),
    ]
    combined = ""
    for path in files:
        try:
            with open(path) as f:
                combined += f.read() + "\n"
        except FileNotFoundError:
            pass
    return f"<style>{combined}</style>"
