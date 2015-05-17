Arch Linux Chinese Community Repository
====

###Usage

Add repo

```
[archlinuxcn]
SigLevel = Optional TrustedOnly
Server = http://repo.archlinuxcn.org/$arch
```
to your /etc/pacman.conf .

For mirrors (mainly in China), see https://github.com/archlinuxcn/mirrorlist-repo.

Add PGP Keys

```bash
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
```

###PKGLIST

* Flag package OUT-OF-DATE by submit new issue, and shall be closed after package updated.

* Please contact us via Email or submitting new issues.
