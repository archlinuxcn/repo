# Fcitx sogoupinyin

[Sogoupinyin](http://pinyin.sogou.com/linux/) for Arch Linux.

## Installation

```
yaourt -S fcitx-sogoupinyin
```

## Configuration

Gnome:

```
# ~/.xprofile
gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/IMModule':<'fcitx'>}"
```

## Known issues

* Not work in [sublime-text-dev](https://aur.archlinux.org/packages/sublime-text-dev). Use [sublime-text-dev-imfix2](https://aur.archlinux.org/packages/sublime-text-dev-imfix2/) instead.
