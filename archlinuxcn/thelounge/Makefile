.SUFFIXES: # empty the defaults

DEFAULT: .SRCINFO

.SRCINFO: PKGBUILD
	makepkg --printsrcinfo > $@

PKGBUILD: updpkgsums

.PHONY: updpkgsums
updpkgsums: cleanslate
	updpkgsums

.PHONY: cleanslate
cleanslate:
	git clean -fdx # else makepkg uses stale files for checksums
