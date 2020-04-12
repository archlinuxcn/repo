.PHONY: all
all: .SRCINFO

.SRCINFO: PKGBUILD
	makepkg --printsrcinfo > .SRCINFO
	
.PHONY: clean
clean:
	rm -f font-victor-mono-*.tar.xz
	rm -f victor-mono-*.zip
	rm -rf pkg src
