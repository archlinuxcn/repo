# Insomnia AUR Package

```shell
# Generate md5
makepkg -g >> PKGBUILD   # then delete old ones

# Generate new .SRCINFO
makepkg --printsrcinfo > .SRCINFO

# Test a build
makepkg
```