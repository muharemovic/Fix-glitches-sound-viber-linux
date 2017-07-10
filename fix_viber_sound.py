#!/usr/bin/python
def fix_viber():
    with open('/etc/pulse/default.pa','r') as f:
        c = f.read()
        if 'tsched=0' in c:
            print("\n\n\t\t\t\t+++ all is ok, no need fix ++++\n\n")

        else:
            r = c.replace('load-module module-udev-detect', 'load-module module-udev-detect tsched=0')
            with open('/etc/pulse/default.pa', 'w+') as k:
                k.write(r)
                k.close()

fix_viber()