nam = $(shell sed -n 's/^pkgname=//p' PKGBUILD)
src = PKGBUILD
inf = .SRCINFO
pkg = $(shell ls -v $(nam)*.pkg.tar* 2>/dev/null | tail -1)

all: sum $(inf) check

$(inf): $(src)
	makepkg --printsrcinfo >$@

check: $(src)
	namcap $^
ifneq ($(strip $(pkg)),)
	namcap $(pkg)
endif

sum: $(src)
	updpkgsums

clean:
	rm -rf $(inf) $(nam)-* *.tar.xz *.tar.gz pkg/ src/ *.part

# vim: se ts=4:
