import athiest
import time as t
import streamlit as st
from colorama import Fore, Style
import religious
athiest_message="Why there are so much Strictness for Women in Islam but not for Men???"
while True:
 religious_message=religious.chat_with_Religious(athiest_message)
 st.write(f"\nReligious Bot: {Fore.GREEN+ religious_message+ Style.RESET_ALL}")
 t.sleep(20)
 athiest_message=athiest.chat_with_athiest(religious_message)
 st.write(f"\nAtheist Bot: {Fore.RED+ athiest_message+Style.RESET_ALL}")
 t.sleep(20)


