from time import sleep

from Discord import Discord

discord = None
try:
    print("Starting process...")

    discord = Discord()

    print("Attempting to open dashboard...")

    discord.make_login()
    sleep(5)
    discord.search_users()

finally:
    discord.exit()
    print("Done")
