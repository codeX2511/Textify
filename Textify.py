import streamlit as st
import re

# Page settings
st.set_page_config(
    page_title="Textify - Text Tools",
    page_icon="📝",
    layout="centered"
)

# Clear function
def clear_text():
    st.session_state.text_input = ""

# Heading
st.title("📝 Textify")
st.subheader("Your Smart Text Tools Application")
st.write("Transform, Analyze and Manage Your Text Easily!")

st.divider()

# Text input
st.subheader("Enter Your Text")

if "text_input" not in st.session_state:
    st.session_state.text_input = ""

text = st.text_area(
    "Type or Paste Your Text Here",
    key="text_input",
    height=180
)

# Tool selection
st.subheader("Choose Your Text Tool")

tool = st.selectbox(
    "Select Operation",
    [
        "Uppercase",
        "Lowercase",
        "Title Case",
        "Sentence Case",
        "Reverse Text",
        "Word Count",
        "Character Count",
        "Character Count (Without Spaces)",
        "Vowel Count",
        "Consonant Count",
        "Palindrome Checker",
        "Find and Replace",
        "Remove Extra Spaces"
    ]
)

result = ""

# Find and Replace inputs
find_word = ""
replace_word = ""

if tool == "Find and Replace":
    find_word = st.text_input("Find Word")
    replace_word = st.text_input("Replace With")

# Process button
if st.button("✨ Process Text", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text first!")

    else:

        if tool == "Uppercase":
            result = text.upper()

        elif tool == "Lowercase":
            result = text.lower()

        elif tool == "Title Case":
            result = text.title()

        elif tool == "Sentence Case":
            result = text.capitalize()

        elif tool == "Reverse Text":
            result = text[::-1]

        elif tool == "Word Count":
            result = str(len(text.split()))

        elif tool == "Character Count":
            result = str(len(text))

        elif tool == "Character Count (Without Spaces)":
            result = str(len(text.replace(" ", "").replace("\n", "")))

        elif tool == "Vowel Count":
            result = str(sum(1 for c in text.lower() if c in "aeiou"))

        elif tool == "Consonant Count":
            result = str(sum(
                1 for c in text.lower()
                if c.isalpha() and c not in "aeiou"
            ))

        elif tool == "Palindrome Checker":
            clean_text = re.sub(r"[^a-z0-9]", "", text.lower())

            if clean_text == clean_text[::-1]:
                result = "Yes! This is a Palindrome."
            else:
                result = "No! This is not a Palindrome."

        elif tool == "Find and Replace":
            if not find_word:
                st.warning("Please enter the word to find.")
            else:
                result = text.replace(find_word, replace_word)

        elif tool == "Remove Extra Spaces":
            result = " ".join(text.split())

        # Save result
        if result != "":
            st.session_state.result = result
            st.success("Text processed successfully!")

# Display result
if "result" in st.session_state:

    st.divider()
    st.subheader("📋 Result")

    st.text_area(
        "Processed Text",
        value=st.session_state.result,
        height=150
    )

    # Copy-friendly output
    st.code(st.session_state.result, language=None)

    # Download TXT
    st.download_button(
        label="⬇️ Download TXT",
        data=st.session_state.result,
        file_name="Textify_Result.txt",
        mime="text/plain",
        use_container_width=True
    )

# Clear button
st.divider()

st.button(
    "🗑️ Clear All",
    on_click=clear_text,
    use_container_width=True
)

st.caption("© 2026 Textify | Created by Gayatri ❤️")
