# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=nomad
pkgver=0.9.3
pkgrel=1
pkgdesc="A Distributed, Highly Available, Datacenter-Aware Scheduler"
arch=('i686' 'x86_64')
url="https://www.nomadproject.io/"
license=('MPL')
depends=('ethtool' 'lxc')
makedepends=('go' 'git')
optdepends=(
	'docker'
	'rkt'
	'java-runtime-headless'
)
backup=(etc/nomad/{server,client}.conf)
source=(https://github.com/hashicorp/nomad/archive/v$pkgver/$pkgname-$pkgver.tar.gz
        nomad-{server,client}.{service,conf})
sha256sums=('65ae3d7c7c88f9a344f88c2444356662eaa16683d0033bf9fbff691633f4e6fe'
            '52b0a22c3c0c72c642a8728cb48bd8797f4f6a12990e11bbb2342edcc2a9a206'
            'da475bc4aa3b1493eb62f09e7f99dcc171e8ce6d74df3da30514cfdfe72a5714'
            '4c8fb7c18c67ca20e3ee07f25cf2f0c82b66c4c173275ae8d643c91cce3c0ceb'
            'ba80943ac42e617627c7e14be402078199ddba8d7e4276d67f0c9f6e6842d4a8')

prepare() {
	mkdir -p src/github.com/hashicorp
	cd src/github.com/hashicorp
	rm -rf nomad
	mv ../../../$pkgname-$pkgver nomad
	cd nomad

	export GOPATH="$srcdir"
	export PATH="$GOPATH/bin:$PATH"

	if [ $CARCH == "x86_64" ]; then
		export GOARCH=amd64
	else
		export GOARCH=386
	fi

	go get golang.org/x/sys/cpu

	make deps lint-deps
	mkdir -p bin
}

build() {
	cd src/github.com/hashicorp/nomad
	export GOPATH="$srcdir"
	export PATH="$GOPATH/bin:$PATH"

	if [ $CARCH == "x86_64" ]; then
		export GOARCH=amd64
	else
		export GOARCH=386
	fi

	CGO_ENABLED=1 \
		go build -ldflags '-X main.GitCommit=""' \
		         -tags "ui lxc" \
		         -o bin/nomad
}

package() {
	for type in server client; do
		install -Dm644 nomad-$type.service \
			"$pkgdir"/usr/lib/systemd/system/nomad-$type.service
		install -Dm644 nomad-$type.conf "$pkgdir"/etc/nomad/$type.conf
	done

	cd src/github.com/hashicorp/nomad
	install -Dm755 bin/nomad "$pkgdir"/usr/bin/nomad
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
