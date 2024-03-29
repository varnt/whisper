import os
import whisper
import json
from pydub import AudioSegment

def convert_to_mp3(input_file, output_file):
    # Load audio file
    sound = AudioSegment.from_file(input_file)

    # Export as MP3
    sound.export(output_file, format="mp3")

def convert_folder_to_mp3(input_folder, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files and subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Check if the file is an audio file
            if file.lower().endswith(('.wav', '.mp3', '.ogg', '.flac', '.m4a')):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, os.path.relpath(input_file_path, input_folder))
                output_file_path = os.path.splitext(output_file_path)[0] + ".mp3"  # Change extension to .mp3
                convert_to_mp3(input_file_path, output_file_path)
                print("Converted:", input_file_path, "->", output_file_path)
                #transcribe(output_file_path,output_folder,transcribe_folder)



  

def convert_folder_to_transcript(input_folder, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files and subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Check if the file is an audio file
            if file.lower().endswith(('.wav', '.mp3', '.ogg', '.flac', '.m4a')):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, os.path.relpath(input_file_path, input_folder))
                output_file_path = os.path.splitext(output_file_path)[0] +"_BASE_"+ ".txt"  # Change extension to .txt
                model = whisper.load_model("base")
                result = model.transcribe(input_file_path)
                file_path = output_file_path
                print(result["text"])
    

                # Write the text content to the file
                with open(file_path, "w") as file:
                    file.write(json.dumps(result))

                # Read the content of the file to verify
                with open(file_path, "r") as file:
                    saved_content = file.read() 

def convert_folder_to_transcript_medium(input_folder, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files and subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Check if the file is an audio file
            if file.lower().endswith(('.wav', '.mp3', '.ogg', '.flac', '.m4a')):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, os.path.relpath(input_file_path, input_folder))
                output_file_path = os.path.splitext(output_file_path)[0] +"_MEDIUM_"+ ".txt"  # Change extension to .txt
                model = whisper.load_model("medium")
                result = model.transcribe(input_file_path)
                file_path = output_file_path
                print(result["text"])
    

                # Write the text content to the file
                with open(file_path, "w") as file:
                    file.write(json.dumps(result))

                # Read the content of the file to verify
                with open(file_path, "r") as file:
                    saved_content = file.read() 

def convert_folder_to_transcript_LARGE(input_folder, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files and subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Check if the file is an audio file
            if file.lower().endswith(('.wav', '.mp3', '.ogg', '.flac', '.m4a')):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, os.path.relpath(input_file_path, input_folder))
                output_file_path = os.path.splitext(output_file_path)[0] +"_large_"+ ".txt"  # Change extension to .txt
                model = whisper.load_model("large")
                result = model.transcribe(input_file_path)
                file_path = output_file_path
                print(result["text"])
    

                # Write the text content to the file
                with open(file_path, "w") as file:
                    file.write(json.dumps(result))

                # Read the content of the file to verify
                with open(file_path, "r") as file:
                    saved_content = file.read() 



if __name__ == "__main__":
    input_folder = "/home/ubuntuwsl/rec/"  # Change this to your input folder
    output_folder = "/home/ubuntuwsl/recmp3/"  # Change this to your desired output folder
    transcribe_folder = "/home/ubuntuwsl/rectranscribe/"  # Change this to your desired output folder
    
    if os.path.exists(input_folder):
        ##convert_folder_to_mp3(input_folder, output_folder)
        print("Conversion completed.")
        print("StartTranscribing_Base")
        convert_folder_to_transcript(output_folder,transcribe_folder)
        print("StartTranscribing_Medium")
        convert_folder_to_transcript_medium(output_folder,transcribe_folder)
        print("StartTranscribing_Large")
        convert_folder_to_transcript_LARGE(output_folder,transcribe_folder)
    else:
        print("Input folder not found.")
