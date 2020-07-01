PKG=pkg/p7zip-natspec
PKGINFO=$(PKG)/.PKGINFO
CI_IMAGE=buzztaiki/pkgbuild-p7zip-natspec-buildenv

.PHONY: all clean test check_upstream _test lint ci_test

all: $(PKGINFO) test .SRCINFO

.SRCINFO: PKGBUILD
	makepkg --printsrcinfo > .SRCINFO

$(PKGINFO): PKGBUILD
	makepkg -f

testfiles/:
	git archive --prefix $@ origin/testfiles | tar xf -

clean:
	rm -rf testfiles src pkg *.pkg.tar.*

check_upstream:
	./check_upstream

test: $(PKGINFO) testfiles/
	$(MAKE) -s _test LANG=ja_JP.UTF-8 TESTFILE=testfiles/SHIFT_JIS.zip PATTERN="解凍すると文字化けするかも.txt"
	$(MAKE) -s _test LANG=ja_JP.UTF-8 TESTFILE=testfiles/UTF8.zip PATTERN="UTF-8固有文字列_( ◕‿‿◕ ).txt"

_test: 
	$(PKG)/usr/lib/p7zip/7z l $(TESTFILE) | grep -qe "$(PATTERN)" && echo ok

lint:
	namcap PKGBUILD

ci_test:
	git fetch --depth=1 origin testfiles:remotes/origin/testfiles
	docker pull $(CI_IMAGE)
	docker run --rm -it -u travis -v $(CURDIR):/mnt $(CI_IMAGE) make lint test
