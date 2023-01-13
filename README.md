# python-usb-linux
Extract Usb Serial Bus Information Really quick with python. Class based. Tested and used


# Installation

```Bash
cd <project dir>
git clone https://github.com/Donny-GUI/python-usb-linux.git

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

# Description

Just Wraps arround linux bash. lsusb to tempfile then read temp file. From there it creates classes for the information

# Class LinuxUSB()

queryusb.LinuxUSB()
main data class
supplied by dataclass queryusb.SerialBus


```Python3
class LinuxUsb:
```

