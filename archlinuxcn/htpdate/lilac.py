#!/usr/bin/env python3

from lilaclib import *

htpdate_default = ("# This file is used to configure htpdate daemon. Most users needn't change" + '\n'
        "# anything here." + '\n'
        '\n'
        "# htpdate will run on system boot as daemon and at every network restart" + '\n'
        "# (IF UP). However you can disable each one uncommenting the following lines." + '\n'
        "# But IF YOUR SYSTEM ARE USING SYSTEMD (Debian Jessie and newer use it!)," + '\n'
        "# the first line will be ignored. You can use '# systemctl disable htpdate'" + '\n'
        "# to disable htpdate on boot and '# systemctl enable htpdate' to reenable it." + '\n'
        '# HTP_DAEMON=no' + '\n'
        '# HTP_IFUP=no' + '\n'
        '\n'
        "# If you have a HTTP proxy, uncomment the following line and change the" + '\n'
        "# values." + '\n'
        '# HTP_PROXY="-P myproxy-xyz.com:8080"' + '\n'
        '\n'
        "# In the next line you should put HTTP servers. Note that htpdate uses" + '\n'
        "# the timestamps extracted from headers to synchronize the time. You" + '\n'
        "# must to use reliable servers only. Remember: you can use any site, not" + '\n'
        "# specifics NTP site only." + '\n'
        'HTP_SERVERS="www.kernel.org www.ntp.org www.wikipedia.org"' + '\n'
        '\n'
        "# The general options can be viewed with '$ htpdate -h'. However, you can" + '\n'
        "# keep the current options, that works fine." + '\n'
        'HTP_OPTIONS="-D -s"')

def pre_build():
    aur_pre_build()
    run_cmd(['sh', '-c', 'sed \'/^$/d\' -i htpdate.service'])
    for line in edit_file('htpdate.service'):
        if line.startswith('Description='):
            line = ('Description=HTTP based time synchronization tool' + '\n'
                    'Documentation=man:htpdate' + '\n'
                    'After=network.target nss-lookup.target')
        elif line.endswith('[Service]'):
            line = '\n' + line
        elif line.startswith('PIDFile='):
            line = line + '\n' + 'EnvironmentFile=/etc/default/htpdate'
        elif line.startswith('ExecStart='):
            line = ('ExecStart=/usr/bin/htpdate ${HTP_OPTIONS} ${HTP_PROXY}'
                    ' '
                    '-i /run/htpdate.pid ${HTP_SERVERS}' + '\n'
                    'ExecReload=/bin/kill -HUP ${MAINPID}' + '\n'
                    '# Security' + '\n'
                    'InaccessibleDirectories='
                    '/boot /home /media /mnt /root /opt /srv' + '\n'
                    'PrivateTmp=yes' + '\n'
                    'ReadOnlyDirectories=/etc /usr /var' + '\n'
                    'ReadWriteDirectories=/var/run')
        elif line.endswith('[Install]'):
            line = '\n' + line
        print(line)

    # Write the contents of the htpdate_default variable
    # to the htpdate.default file

    with open('htpdate.default', 'w') as htpdate_default_file:
        print(htpdate_default, file = htpdate_default_file)

    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgdesc='):
            line = 'pkgdesc="HTTP based time synchronization tool"'
        elif line.startswith('source='):
            line = (line + '\n' + '        '
                    '"htpdate.default"')
        elif line.startswith('md5sums='):
            line = 'sha256sums=('
        elif line.startswith('package()'):
            line = (line + '\n' + '  '
                    'install -D -m 644 htpdate.default'
                    ' '
                    '${pkgdir}/etc/default/htpdate')
        print(line)
    run_cmd(['updpkgsums'])
