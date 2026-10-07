import asyncio
from machine import Pin
# دیاریکردنی LED
try:
    led = Pin("LED", Pin.OUT)
except:
    led = Pin(25, Pin.OUT)
# ئەرکی بلینک — وەک vBlinkTask
async def blink_task():
    while True:
        led.value(1)
        await asyncio.sleep_ms(250)   # وەک vTaskDelay(250)
        led.value(0)
        await asyncio.sleep_ms(250)   # وەک vTaskDelay(250)
# ئەرکی دووەم (نموونە — دەتوانیت زیاد بکەیت)
async def print_task():
    while True:
        print(" ئەرکی دووەم کار دەکات")
        await asyncio.sleep(2)   # هەر ٢ چرکە
# فانکشنی سەرەکی — وەک main()
async def main():
    # دروستکردنی ئەرکەکان — وەک xTaskCreate
    task1 = asyncio.create_task(blink_task())
    task2 = asyncio.create_task(print_task())
    # چاوەڕوانی ئەرکەکان (هەرگیز کۆتایی نایەت)
    await task1
    await task2
# دەستپێکردنی scheduler — وەک vTaskStartScheduler()
asyncio.run(main())