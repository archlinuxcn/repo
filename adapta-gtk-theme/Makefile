
.SRCINFO: PKGBUILD
	mksrcinfo

package: PKGBUILD .SRCINFO
	updpkgsums
	makepkg --syncdeps --rmdeps --force --clean --noconfirm

all: package

clean:
	rm -Rfv *.jpg .SRCINFO *.tar.gz *.tar.xz *.part src/ pkg/ 2> /dev/null || true
