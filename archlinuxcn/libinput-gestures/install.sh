_pkgname=libinput-gestures

post_install() {
	echo -ne "\e[34;1m"
	echo "=== INSTALLATION NOTES for $_pkgname ==="
	echo -ne "\e[39;1m"
	echo "A user must be a member of the input group, i.e. run:"
	echo "   sudo gpasswd -a \$USER input"
	echo "A user can start $_pkgname from their DE, or run:"
	echo "   $_pkgname-setup start"
	echo "A user can enable auto start of $_pkgname, i.e. run:"
	echo "   $_pkgname-setup autostart"
	echo "Configuration files are at:"
	echo "   /etc/$_pkgname.conf (system wide default)"
	echo "   \$HOME/.config/$_pkgname.conf (optional per user)"
	echo -ne "\e[0m"
}

post_upgrade() {
	echo -ne "\e[34;1m"
	echo "=== UPGRADE NOTES for $_pkgname ==="
	echo -ne "\e[39;1m"
	echo "A user should restart $_pkgname, i.e. run:"
	echo "   $_pkgname-setup restart"
	echo -ne "\e[0m"
}
