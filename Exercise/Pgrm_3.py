# Async Programming: Generate numbers asynchronously
# Write an async function that counts down from 0 to 100 asynchronously and appends to a list named "numbers" and returns the list.

# The program can sleep asynchronously for 0.01 seconds in each iteration. [Optional]

import asyncio

async def generate_numbers():
    numbers = []
    for number in range(101):
        numbers.append(number)
        await asyncio.sleep(0.01)
    return numbers

async def main():
    numbers = await generate_numbers()
    print(numbers)


if __name__ == "__main__":
    asyncio.run(main())