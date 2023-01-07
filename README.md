# python-usb-linux
Extract Usb Serial Bus Information Really quick with python. Class based. Tested and used


# Installation

```Bash
cd <project dir>
https://github.com/Donny-GUI/python-usb-linux.git

```

> within project

```Python3
import queryusb

def show_names():
  lusb = queryusb.LinuxUSB()
  lsusb.showNames()

show_names()

```
> or

```Python3
from queryusb import LinuxUSB

def show_names():
  lusb = LinuxUSB()
  lusb.showNames()
show_names()

```
