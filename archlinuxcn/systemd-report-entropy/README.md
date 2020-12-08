# systemd-report-entropy
report system entropy to journald during boot

## Why ?
Because it is hard to check available entropy during system boot,
and lack of entropy can cause delay in system boot process.

## How ?
Just start a systemd service early enough to report available entropy
to the journal, until systemd finished its booting.

## Ok, how to use it

1. Build and install the package 
```bash
makepkg -si
```

2. Enable the service
```bash
sudo systemctl enable systemd-report-entropy.service
```

3. reboot

4. check entropy report
```bash
journalctl -b0 -u systemd-report-entropy.service
```

## Example output:

```
-- Journal begins at Mon 2020-11-30 11:05:02 JST, ends at Mon 2020-12-07 11:32:10 JST. --
12月 07 11:30:31 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:31,703999577+09:00 ENTROPY 2273 sleeping 227.30000000000000000000 ms
12月 07 11:30:32 imacssd systemd-report-entropy[317]: is-system-running: initializing
12月 07 11:30:32 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:32,028432113+09:00 ENTROPY 2278 sleeping 227.80000000000000000000 ms
12月 07 11:30:32 imacssd systemd-report-entropy[317]: is-system-running: initializing
12月 07 11:30:32 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:32,275582469+09:00 ENTROPY 2281 sleeping 228.10000000000000000000 ms
12月 07 11:30:32 imacssd systemd-report-entropy[317]: is-system-running: initializing
12月 07 11:30:32 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:32,530915564+09:00 ENTROPY 2296 sleeping 229.60000000000000000000 ms
12月 07 11:30:32 imacssd systemd-report-entropy[317]: is-system-running: initializing
12月 07 11:30:32 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:32,776745567+09:00 ENTROPY 2306 sleeping 230.60000000000000000000 ms
12月 07 11:30:33 imacssd systemd-report-entropy[317]: is-system-running: initializing
12月 07 11:30:33 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:33,019687024+09:00 ENTROPY 2308 sleeping 230.80000000000000000000 ms
12月 07 11:30:33 imacssd systemd-report-entropy[317]: is-system-running: starting
12月 07 11:30:33 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:33,262886342+09:00 ENTROPY 2310 sleeping 231.00000000000000000000 ms
12月 07 11:30:33 imacssd systemd-report-entropy[317]: is-system-running: starting
12月 07 11:30:33 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:33,506260356+09:00 ENTROPY 2313 sleeping 231.30000000000000000000 ms
12月 07 11:30:33 imacssd systemd-report-entropy[317]: is-system-running: starting
12月 07 11:30:33 imacssd systemd-report-entropy[317]: At 2020-12-07T11:30:33,749220139+09:00 ENTROPY 2313 sleeping 231.30000000000000000000 ms
12月 07 11:30:33 imacssd systemd-report-entropy[317]: is-system-running: running
12月 07 11:30:33 imacssd systemd-report-entropy[317]: REPORT ENTROPY systemd boot finished, quit.
```

## What do these outputs all mean?

The service will start before system enters `basic.target` and report time, entropy several times per second.

The output line with `is-system-running` is from `systemctl is-system-running`, which is used to determine the systemd bootup status.
`initializing` means the system hasn't reach `basic.target`, and is most likely tring to mount local filesystems.
`starting` is after `basic.target` and before `default.target`, when systemd is starting up system services. 

You can co-relate the timestamps, entropy with other systemd units to see at which point the entropy is enough.

To initialize kernel PRNG(Pseudo-Random Number Generator), that is for programs to able to read from `/dev/urandom` or `getrandom`,
the kernel needs at least 512 bits of entropy. Therefore any value less than 512 indicates that you may want to add entropy sources.
 

