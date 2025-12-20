<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=220&section=header&text=TimerBothole&fontSize=70&animation=fadeIn&fontAlignY=35&desc=Your%20Discord%20Productivity%20Partner&descAlignY=55&descAlign=50)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Disnake](https://img.shields.io/badge/Disnake-Library-CC0000?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/DisnakeDev/disnake)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

<h3>🚀 Boost your server's productivity with Pomodoro & Automation</h3>

<p>
  <b>TimerBothole</b> is a modular Discord bot built for focus and efficiency.<br>
  It handles multiple timers simultaneously and manages server routines automatically.
</p>

</div>

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **🍅 Multi-User Pomodoro** | Advanced session tracking allows multiple users to run their own timers simultaneously. |
| **🔊 Voice Integration** | The bot joins your VC to play high-quality audio alerts using FFmpeg. |
| **🛡️ Auto-Roles System** | Automatically assigns specific roles (e.g., `Novice`) to new members. |
| **⚙️ Slash Commands** | Modern interface using Discord's latest API (`/work`, `/stop`). |

---

## 🛠 Tech Stack & Structure

**Developed with:**

<div align="left">
	<img src="https://skillicons.dev/icons?i=python,vscode,discord,git,bash,linux&theme=light" height="40" />
</div>

<br>

**Project Tree:**

```text
TimerBothole/
├── 📄 main.py           # Bootloader & Cog Manager
├── 📄 .env              # Secrets (Token)
├── 🎵 alarm.mp3         # Audio asset
└── 📂 cogs/             # Modular Logic
    ├── 📄 timer.py      # Pomodoro Engine
    └── 📄 roles.py      # Event Listener System
```

---

## ⚡ Installation & Setup

> **Note:** Follow these steps to deploy the bot on your local machine.

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TimerBothole.git
cd TimerBothole
```

### 2️⃣ Virtual Environment

It is strictly recommended to isolate dependencies.

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install disnake python-dotenv
```

> ⚠️ **Important:** Ensure FFmpeg is installed and added to PATH.

### 4️⃣ Configuration

Create a `.env` file and paste your token:

```env
DISCORD_TOKEN=your_token_here
```

### 5️⃣ Launch

```bash
python main.py
```

---

## 📝 Usage

### Available Commands

- `/work <work_time> <break_time>` - Start a Pomodoro session
- `/stop` - Stop your active timer
- **Stop Button** - Integrated UI button to halt the session

### Example

```
/work 25 5
```
This starts a 25-minute work session followed by a 5-minute break.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
  <p>Made with ❤️ for productive Discord communities</p>
</div>
