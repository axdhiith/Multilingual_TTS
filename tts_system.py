import os
import tempfile
import soundfile as sf
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from scipy.signal import resample

class MultilingualTTSSystem:
    def __init__(self):
        print("Initializing TTS model...")
        self.model_name = "tts_models/multilingual/multi-dataset/your_tts"
        self.manager = ModelManager()
        self.model_path, self.config_path, _ = self.manager.download_model(self.model_name)
        self.synthesizer = Synthesizer(
            self.model_path,
            self.config_path
        )

        self.languages = {"English": "en", "French": "fr-fr", "Portuguese": "pt-br"}

        self.voice_samples = {
            "Female": "sample_voices/female.wav",
            "Male": "sample_voices/male.wav",
        }

    def add_robotic_effect(self, wav):
        pitch_factor = 0.8 
        return resample(wav, int(len(wav) * pitch_factor))

    def synthesize_speech(self, text, language, voice):
        try:
            language_code = self.languages.get(language)
            speaker_audio = self.voice_samples.get(voice)

            if not language_code:
                raise ValueError("Invalid language selected.")
            
            if voice == "Robotic":
                speaker_audio = self.voice_samples.get("Male")
                if not speaker_audio:
                    raise ValueError(f"Speaker audio file for {voice} not found.")
                wav = self.synthesizer.tts(
                    text=text,
                    speaker_wav=speaker_audio,
                    language_name=language_code
                )
                wav = self.add_robotic_effect(wav)
            else:
                if not speaker_audio:
                    raise ValueError(f"Speaker audio file for {voice} not found.")
                wav = self.synthesizer.tts(
                    text=text,
                    speaker_wav=speaker_audio,
                    language_name=language_code
                )
            
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
                sf.write(temp_file.name, wav, 22050)
                temp_file_path = temp_file.name
            
            return temp_file_path
        except Exception as e:
            print(f"Error in TTS synthesis: {e}")
            return str(e)