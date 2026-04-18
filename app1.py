import streamlit as st 
from PIL import Image
from api_calling_app1 import note_generator, audio_transcription, quiz_generator

# title

st.title("Note Summary and Quiz Generator")

st.markdown("Upload up to 3 images to generate Note Summary and Quizzes")

st.divider()

with st.sidebar:
    st.header("Controls")
    # images
    images = st.file_uploader("Upload the photos of your note", type=["jpg","jpeg","png"],accept_multiple_files=True)
    
    pil_images = []
    for image in images:
        pil_image = Image.open(image)
        pil_images.append(pil_image)
    
    
    if images:
        # st.image(images)
        
        if len(images)>3:
            st.error("Upload at max 3 images")
            
        else:
            st.subheader("Uploaded images")
            col = st.columns(3)
            
            for i, image in enumerate(images):
                with col[i]:
                    st.image(image)
                    
    # difficulty level portion
    
    selected_option=st.selectbox("Enter the difficulty of your quiz", ("Easy","Medium","Hard"),index=None)
    
    # if selected_option:
    #     st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")
        
    # else:
    #     st.error("You must select a difficulty")
        
    # button 
    pressed=st.button("Click the button to initiate AI", type="primary")
    
if pressed:
    if not images:
        # jodi images na deya hoy
        st.error("You must upload 1 image")
    if not selected_option:
        # jodi selected_option e na click kora hoy
        st.error("You must select a difficulty")
    if images and selected_option:
        
        # note er khetre container create
        with st.container(border=True):
            with st.spinner("AI is writting notes for you."):
                st.subheader("Your Note", anchor=False)
            
                # This portion bellow will replaced by API call
                generated_notes=note_generator(pil_images)
                st.markdown(generated_notes)
            
        
        # audio transcript er ekhetre container create
        with st.container(border=True):
            st.subheader("Audio Transcription", anchor=False)
            
            # This portion bellow will replaced by API call
            # st.text("Audio transcription will be shown here")
            with st.spinner("AI is generating the audio transcription."): 
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("**", "")
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("_", "")
                generated_notes = generated_notes.replace("`", "")
                
                generated_notes = (generated_notes
                                        .replace(">", "")
                                        .replace("-", "")
                                        .replace("|", "")
                                        .replace("~", "")
                                        .replace("[", "")
                                        .replace("]", "")
                                    )
                
                audio_transcript=audio_transcription(generated_notes)
                st.audio(audio_transcript)
        
        
        # quiz er ekhetre container create
        with st.container(border=True):
            st.subheader(f"Quiz (Difficulty Level {selected_option})", anchor=False)
            
            # This portion bellow will replaced by API call
            # st.markdown("Note will be shown here")
            
            with st.spinner("AI is generating the quizzes."):
                quiz_generate=quiz_generator(pil_images, selected_option)  
                st.markdown(quiz_generate)
            