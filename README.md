# Countdown-timer

This is a **Discord bot** that provides a countdown to the release of **Honkai: Star Rail 3.1** (ofcs you can change what it countdowns to). It updates the time remaining in different phases and announces the release when the countdown hits zero. (you can manually change the date)

NOTE:
You have to change the date manually as I haven't added a command to change it automatically from discord

## Features
✅ **Live Countdown** – Displays the time left until release
✅ **Automatic Updates** – Changes messages as time progresses
✅ **Final Announcement** – Alerts everyone when the update goes live
✅ **Cool Embed Messages** – Uses Discord embeds for a clean look


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

