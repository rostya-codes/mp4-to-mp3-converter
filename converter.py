import moviepy.editor


video = moviepy.editor.VideoFileClip('growguide3-163onmyneck.mp4') # Initialize video
audio = video.audio # Get audio from file
audio.write_audiofile('my_audio.mp3') # Save mp3 file
