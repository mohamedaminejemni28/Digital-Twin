import asyncio
import bleak
import json
from bleak import BleakClient

async def run():
    def callback(sender, data):
        parsed = {
            "heart_rate": int(data[1]),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "athlete_id": "athlete_ble"
        }
        print(json.dumps(parsed))
    async with BleakClient(SENSOR_ADDRESS) as client:
        await client.start_notify(CHARACTERISTIC_UUID, callback)
        await asyncio.sleep(60)  # run for 1 minute

asyncio.run(run())