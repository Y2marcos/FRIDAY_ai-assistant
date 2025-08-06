# Friday AI Assistant

An advanced voice-based AI assistant built with LiveKit agents, designed to provide intelligent conversation, system control, and proactive support through natural Hinglish communication.

## Overview

Friday is a sophisticated AI assistant created by **Me** that combines the elegance of Iron Man's Friday with modern Indian communication style. It provides real-time assistance for various tasks including application control, file management, web search, weather updates, and system automation.

## Features

### 🎯 **Core Capabilities**
- **Voice-based interaction** with natural Hinglish communication
- **Application control** - Open, close, and manage desktop applications
- **File and folder management** - Search, open, create, rename, and delete files/folders
- **System automation** - Keyboard shortcuts, mouse control, typing automation
- **Web search** - Real-time Google search integration
- **Weather updates** - Location-based weather information
- **Smart window management** - Focus and control application windows

### 🛠️ **System Control Tools**
- **Mouse Control**: Move cursor, click, scroll, swipe gestures
- **Keyboard Control**: Type text, press keys, hotkey combinations
- **Volume Control**: Adjust system volume up/down/mute
- **Window Management**: Focus, minimize, restore application windows

### 🌐 **Web Integration**
- **Google Custom Search** - Real-time web search results
- **Weather API** - Current weather conditions with IP-based location detection
- **Date/Time** - Current datetime information

### 📁 **File Operations**
- **Smart file search** using fuzzy matching
- **Multi-format support** - MP4, MP3, PDF, PPT, images, documents
- **Folder operations** - Create, rename, delete, browse
- **Automated file opening** with window focus

## Installation

### Prerequisites
- Python 3.8+
- Windows OS (for full functionality)
- Required API keys (Google, OpenWeather)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Y2marcos/friday-ai-assistant.git
cd friday-ai-assistant
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
Create a `.env` file with your API keys:
```env
# LiveKit config
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_secret
LIVEKIT_URL=your_livekit_url

# Google Gemini API key
GOOGLE_API_KEY=your_google_api_key

# Google Search API key & search ID
GOOGLE_SEARCH_API_KEY=your_google_search_api_key
SEARCH_ENGINE_ID=your_search_engine_id

# Weather API Key
OPENWEATHER_API_KEY=your_openweather_api_key
```

4. **Run the assistant**
```bash
python agent.py
```

## File Structure

```
friday-ai-assistant/
├── agent.py                    # Main agent entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── Friday_prompts.py          # AI personality and behavior prompts
├── Friday_google_search.py    # Google search functionality
├── friday_get_weather.py      # Weather information service
├── Friday_window_CTRL.py      # Window and app control
├── Friday_file_opener.py      # File management operations
└── keyboard_mouse_CTRL.py     # System automation controls
|__ test_prompt.py             # test the packages is install properly
```


## API Requirements

### Google APIs
- **Google Custom Search API** - For web search functionality
- **Google Gemini API** - For AI language processing

### Weather API
- **OpenWeatherMap API** - For weather information

### LiveKit
- **LiveKit Cloud** - For real-time voice processing

## Configuration

### Application Mappings
Customize app shortcuts in `Friday_window_CTRL.py`:
```python
APP_MAPPINGS = {
    "notepad": "notepad",
    "calculator": "calc",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vs code": "C:\\Users\\yourname\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    # Add your applications here
}
```

### File Search Directories
Configure search directories in relevant files:
```python
folders_to_index = ["C:/", "D:/", "E:/"]  # Add your preferred drives
```

## Security Features

- **Token-based activation** for system control functions
- **Temporary activation** with auto-deactivation
- **Action logging** for audit trail
- **Input validation** for system commands

## Dependencies

### Core Libraries
- `livekit-agents` - Voice processing framework
- `livekit-plugins-google` - Google services integration
- `pyautogui` - System automation
- `pynput` - Keyboard and mouse control

### Search and Processing
- `fuzzywuzzy` - Fuzzy string matching
- `python-Levenshtein` - String similarity
- `requests` - HTTP requests
- `python-dotenv` - Environment management

### Windows Integration
- `pywin32` - Windows API access
- `pygetwindow` - Window management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

- Inspired by Iron Man's Friday AI assistant
- Built with LiveKit's real-time AI framework
- Integrates multiple Google and OpenWeather APIs
- Designed for Indian users with Hinglish support


**Note**: This assistant requires appropriate API keys and permissions for full functionality. Ensure you have valid API access before deployment.
