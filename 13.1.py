
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    print('Давайте проверим кто босс этой качалки!')
    participants = [
        ('Pasha', 3),
        ('Denis', 4),
        ('Billy', 5)
    ]
    tasks = [asyncio.create_task(start_strongman(name, power)) for name, power in participants]
    await asyncio.gather(*tasks)
    print('Победил Billy!')



asyncio.run(start_tournament())




