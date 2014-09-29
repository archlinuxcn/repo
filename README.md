Arch Linux Chinese Community Repository
====

###Usage

Add repo

```
[archlinuxcn]
SigLevel = Optional TrustAll
Server = http://repo.archlinuxcn.org/$arch
```
to your /etc/pacman.conf .

For mirrors (mainly in China), see https://github.com/archlinuxcn/mirrorlist-repo.

Add PGP Keys

```bash
for key in 47CD9E46 95FF0792 A403F63E; do
  sudo pacman-key -r $key
  sudo pacman-key --lsign-key $key
done
```

###PKGLIST

* Flag package OUT-OF-DATE by submit new issue, and shall be closed after package updated.

* Please contact us via Email or submitting new issues.
