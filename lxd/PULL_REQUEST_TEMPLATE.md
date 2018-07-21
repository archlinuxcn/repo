


## Checklist:

Please ensure you've done the below when submitting a pull request:

- [ ] Run `updpkgsums` to ensure checksums are up to date.
- [ ] Make and install changes locally.
- [ ] Bump `_pkgrel` if change is not an upstream update.
- [ ] Reset `_pkgrel` to 1 if `_pkgver` has changed.
- [ ] Run `mksrcinfo` to update AUR info file (do this last).
