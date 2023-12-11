# Arch Linux CN Community Repository

[![Packaging consistency check](https://github.com/archlinuxcn/repo/actions/workflows/test.yml/badge.svg)](https://github.com/archlinuxcn/repo/actions/workflows/test.yml)

For detailed information in Chinese, [please visit here](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/).
中文介绍[请看这里](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)。

## Usage

To use this repository, please append the following lines to /etc/pacman.conf:

```ini
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```

For mirrors (strongly recommended for users in China), [please visit here](https://github.com/archlinuxcn/mirrorlist-repo).

To import PGP keys, run the following command as a superuser:

```bash
pacman -Sy && pacman -S archlinuxcn-keyring
```

## Issues

* If you find any package that is OUT-OF-DATE, please report it by creating a new issue (following the template provided).
  * If the new release is within less than a day, please be patient and wait for up to one day; our bot will likely build a new one soon.
* If there is something wrong with the provided packages, please submit an issue of the appropriate type.
* Please contact us via issues or email if you have any questions or suggestions.
