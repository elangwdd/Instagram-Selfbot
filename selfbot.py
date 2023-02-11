import asyncio
import aiohttp

async def help_menu():
    print("=============================")
    print("Instagram Self-Bot v0.1")
    print("=============================")
    print("Menu:")
    print("1. Follow user")
    print("2. Unfollow user")
    print("3. Speed test")
    print("4. Exit")
    print("=============================")

async def follow_user(session, username):
    # Follow user
    async with session.post(f'https://www.instagram.com/web/friendships/{username}/follow/'):
        print(f"Successfully followed {username}")

async def unfollow_user(session, username):
    # Unfollow user
    async with session.post(f'https://www.instagram.com/web/friendships/{username}/unfollow/'):
        print(f"Successfully unfollowed {username}")

async def speed_test():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        # Do a speed test
        async with session.get("https://www.google.com"):
            end_time = time.time()

    # Calculate the response time in milliseconds
    response_time = (end_time - start_time) * 1000
    print("Response time: %.2f ms" % response_time)

async def login_instagram(session):
    # Your Instagram username and password
    login_data = {
        'username': 'YOUR_USERNAME',
        'password': 'YOUR_PASSWORD'
    }

    # Login to Instagram
    async with session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data):
        pass

async def main():
    await help_menu()
    async with aiohttp.ClientSession() as session:
        await login_instagram(session)
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter the username to follow: ")
                await follow_user(session, username)
            elif choice == "2":
                username = input("Enter the username to unfollow: ")
                await unfollow_user(session, username)
            elif choice == "3":
                await speed_test()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    asyncio.run(main())
