# fcitx-sogoupinyin

AUR package of [sogoupinyin for Linux](http://pinyin.sogou.com/linux/).

## Installation

This package is available on both [AUR](https://aur.archlinux.org/packages/fcitx-sogoupinyin/) and [archlinuxcn repository](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/).

```bash
# Use yay or any other AUR helpers to install from AUR
yay -S fcitx-sogoupinyin
```

Don't forget to add this input method in Fcitx configuration.

## Configuration

No configuration is needed.

For fcitx's configuation, refer to [Fcitx#Configuration](https://wiki.archlinux.org/index.php/Fcitx#Configuration) on ArchWiki.

## Troubleshooting

### Unable to start

__Make sure fcitx is running before start `sogou-qimpanel`.__

Try one of the following methods:

* Delete sogou lock files: `rm -rf ~/.sogouinput/`
* Relogin the desktop environment
* Delete all sogou related files: `rm -rf ~/.sogouinput/ ~/.config/SogouPY*`

### Not working

It's probably caused by fcitx not working. See [Fcitx#Troubleshooting](https://wiki.archlinux.org/index.php/Fcitx#Troubleshooting) on ArchWiki.
