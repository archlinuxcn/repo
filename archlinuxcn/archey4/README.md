# Archey4-PKGBUILD

> Archey4 PKGBUILD for Arch User Repository (AUR)

## Required dependencies

```bash
# For developers
pacman -S base-devel pacman-contrib namcap

# For end-users
pacman -S python-setuptools python-distro python-netifaces
```

## Clone this repository

```bash
git clone https://aur.archlinux.org/archey4.git
cd archey4/
```

## Development procedure

```bash
# Edit PKGBUILD as needed here...
nano PKGBUILD

# Run PKGBUILD lint
namcap PKGBUILD

# Update MD5 and SHA1 sums
updpkgsums

# Let's build the package
makepkg
makepkg --printsrcinfo > .SRCINFO

# Commit changes and publish them
git add PKGBUILD .SRCINFO
git commit -m '...'
git push
```

## Installation procedure

```bash
pacman -U ./archey4-*.pkg.tar.zst

# These entry points should now be available on your system
archey
archey4
```
