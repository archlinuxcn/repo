[sway-im](https://aur.archlinux.org/packages/sway-im/)
========
The [sway](https://swaywm.org/) package with [input method keyboard
grab](https://github.com/swaywm/sway/pull/4932) support for Arch Linux.

You can download sway-im from AUR:
```bash
paru -S sway-im
```

And you can install the pre-build package too:
```bash
# You only need to do it once
sudo pacman-key -r 0F85F46EE242057F
sudo pacman-key --lsign-key 0F85F46EE242057F

# Install
sudo pacman -U https://i.hyeon.me/PKGBUILD/sway-im-1:1.5.1.r2.ec36e113-1-x86_64.pkg.tar.zst
```

#### References
- https://github.com/swaywm/sway/pull/4932
- https://github.com/Riey/kime/pull/129#issuecomment-767000048
