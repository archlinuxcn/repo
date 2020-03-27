# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=nomad
pkgver=0.10.5
pkgrel=2
pkgdesc="A Distributed, Highly Available, Datacenter-Aware Scheduler"
arch=('x86_64' 'aarch64' 'armv7h' 'armv7l')
url="https://nomadproject.io/"
license=('MPL2')
#depends=('ethtool' 'lxc')
makedepends=('go' 'git')
optdepends=('docker: enables docker driver'
            'java-runtime: enables java driver'
            'qemu-headless: enables qemu driver'
            'rkt: enables rkt driver')
backup=(etc/nomad/{server,client}.conf)
source=(https://github.com/hashicorp/nomad/archive/v$pkgver/$pkgname-$pkgver.tar.gz
        nomad-{server,client}.{service,conf})
sha256sums=('ba23bcbc29138be9a2033531114e447f92a2e57a0f0a7bea84734845c8b89eaf'
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

	go get golang.org/x/sys/cpu

	make deps lint-deps
	mkdir -p bin
}

build() {
	cd src/github.com/hashicorp/nomad
	export GOPATH="$srcdir"
	export PATH="$GOPATH/bin:$PATH"

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
