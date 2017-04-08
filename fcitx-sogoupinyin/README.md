# Fcitx sogoupinyin

[Sogoupinyin](http://pinyin.sogou.com/linux/) for Arch Linux.

## Installation

```
yaourt -S fcitx-sogoupinyin
```

Don't forget to add this input method in Fcitx configurations.

## Configuration

It should work out of the box.

In case it doesn't work in Gnome 3, add the following to `~/.xprofile`:

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"

gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/IMModule':<'fcitx'>}"
```

## Troubleshooting

### Not work

Try executing `rm -rf ~/.config/SogouPY*` and restart.

## Known issues

* Not work in [sublime-text-dev](https://aur.archlinux.org/packages/sublime-text-dev). Use [sublime-text-dev-imfix2](https://aur.archlinux.org/packages/sublime-text-dev-imfix2/) instead.
