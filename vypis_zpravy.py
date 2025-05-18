from mfrc522 import MFRC522
from rfidaccess import RfidAccess
import utime


reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

print("")
print("Please place card on reader")
print("")

PreviousCard = [0]

try:
    while True:
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if uid == PreviousCard:
                continue
            if stat == reader.OK:
                print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid), "little", False)).upper(), reader.tohexstring(uid)))
                defaultKey = [255, 255, 255, 255, 255, 255]

                # Read the message from block 1 of sector 1
                (stat, data) = reader.readSectorBlock(uid, 1, 1, keyA=defaultKey)
                if stat == reader.OK:
                    message = ''.join(chr(b) for b in data).strip('\x00')
                    print("Message on card: {}".format(message))
                    if message == "Hubkaaultralight":
                        print("KrupRup")
                else:
                    print("Reading message failed!")

                PreviousCard = uid
                break
        else:
            PreviousCard = [0]
        utime.sleep_ms(50)

except KeyboardInterrupt:
    print("Bye")