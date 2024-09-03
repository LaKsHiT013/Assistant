import streamlit as st

st.set_page_config(page_title="Assistant", page_icon=":material/edit:")

st.sidebar.title("Your Assistant ready at your Service!")
selection = st.sidebar.radio("",["Personal_Assistant","Image_QA","AskMe","MCQ_Assistant","PDF_Assistant"])

if selection == "Personal_Assistant":
    import Personal_Assistant
    Personal_Assistant.show()
elif selection == "Image_QA":
    import Image_QA
    Image_QA.show()
elif selection == "AskMe":
    import AskMe
    AskMe.show()
elif selection == "PDF_Assistant":
    import PDF_Assist
    PDF_Assist.show()

