# Countdown-timer

This is a **Discord bot** that provides a countdown to the release of **Honkai: Star Rail 3.1**. It updates the time remaining in different phases and announces the release when the countdown hits zero. (you can manually change the date)

## Features
✅ **Live Countdown** – Displays the time left until release
✅ **Automatic Updates** – Changes messages as time progresses
✅ **Final Announcement** – Alerts everyone when the update goes live
✅ **Cool Embed Messages** – Uses Discord embeds for a clean look

## Requirements
- Python 3.8 or newer
- Discord bot token
- Required Python libraries:
  ```bash
  pip install discord.py pytz
  ```

## How to Use
1. **Clone this repo** (or copy the script)
   ```bash
   git clone https://github.com/yourusername/honkai-countdown-bot.git
   cd honkai-countdown-bot
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your bot token**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a bot and copy the token
   - Replace `YOUR_BOT_TOKEN` in the script with your actual token

4. **Run the bot**
   ```bash
   python bot.py
   ```

## How It Works
1. The bot starts by getting the **current time** and the **target release time**.
2. It sends an **initial message** with the countdown.
3. The countdown updates in phases:
   - **More than 2 days left** → "Preparing for departure"
   - **1 day left** → "Preparing for arrival"
   - **30 minutes left** → "Arriving at your destined location"
4. When the countdown hits **zero**, it announces the release with a final message.

## Notes
- Make sure your bot has the **message content intent** enabled.
- The bot runs in **Asia/Manila timezone** (adjust if needed).
- Customize the messages as you like!

## License
Feel free to modify and use this bot for your own countdowns!

