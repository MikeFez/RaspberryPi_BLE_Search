from flask import Flask
from bluepy.btle import Scanner, DefaultDelegate


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        return()

scanner = Scanner().withDelegate(ScanDelegate())

app = Flask(__name__)


@app.route('/api/search/<string:mac_addr>', methods=['GET'])
def device_scan(mac_addr):
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(3.0)
    for dev in devices:
        if dev.addr == mac_addr:
            return("true")
    return("false")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
