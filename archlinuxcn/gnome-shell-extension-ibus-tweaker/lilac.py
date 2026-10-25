def _major(ver):
    return (ver or '').split('.', 1)[0]


def prepare():
    arch = _major(_G.newvers[1] if len(_G.newvers) > 1 else None)
    upstream = _major(_G.newver)
    if arch.isdigit() and upstream.isdigit() and arch != upstream:
        return (f'ibus-tweaker {_G.newver} targets GNOME Shell {upstream}, '
                f'Arch ships {_G.newvers[1]}')
