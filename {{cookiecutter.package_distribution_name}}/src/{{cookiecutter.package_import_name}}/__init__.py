"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    """Return a greeting, using world for a blank name."""
    recipient = name.strip() or "world"
    return f"Hello, {recipient}!"
