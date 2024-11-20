# Multilingual Text-to-Speech (TTS) Tool

A Text-to-Speech system powered by the **Your_TTS** pre-trained model, capable of generating natural-sounding speech in English, French, and Portuguese with Male, Female, and Robotic voice options.

## Live Demo

Try out the system live on Hugging Face Spaces: [Multilingual TTS Demo](https://axdhiith-multilingual-tts.hf.space)

> Note: The demo is optimized for desktop/laptop devices and may not work properly on mobile devices.

## Features

- **3 Languages**
  - English
  - French
  - Portuguese

- **3 Voice Options**
  - Male
  - Female
  - Robotic (post-processed Male voice with effects)

- **Core Components**
  - Built with Python 3.9
  - Leveraged [Coqui TTS](https://github.com/coqui-ai/TTS) library
  - Uses pre-trained `Your_TTS` model
  - Efficient temporary file management

## Technical Implementation

### Model Selection
This project uses the **Your_TTS** model for the following reasons:
- Built-in multilingual support
- High-quality voice synthesis
- Efficient performance
- No reliance on external APIs

The implementation is completely self-contained and doesn't require any cloud-based TTS services or external APIs, making it suitable for offline use and ensuring full control over the voice generation process.

## Installation

### Prerequisites
- Python 3.9.18
  - Recommended: Use Anaconda environment (preferred)
  - Alternative: Use `pyenv` or similar tools for version management

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/axdhiith/Multilingual_TTS.git
   cd Multilingual_TTS
   ```

2. Set up Python environment:

   **Option A: Using Anaconda (Recommended)**
   ```bash
   # Create a new conda environment
   conda create -n tts-env python=3.9.18
   
   # Activate the environment
   conda activate tts-env
   ```

   **Option B: Using pip/venv**
   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the environment
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> **Note**: Using Anaconda is recommended as it helps manage package dependencies and avoid conflicts, especially with PyTorch and other ML libraries.

## Usage

### Web Interface

Launch the Gradio web application:
```bash
python app.py
```

## Key Features in Detail

- **Language Support**: Full support for English, French, and Portuguese
- **Voice Variety**: Male, Female, and Robotic voice options
- **File Management**: Automatic cleanup of temporary audio files
- **Web Interface**: User-friendly Gradio-based interface
- **API Access**: Programmatic access for integration

## Future Development

- [ ] Exploring other models
- [ ] Additional language support
- [ ] Improved robotic voice processing
- [ ] Extended voice options


## Acknowledgements

- **Coqui TTS** for the Your_TTS model
- Built with Python, Gradio, PyTorch, and Coqui TTS

---

For issues, feature requests, or contributions, please open an issue or pull request in the repository.
