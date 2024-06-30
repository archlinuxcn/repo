.PHONY: pkg src

src: PKGBUILD
	makepkg --printsrcinfo > .SRCINFO

pkg:
	makepkg -Asc
