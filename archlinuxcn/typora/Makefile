
# This will update the checksums and build the package
all:
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO
	makepkg -sr

# This will do the same as all, but will install it to the local system as well
install:
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO
	makepkg -sri

# This will update PKGBUILD with the latest version and build the package
update:
	sed 's/^pkgver=.*$$/pkgver=$(shell $(MAKE) versions | tail -n 1)/' -i PKGBUILD
	$(MAKE)

# This will list the versions available in the Ubuntu repository
versions:
	curl -s https://www.typora.io/linux/Packages | perl -n -e '/^Version: (.*)-[0-9]+$$/ && print "$$1\n"' | sort -V | uniq

# This will remove the files downloaded and created in the build process
clean:
	rm -rf pkg src typora_*.deb typora-*.pkg.tar

publish:
	git add .
	git commit -m "Update to version $(shell $(MAKE) versions | tail -n 1)"
	git push
	git push aur master
