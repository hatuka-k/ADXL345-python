import mraa
import sys
import time

def init(ADXL345_I2C):
    ADXL345_I2C.address(0x53)

    if(ADXL345_I2C.readReg(0x00)!=0xe5):
        print("Error: ADXL345 is not connect")
        sys.exit()

    ADXL345_I2C.writeReg(0x2D,0x08)

def test1(ADXL345_I2C):
    for i in range(0,100):
        print(hex(ADXL345_I2C.readWordReg(0x32)))
        print(hex(ADXL345_I2C.readWordReg(0x34)))
        print(hex(ADXL345_I2C.readWordReg(0x36)))
        time.sleep(1)


if __name__ == "__main__":
    ADXL345_I2C = mraa.I2c(6)
    init(ADXL345_I2C)
    test1(ADXL345_I2C)

