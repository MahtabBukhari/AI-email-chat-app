



import streamlit as st
import time
from llama_hub.tools.gmail.base import GmailToolSpec
from llama_index.agent import OpenAIAgent
from dotenv import load_dotenv
import openai
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

tool_spec = GmailToolSpec()
agent = OpenAIAgent.from_tools(tool_spec.to_tool_list(), verbose=True)

st.title("Email Drafting and Sending")

def send_email(draft, page):
    with st.spinner("Sending email..."):
        try:
            if page:
                st.session_state.page = page
            # Send the email using the agent
            time.sleep(25)
            agent.chat(f"send the draft email {draft}")
            st.success("Email sent successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")

def update_draft(page, pre_draft):
    try:
        st.session_state.page = page
        if pre_draft:
            st.session_state.draft_id = pre_draft
    except Exception as e:
        st.error(f"Failed to update draft: {e}")

if "page" not in st.session_state:
    st.session_state.page = 1  # Set initial page

page = st.session_state.page

with st.container():
    if page == 1:
        st.title("Page 1")
        user_query = st.text_input("Enter your query to create an email:")
        submit_query_button = st.button("Submit Query")
        
        if submit_query_button:
            with st.spinner("Creating draft..."):
                try:
                    # Create the email draft using the agent
                    agent.chat(f"create email according to the user query the user query is: {user_query}")
                    time.sleep(25)  # Adjust delay as needed
                    draft = agent.chat("display the draft")
                    response = draft.response
                    time.sleep(5)
                    # Display the draft to the user
                    save_draft = draft.sources[0]
                    # st.write("Email Draft:")
                    st.write(response)
                    sendMail, updateDraft = st.columns(2)
                    sendMail.button("Send Email", on_click=send_email, args=(draft,1,))
                    updateDraft.button("Update Draft", on_click=update_draft, args=(2, save_draft,))
                except Exception as e:
                    st.error(f"Failed to create draft: {e}")
        
    if page == 2:
        st.title("Page 2")
        update_query = st.text_input("Enter your query to update the draft:")
        update_submit_button = st.button("Submit Update")

        if update_submit_button:
            with st.spinner("Updating draft..."):
                try:
                    # Update the draft using the agent
                    pre_draft = st.session_state.draft_id
                    time.sleep(25)
                    agent.chat(f"change some changes in this draft {pre_draft} as {update_query} ")

                    time.sleep(25)
                    updated_draft = agent.chat(f"display the draft")
                    time.sleep(5)
                    st.write("Updated Draft:")
                    st.write(updated_draft.response)
                    st.session_state.draft_id = updated_draft.sources[0]
                    save_draft = updated_draft.sources[0]
                    sendMail, updateDraft = st.columns(2)
                    sendMail.button("Send Mail", on_click=send_email, args=(updated_draft, 1,))
                    updateDraft.button("Update Draft", on_click=update_draft, args=(2, save_draft,))
                except Exception as e:
                    st.error(f"Failed to update draft: {e}")























# import streamlit as st
# import time
# from llama_hub.tools.gmail.base import GmailToolSpec
# from llama_index.agent import OpenAIAgent
# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key

# tool_spec = GmailToolSpec()
# agent = OpenAIAgent.from_tools(tool_spec.to_tool_list(), verbose=True)


# st.title("Email Drafting and Sending")

# def send_email(draft,page):
#      with st.spinner("Sending email..."):
#         if page:
#             st.session_state.page = page
#         # Send the email using the agent
#         time.sleep(20)
#         try:
#             agent.chat(f"send the draft email {draft}")
#             st.success("Email sent successfully!")
#         except Exception as e:
#             st.error("Failed to send email:", e)

# def update_draft(page,pre_draft):
#      st.session_state.page = page
#      if pre_draft:
#          st.session_state.draft_id=pre_draft


# if "page" not in st.session_state:
#     st.session_state.page = 1  # Set initial page

# page = st.session_state.page

# with st.container():
#     if page == 1:
#         st.title("Page 1")
#         user_query = st.text_input("Enter your query to create an email:")
#         submit_query_button = st.button("Submit Query")
#         if submit_query_button:
            
#             with st.spinner("Creating draft..."):
#                 # Create the email draft using the agent
#                 agent.chat(f"create email according to the user query the user query is: {user_query}")
#                 time.sleep(25)  # Adjust delay as needed
#                 draft = agent.chat("display the draft")
#                 response = draft.response
#                 time.sleep(5)
#                 # Display the draft to the user
#                 save_draft = draft.sources[0]
#                 # st.write("Email Draft:")
#                 st.write(response)
#                 sendMail, updateDraft = st.columns(2)
#                 sendMail.button("Send Email",on_click=send_email, args=(draft,))
#                 updateDraft.button("Update Draft",on_click=update_draft, args=(2,save_draft,))
           
        
               
        

#     if page == 2:
#         st.title("Page 2")
#         update_query = st.text_input("Enter your query to update the draft:")
#         update_submit_button = st.button("Submit Update")


#         if update_submit_button:
#             with st.spinner("Updating draft..."):
#                 # Update the draft using the agent
#                     pre_draft = st.session_state.draft_id
#                     time.sleep(20)
#                     agent.chat(f"change some changes in this draft {pre_draft} as {update_query} ")

#                     time.sleep(25)
#                     updated_draft = agent.chat(f"display the draft")
#                     time.sleep(5)
#                     st.write("Updated Draft:")
#                     st.write(updated_draft.response)
#                     st.session_state.draft_id = updated_draft.sources[0]
#                     save_draft =updated_draft.sources[0]
#                     sendMail, updateDraft = st.columns(2)
#                     sendMail.button("Send Mail",on_click=send_email, args=(updated_draft,1,))
#                     updateDraft.button("Update Draft",on_click=update_draft, args=(2,save_draft,))


