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

### Issues

* Flag package OUT-OF-DATE by submiting new issues (please follow the template).
  * If the new release is within less than a day, please be patient and wait for up to one day; our bot is likely going to build a new one soon.
* If there is something wrong with provided packages, please submit issues of desired type.
* Please contact us via issues or email.
