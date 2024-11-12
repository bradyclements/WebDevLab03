def about_me_section():
    st.header("👋 About Me")
    st.image(info.profile_picture, width = 300)
    st.write(info.about_me)
    st.write('---')
about_me_section()
