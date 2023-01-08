import pyttsx3, PyPDF2

filename = 'Leinasaar_cover_letter.pdf'

pdf_reader = PyPDF2.PdfReader(open(filename, 'rb'))
voice = pyttsx3.init()



to_transform = ''' '''
for num_page in range(len(pdf_reader.pages)):
    print(f"Current page is {num_page}")
    content = pdf_reader.pages[num_page].extract_text()
    cleaned_content = content.strip().replace('\n', ' ')
    to_transform += cleaned_content
    
voice.save_to_file(to_transform, 'audio_f.mp3')
voice.runAndWait()

voice.stop()

