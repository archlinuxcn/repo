all: prepare PKGBUILD .SRCINFO
	makepkg -C -c -f -r
	rm -rf *.jar *.tar.gz

prepare:
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO
