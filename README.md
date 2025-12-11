Arch Linux Chinese Community Repository
====

[![Packaging consistency check](https://github.com/archlinuxcn/repo/actions/workflows/test.yml/badge.svg)](https://github.com/archlinuxcn/repo/actions/workflows/test.yml)

For detailed information in Chinese, [visit here](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/).
中文介绍[请看这里](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)。

### Usage

Add repo:

```
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```
to your /etc/pacman.conf .

For mirrors (strongly recommended for users in China), see https://github.com/archlinuxcn/mirrorlist-repo.

Import PGP Keys:

```bash
sudo pacman -Sy && sudo pacman -S archlinuxcn-keyring
```

### Soyam Kayasth
