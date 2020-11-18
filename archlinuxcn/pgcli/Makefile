all:
	make srcinfo
	make build
	make clean
	make check

build:
	makepkg -f

srcinfo:
	makepkg --printsrcinfo > .SRCINFO

clean:
	rm -rf pkg/ src/

check:
	namcap *.tar.xz
