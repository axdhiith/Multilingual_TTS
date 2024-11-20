# Multilingual Text-to-Speech (TTS) System

A robust multilingual Text-to-Speech system powered by the **Your_TTS** pre-trained model, capable of generating natural-sounding speech in multiple languages with diverse voice options.

## 🌟 Features

- **Multiple Languages**
  - English
  - French
  - Portuguese

- **Voice Options**
  - Male
  - Female
  - Robotic (post-processed Male voice with effects)

- **Core Components**
  - Built with Python 3.9
  - Powered by [Coqui TTS](https://github.com/coqui-ai/TTS) library
  - Uses pre-trained `Your_TTS` model
  - Efficient temporary file management

## 🤖 Technical Implementation

### Model Selection
This project uses the **Your_TTS** model from Coqui TTS for several key reasons:
- Built-in multilingual support
- High-quality voice synthesis
- Efficient performance
- Active community support
- No reliance on external APIs

The implementation is completely self-contained and doesn't require any cloud-based TTS services or external APIs, making it suitable for offline use and ensuring full control over the voice generation process.

## ⚙️ Installation

### Prerequisites

- Python 3.9.18 
  - Use `pyenv` or similar tools for version management

### Setup Steps

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Web Interface

Launch the Gradio web application:
```bash
python app.py
```

The web interface allows you to:
- Input text for conversion
- Select your desired language
- Choose a voice type
- Generate and play audio files

### Programmatic Usage

```python
from tts_system import MultilingualTTSSystem

# Initialize the system
tts_system = MultilingualTTSSystem()

# Example usage
text = "Bonjour, comment allez-vous?"
language = "French"
voice = "Female"

# Generate speech
wav_path = tts_system.synthesize_speech(text, language, voice)
print(f"Generated audio saved at: {wav_path}")
```

## 🗂️ Project Structure

```
.
├── app.py              # Gradio web interface
├── tts_system.py       # Core TTS functionality
├── TTS/                # Coqui TTS library
├── sample_voices/      # Voice sample files
└── requirements.txt    # Project dependencies
```

## 🔧 Technical Requirements

```bash
# Install Python 3.9.18 first, then:
pip install -r requirements.txt
```

## 🎯 Key Features in Detail

- **Language Support**: Full support for English, French, and Portuguese
- **Voice Variety**: Male, Female, and Robotic voice options
- **File Management**: Automatic cleanup of temporary audio files
- **Web Interface**: User-friendly Gradio-based interface
- **API Access**: Programmatic access for integration

## 🔄 Future Development

- [ ] Additional language support
- [ ] Enhanced user interface
- [ ] Improved robotic voice processing
- [ ] Extended voice options
- [ ] Performance optimizations

## 📝 Implementation Notes

- **Temporary Files**: The system generates `.wav` files that are automatically removed after playback
- **Extensibility**: Add new languages/voices by updating `self.languages` and `self.voice_samples` in `tts_system.py`
- **Model**: Utilizes the pre-trained `Your_TTS` model from Coqui TTS

## 🙏 Acknowledgements

- **Coqui TTS** for the Your_TTS model
- Built with Python, Gradio, PyTorch, and Coqui TTS

## 📄 License

[Add your license information here]

---

For issues, feature requests, or contributions, please open an issue or pull request in the repository.
