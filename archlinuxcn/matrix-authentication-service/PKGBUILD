# Maintainer: Kimiblock Moe

pkgname="matrix-authentication-service"
pkgver=0.18.0
pkgrel=1
pkgdesc='Authentication service for Matrix Synapse'
arch=('x86_64')
url="https://github.com/element-hq/$pkgname"
license=('AGPL-3.0-or-later')
provides=('mas-cli')
depends=()
options=(!lto)
backup=('etc/matrix-authentication-service/config.yaml')
makedepends=(
  'nodejs'
  'rust'
  'opa'
  'npm'
  'git'
)
source=(
  "$pkgname::git+$url.git#tag=v${pkgver}"
)

build() {
  cd "$pkgname"
  cd frontend
  npm ci
  npm run build
  cd ../policies
  make
  cd ..
  cargo build --release
}

function package() {
    echo '''[Unit]
Description=Matrix Authentication Service
After=network.target
RequiresMountsFor=/var/lib/private/matrix-authentication-service

[Service]
DynamicUser=yes
Environment=HOME=/var/lib/private/matrix-authentication-service
LoadCredential=config.yaml:/etc/matrix-authentication-service/config.yaml
WorkingDirectory=/usr/share/matrix-authentication-service
ExecStart=bash -c "ln -sfr ${CREDENTIALS_DIRECTORY}/* /var/tmp/ && /usr/bin/mas-cli server -c /var/tmp/config.yaml"
Restart=on-failure
PrivateTmp=disconnected
NoNewPrivileges=yes
StateDirectory=matrix-authentication-service
ProtectSystem=strict
ProtectHome=tmpfs
PrivateDevices=true
PrivateMounts=true
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectKernelLogs=true
ProtectControlGroups=true
ProtectProc=invisible
ProcSubset=pid
LockPersonality=true
RestrictRealtime=true
ProtectClock=true
MemoryDenyWriteExecute=no

SystemCallFilter=~@clock @debug @module @mount @reboot @swap @cpu-emulation @obsolete @timer @chown @setuid @privileged @resources
SystemCallErrorNumber=EPERM
PrivateTmp=disconnected
NoNewPrivileges=yes

[Install]
WantedBy=multi-user.target''' >systemd.service

    install -Dm644 systemd.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
    cd "$pkgname"
    install -vd "$pkgdir/etc/$pkgname"
    install -vd "$pkgdir/usr/share/$pkgname/frontend"

    cp -R frontend/dist "$pkgdir/usr/share/$pkgname/frontend"
    cp -R policies templates translations "$pkgdir/usr/share/$pkgname"
    install -Dm755 -t "$pkgdir/usr/bin" target/release/mas-cli
    cd "${pkgdir}/usr/share/matrix-authentication-service"
    "${pkgdir}/usr/bin/mas-cli" config generate >${pkgdir}/etc/matrix-authentication-service/config.yaml
    chmod 700 ${pkgdir}/etc/matrix-authentication-service/config.yaml
    chmod 755 "${pkgdir}/usr/share/matrix-authentication-service" -R
}

sha256sums=('3cc081781932e16b7ea31378616a3a22ab4eda4099e7a3efad594d663b65e629')
