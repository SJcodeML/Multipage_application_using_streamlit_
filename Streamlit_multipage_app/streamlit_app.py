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

# # # run navigation 
# pg.run()/




# -------------------
# import streamlit as st  
# from views import about_me, sales_dashboard, chat_bot  

# # Set the page config to include a title  
# st.set_page_config(page_title="My Multipage App")  

# # Create a sidebar for navigation  
# pages = {  
#     "About Me": about_me,  
#     "Sales Dashboard": sales_dashboard,  
#     "Chat Bot": chat_bot  
# }  

# selected_page = st.sidebar.selectbox("Select a Page", list(pages.keys()))  

# # Run the selected page's app function  
# pages[selected_page].app()  

