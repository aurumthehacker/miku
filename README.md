# miku
### A cybersecurity Discord bot made by aurum8322

This is a multi-functional Discord bot built using the `discord.py` library, designed to offer various utilities and fun features. Here's a detailed description of its capabilities and features:

### Description

**Miku Bot** is a versatile Discord bot named after the popular Vocaloid character Hatsune Miku. It provides various functionalities, from basic network mapping and password generation to fun and interactive commands. This bot is designed to enhance the user experience on Discord servers by offering useful tools and entertaining features.

### Key Features

1. **Network Utilities:**
   - **Network Mapping (`sudo netmap <ip_or_url>`):**
     - Performs a basic network mapping using the `socket` library.
     - Checks the IP address of a given URL or hostname.
     - Scans common ports (21, 22, 23, 80, 443) to check if they are open or closed.
   - **Find IP Address (`sudo findip <website>`):**
     - Resolves the IP address of a given website or hostname.

2. **Password Utilities:**
   - **Generate Password (`sudo genpass [length]`):**
     - Generates a random password of specified length (default is 12 characters).
     - Includes a mix of letters, digits, and punctuation.
   - **Create Password List (`sudo passlist [count] [length]`):**
     - Generates a list of random passwords.
     - Allows specifying the number of passwords and their length.

3. **Help and Information:**
   - **Help Command (`sudo -h`):**
     - Displays an embedded help menu listing all available commands.
   - **Bot Information (`sudo neofetch`):**
     - Shows ASCII art of Miku along with the bot's version and author information.
   - **Ping Command (`sudo ping`):**
     - Displays the WebSocket latency to show the bot's responsiveness.
   - **YouTube Link (`sudo youtube`):**
     - Sends a special YouTube video link for fun interaction.

4. **Interactive Features:**
   - **Bot Mention Response:**
     - When the bot is mentioned, it responds with an embedded message providing its basic information and how to get help.

### Technical Details

- **Environment Variables:** Utilizes a `.env` file to securely store the bot token.
- **Libraries Used:**
  - `discord.py`: Core library for interacting with the Discord API.
  - `dotenv`: For loading environment variables.
  - `socket`: For network-related commands.
  - `random` and `string`: For generating random passwords.
- **Intents:** Uses the default intents with `message_content` enabled to allow the bot to read message content.
- **Commands Framework:** Uses `commands.Bot` from `discord.ext` to handle command parsing and execution.

### Code Structure

- **Initialization and Configuration:**
  - Loads environment variables and sets up the bot with the necessary intents and command prefix.
- **Event Handlers:**
  - `on_ready()`: Prints a message when the bot successfully connects to Discord.
  - `on_message()`: Responds to bot mentions and processes other commands.
- **Commands:**
  - `netmap`: Performs network mapping and port scanning.
  - `genpass`: Generates a random password.
  - `findip`: Resolves the IP address of a website.
  - `passlist`: Creates a list of random passwords.
  - `help_command`: Displays the help menu.
  - `neofetch`: Shows ASCII art and version information.
  - `ping`: Displays WebSocket latency.
  - `youtube`: Sends a special YouTube video link.

### Example Usage

- To perform a basic network mapping:
  ```text
  sudo netmap example.com
  ```
- To generate a random password of 16 characters:
  ```text
  sudo genpass 16
  ```
- To find the IP address of a website:
  ```text
  sudo findip google.com
  ```
- To create a list of 5 passwords, each 10 characters long:
  ```text
  sudo passlist 5 10
  ```
- To view the help menu:
  ```text
  sudo -h
  ```
- To display the bot's information:
  ```text
  sudo neofetch
  ```
- To check the WebSocket latency:
  ```text
  sudo ping
  ```
- To send a fun YouTube video link:
  ```text
  sudo youtube
  ```

### Conclusion

Miku Bot is a comprehensive and multi-functional Discord bot designed to offer utility and fun in a Discord server. With its wide range of commands, it can assist users with network-related tasks, generate secure passwords, and provide helpful information and entertaining interactions.
