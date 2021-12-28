
# This will update the checksums and build the package
all: updateinfo
	makepkg -sr

# This will do the same as all, but will install it to the local system as well
install: updateinfo
	makepkg -sri

# This will update the checksums and .SRCINFO
updateinfo:
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO

# This will update PKGBUILD with the latest version and build the package
update:
	sed 's/^pkgver=.*$$/pkgver=$(shell $(MAKE) versions | tail -n 1)/' -i PKGBUILD
	sed 's/^pkgrel=.*$$/pkgrel=1/' -i PKGBUILD
	$(MAKE)

# This will list the versions available in the Ubuntu repository
versions:
	curl -s https://www.typora.io/linux/Packages | grep Version | cut -f 2 -d ' ' | sort -V | cut -f 1 -d '-' | uniq

# This will remove the files downloaded and created in the build process
clean:
	rm -rf pkg src typora_*.deb typora-*.pkg.*

publish:
	git add .
	git commit -m "Update to version $(shell $(MAKE) versions | tail -n 1)"
#	git push
