import os
import subprocess
import audiosegment

# Get the current working directory
current_dir = os.getcwd()

print("Text: ")
text = input()

print("\nSpeaker's Gender? \n 1 Male\n 2 Female")
gender = input()
print("\nSpeaker's Language? \n 1 English\n 2 Indonesian")
language = input()

output_file = os.path.join(current_dir, "edge.mp3")

if gender == "1":
    if language == "1":
        voice = 'en-AU-WilliamNeural'
    else:
        voice = 'id-ID-ArdiNeural'
else:
    if language == "1":
        voice = 'en-GB-SoniaNeural'
    else:
        voice = 'id-ID-GadisNeural'

command = ['edge-tts', '--voice', voice, '--text', text, '--write-media', output_file]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode != 0:
    print(f"Error: {result.stderr}")
else:
    print(result.stdout)

    if os.path.exists(output_file):
        audio = audiosegment.from_file(output_file)

        # Set the output format to WAV
        audio = audio.set_sample_width(2)
        audio = audio.set_frame_rate(44100)
        audio = audio.set_channels(1)

        # Export the audio to WAV format
        wav_output = os.path.join(current_dir, "edge-conv.wav")
        audio.export(wav_output, format='wav')

        print("DONE: Audio for cloning")
    else:
        print(f"Error: {output_file} was not created")
