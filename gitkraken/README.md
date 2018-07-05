# Update package

* Update package version in PKGBUILD
* Generate new checksums with

```$ updpkgsums```

* Test install

```$ makepkg -si```

* Update .SRCINFO 

```$ makepkg --printsrcinfo > .SRCINFO```
