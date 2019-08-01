Arch Linux Chinese Community Repository
====

Packaging consistency check: [![Build Status](https://travis-ci.org/archlinuxcn/repo.svg?branch=master)](https://travis-ci.org/archlinuxcn/repo)

### Usage

Add repo:

```
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```
to your /etc/pacman.conf .

For mirrors (mainly in China), see https://github.com/archlinuxcn/mirrorlist-repo.

Import PGP Keys:

```bash
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
```

### PKGLIST

* Flag package OUT-OF-DATE by submiting new issue, and shall be closed after package updated.
  * If the new release is within less than a day, and you can see a file named `lilac.py` alongside the PKGBUILD for the package here, please be patient and wait for up to one day.

* Please contact us via emails or issues.
