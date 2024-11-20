import gradio as gr
from tts_system import MultilingualTTSSystem

tts_system = MultilingualTTSSystem()

def generate_tts(text, language, voice):
    try:
        return tts_system.synthesize_speech(text, language, voice)
    except Exception as e:
        return str(e)

interface = gr.Interface(
    fn=generate_tts,
    inputs=[
        gr.Textbox(label="Enter text"),
        gr.Dropdown(["English", "French", "Portuguese"], label="Select Language"),
        gr.Dropdown(
            ["Male", "Female", "Robotic"],
            label="Select Voice",
        ),
    ],
    outputs=gr.Audio(label="Generated Speech"),
    title="Multilingual TTS System",
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch(share=True)