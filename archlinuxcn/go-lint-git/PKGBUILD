pkgname=go-lint-git
pkgver=20190301.176_5614ed5
pkgrel=1
pkgdesc="golang lint"
arch=('i686' 'x86_64')
license=('GPL')
depends=(
)
makedepends=(
	'go'
	'git'
)

source=(
	"git://github.com/golang/lint.git"
)

md5sums=(
	'SKIP'
)

backup=(
)

conflicts=(
)

pkgver() {
	cd "$srcdir/lint"
	local date=$(git log -1 --format="%cd" --date=short | sed s/-//g)
	local count=$(git rev-list --count HEAD)
	local commit=$(git rev-parse --short HEAD)
	echo "$date.${count}_$commit"
}

build() {
	GOPATH=$srcdir
	GOBIN=$srcdir/bin/
	mkdir -p $srcdir/src/golang.org/x/
	ln -sf $srcdir/lint $srcdir/src/golang.org/x/lint
	cd $srcdir/src/golang.org/x/lint/golint
	go get -v
}

package() {
	find "$srcdir/bin/" -type f -executable | while read filename; do
		install -DT "$filename" "$pkgdir/usr/bin/$(basename $filename)"
	done
}
