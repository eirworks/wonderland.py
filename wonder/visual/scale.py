def star_scale(value: float, stars: int = 5) -> str:
    render_stars = int(stars * value)
    return "[{}]".format(("*" * render_stars).ljust(stars, "-"))
