import machine  # type: ignore
import utime  # type: ignore

# Pinの番号
moterA = machine.Pin(14, machine.Pin.OUT)
moterB = machine.Pin(15, machine.Pin.OUT)


# 時計周り
def clockwise():
    moterA.high()  # high...ON
    moterB.low()  # low...OFF


# 反時計回り
def anticcloskwise():
    moterA.low()
    moterB.high()


# モーターを停止
def stopMoter():
    moterA.low()
    moterB.low()


# モーターを10秒間交互に回転と停止
while True:
    clockwise()
    utime.sleep(10)
    stopMoter()
    utime.sleep(1)
    anticcloskwise()
    utime.sleep(10)
    stopMoter()
    utime.sleep(1)
