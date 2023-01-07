import os

class Files:
    temp = f'{os.getcwd()}/tempfile'
    read = 'r'
    append = 'a'
    write = 'w'
    create = 'x'
    readbytes = 'rb'
    writebytes = 'wb'

class Commands:
    listUsb = 'lsusb'
    overwriteFile = ">"

class SerialBus:
    def __init__(self, bus: str, device: str, ID: str, name: str):
        self.bus = bus
        self.device = device
        self.id = ID
        self.name = name
        self.serialbus = {"bus":self.bus, "device": self.device, "id":self.id, "name":self.name}

    def __str__(self):
        return self.serialbus

class LinuxUSB:
    def __init__(self):
        self.items = parse_usb_list(lsusb())
        self.names = [x.name for x in self.items]
        self.busses = [x.bus for x in self.items]
        self.devices = [x.device for x in self.items]
        self.ids = [x.id for x in self.items]
        self.values = {"items": self.items, "names": self.names, "busses":self.busses, "devices": self.devices, "ids":self.ids}

    def refresh(self):
        self.items = parse_usb_list(lsusb())
        self.names = [x.name for x in self.items]
        self.busses = [x.bus for x in self.items]
        self.devices = [x.device for x in self.items]
        self.ids = [x.id for x in self.items]
        self.values = {"items": self.items, "names": self.names, "busses":self.busses, "devices": self.devices, "ids":self.ids}

    def get(self) -> list[str]:
        return self.values

    def getItems(self) -> list[str]:
        return self.values["items"]

    def getNames(self) -> list[str]:
        return self.values["names"]

    def getBus(self) -> list[str]:
        return self.values["busses"]

    def getDevices(self) -> list[str]:
        return self.values["devices"]

    def getIds(self) -> list[str]:
        return self.values["ids"]

    def show(self) -> None:
        print(self.values)

    def showDevices(self) -> None:
        for item in self.items:
            print(item.device)

    def showBus(self) -> None:
        for item in self.items:
            print(item.bus)

    def showIDs(self) -> None:
        for item in self.items:
            print(item.id)

    def showNames(self) -> None:
        for item in self.items:
            print(item.name)


def parse_usb_list(serial_list: list[str]) -> list[SerialBus]:
    retv = []
    for x in serial_list:
        bus_area = str(x)
        busid_name = bus_area.rsplit(":")
        bus = busid_name[0][:8]
        device = busid_name[0][7:].strip(" ")
        ID = busid_name[1][3:] + busid_name[2][:5]
        name = busid_name[2][5:].strip(" ")
        ID = ID.strip(" ")
        retv.append(
            SerialBus(
                bus=bus, 
                device=device, 
                ID=ID, 
                name=name
                )
            )
    return retv

def lsusb() -> list[str]:
    os.system(f"{Commands.listUsb} {Commands.overwriteFile} {Files.temp}")
    with open(Files.temp, Files.read) as rfile:
        lines = [x.strip("\n") for x in rfile.readlines()]
    os.remove(Files.temp)
    return lines


lusb = LinuxUSB()
lusb.show()
lusb.showNames()
lusb.showDevices()

