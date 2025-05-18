from mfrc522 import MFRC522
from rfidaccess import RfidAccess
import utime

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)
access = RfidAccess()

print("")
print("Please place card on reader")
print("")

def checksum(data):
    crc = 0xc7
    for byte in data:
        crc ^= byte
        for _ in range(8):
            msb = crc & 0x80
            crc = (crc << 1) & 0xff
            if msb:
                crc ^= 0x1d
    return crc

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
                
                # Message to write
                message = "HubkaAultralight"
                # Convert message to byte array and pad if necessary
                message_bytes = [ord(c) for c in message]
                if len(message_bytes) < 16:
                    message_bytes += [0] * (16 - len(message_bytes))

                # Write the message to block 1 of sector 1
                if reader.writeSectorBlock(uid, 1, 1, message_bytes, keyA=defaultKey) == reader.ERR:
                    print("Writing message failed!")
                else:
                    print("Message written successfully!")

                previousCard = uid
                break
        else:
            PreviousCard = [0]
        utime.sleep_ms(50)

except KeyboardInterrupt:
    print("Bye")
