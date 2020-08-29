all: clean build git install

clean:
	rm -r src pkg || true

geninteg:
	sed -i '/.*sums=(/,$$d' PKGBUILD
	makepkg --geninteg >> PKGBUILD

srcinfo:
	makepkg --printsrcinfo > .SRCINFO

makepkg:
	makepkg -s

build: geninteg srcinfo makepkg

git: git_add git_commit

git_add:
	git add PKGBUILD .SRCINFO

git_commit: VERSION = $(shell grep pkgver .SRCINFO | cut -d '=' -f 2 | tr -d '[:space:]')
git_commit:
	git commit -m "Update to ${VERSION}"

install:
	makepkg --install
