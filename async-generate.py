import asyncio
import ollama
import sys

async def main():
    client = ollama.AsyncClient()
    response = await client.generate('llama3.2', 'Why is the sky blue?')
    print(response['response'])

# Fix for Windows' event loop issues
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    try:
        asyncio.run(main())  # Use asyncio.run() safely
    except KeyboardInterrupt:
        print('\nGoodbye!')
