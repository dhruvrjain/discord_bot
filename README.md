# Discord Bot

This is a simple Discord bot that responds to commands and has a specific `/kill` command to simulate a moon-breathing attack on a target.

## Prerequisites

To run this bot, you need the following:

- Python 3.6 or higher installed
- `discord.py` library installed (version 1.7.3 or higher)

## Getting Started

Follow the steps below to get the bot up and running:

1. Clone the repository or download the source code.

2. Install the required dependencies. Open a terminal or command prompt and run the following command:

```
pip install discord.py
```

This will install the necessary `discord.py` library.

3. Create a Discord bot and get the bot token:
- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Click on "New Application" and give it a name.
- Navigate to the "Bot" tab on the left sidebar.
- Click on "Add Bot" and confirm the prompt.
- Under the "Token" section, click on "Copy" to copy your bot token.

4. Authorize the bot to join your server:
- In the Discord Developer Portal, go to the "OAuth2" tab on the left sidebar.
- Under the "Scopes" section, select "bot".
- Under the "Bot Permissions" section, choose the necessary permissions your bot requires (e.g., "Send Messages").
- Copy the generated OAuth2 URL and open it in a browser.
- Select a server where you have administrative privileges and authorize the bot to join.

5. Configure the bot:
- Open the `bot.py` file in a text editor.
- Replace `"PASTE_YOUR_TOKEN_HERE"` in the last line with the bot token you copied in step 3.
- Save the file.

6. Run the bot:
- Open a terminal or command prompt and navigate to the directory where the `bot.py` file is located.
- Run the following command:

  ```
  python bot.py
  ```

- The bot should now be online and ready to respond to commands.

## Usage

Once the bot is running and connected to your server, you can use the following commands:

- `/info` - Displays information about the bot and available commands.
- `/ping` - Responds with "pong".
- `/kill @someone` - Simulates a moon-breathing attack on the mentioned user.( Try to kill yourself or the bot )
- `/sorry` - Appologize to the bot after killing it

## Contributing

If you want to contribute to this project, feel free to submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
