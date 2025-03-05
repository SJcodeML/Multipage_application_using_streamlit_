import streamlit as st 
# from views import about_me, sales_dashboard, chat_bot  


about_page = st.Page(
    page= "views/about_me.py",
    title = "About Me", 
    icon = ":material/account_circle:",
    default =True,
)
project_1_page = st.Page(
    page= "views/sales_dashboard.py",
    title = "Sales Dashboard", 
    icon = ":material/bar_chart:",
    
)
project_2_page = st.Page(
    page= "views/chat_bot.py",
    title = "Chat bot", 
    icon = ":material/smart_toy:",
  
)


# # # Navigation setup (without sectons)---
pg= st.navigation(pages=[about_page , project_1_page  , project_2_page ])

pg= st.navigation (
    {
        "Info": [about_page],
        "projects" :[project_1_page , project_2_page]
    }
)

# shared on all pages 
st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made by 💖 Sidra Jabin")

# # # run navigation 
pg.run()


 

