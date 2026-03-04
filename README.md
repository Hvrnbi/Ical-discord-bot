# ical-discord-bot
___

The **Ical Discord Bot** sends your daily events from an .ics calendar directly to Discord.

___

## Deploy the Bot

1. Clone this repository.
2. Create a ".env" file at the root of the project and add the following:
   ```
   TOKEN=""
   GUILD=""
   ```
3. Create an application on [Discord Developer Portal](https://discord.com/developers/).
   - Go to the **Bot** section and click **Reset Token**.
   - Copy the token and paste it into the '.env' file, inside the quotes after "TOKEN=".
4. Copy the ID of the server where you want to invite the bot.
   - Right-click the server name in the sidebar (with Developer Mode enabled).
   - Paste the ID into the ".env" file, inside the quotes after "GUILD=".
5. Create a "data" folder at the root of the project and place your calendar file inside.
6. Rename your calendar file to "cal.ics".
7. Create a virtual environment and install the dependencies:
   ```
   pip install -r requirements.txt
   ```
8. Run the main file.
9. Add the bot to your server.

That’s it! You can now view your events for today using the "/day(today)" command (by default).