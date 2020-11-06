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
-- Logs begin at Sat 2020-08-01 09:15:18 JST, end at Fri 2020-11-06 01:40:57 JST. --
Nov 06 01:40:01 farseerfc-mbp systemd[1]: Started Start to report entropy in journal.
Nov 06 01:40:01 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:01,821656364+09:00 2256
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[424]: starting
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:02,094607322+09:00 2257
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[467]: starting
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:02,342393182+09:00 2261
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[529]: starting
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:02,624923358+09:00 2265
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[639]: starting
Nov 06 01:40:02 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:02,888413750+09:00 2269
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[778]: starting
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:03,130162362+09:00 2270
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[797]: starting
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:03,369049032+09:00 2271
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[864]: starting
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:03,611843147+09:00 2272
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[905]: starting
Nov 06 01:40:03 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:03,851492751+09:00 2273
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[913]: starting
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:04,091936135+09:00 2275
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[1036]: starting
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:04,330146916+09:00 2275
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[1053]: starting
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:04,570204545+09:00 2276
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[1092]: starting
Nov 06 01:40:04 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:04,817767855+09:00 2277
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[1117]: starting
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:05,058280321+09:00 2277
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[1125]: starting
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:05,297474806+09:00 2278
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[1132]: starting
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:05,538473136+09:00 2279
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[1139]: starting
Nov 06 01:40:05 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:05,779119853+09:00 2282
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[1146]: starting
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:06,019094053+09:00 2287
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[1153]: starting
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:06,262658068+09:00 2293
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[1160]: starting
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:06,503870376+09:00 2296
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[1167]: starting
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:06,749538576+09:00 2299
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[1175]: starting
Nov 06 01:40:06 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:06,990995043+09:00 2301
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[1182]: starting
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:07,232147585+09:00 2301
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[1189]: starting
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:07,476427253+09:00 2302
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[1233]: starting
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: ENTROPY 2020-11-06T01:40:07,717667752+09:00 2302
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY is-system-running:
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[1249]: running
Nov 06 01:40:07 farseerfc-mbp systemd-report-entropy[311]: REPORT ENTROPY systemd boot finished, quit.
```


