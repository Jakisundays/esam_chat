import os
import shutil
import streamlit as st
import fitz  # PyMuPDF
import PyPDF2
from typing import List, Dict, Union
import re


def extract_pdf_content_by_page(
    file_path: str,
) -> Union[List[Dict[str, Union[str, int]]], str]:
    file_name = file_path.split("/")[-1]
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            page_content: List[Dict[str, Union[str, int]]] = []

            for page_number, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                page_content.append(
                    {
                        "file_name": file_name,
                        "source": page_number + 1,
                        "content": page_text if page_text else "",
                    }
                )

        if not any(page["content"].strip() for page in page_content):
            return []

        return page_content

    except Exception as e:
        st.error(f"Error processing {file_path}: {e}")
        return []


def create_required_folders():
    """Ensure required folders exist."""
    for folder in ["docs", "img_docs", "weird_docs", "correct_docs"]:
        os.makedirs(folder, exist_ok=True)


def convert_pdf_to_images(pdf_path):
    """Convert PDF pages to images using PyMuPDF."""
    try:
        doc = fitz.open(pdf_path)
        displayed_pages: List[bytes] = []

        for page in doc:
            # Render page to an image
            pix = page.get_pixmap(dpi=200)

            # Convert to PNG bytes for Streamlit display
            img_bytes = pix.tobytes("png")
            displayed_pages.append(img_bytes)

        doc.close()
        return displayed_pages

    except Exception as e:
        st.error(f"Error converting PDF to images: {e}")
        return []


def main():
    st.title("PDF Document Classifier")

    # Ensure folders exist
    create_required_folders()

    def natural_sort_key(s):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        return [convert(text) for text in re.split("(-?[0-9]+)", s)]

    pdf_files = sorted(
        [f for f in os.listdir("./docs") if f.endswith(".pdf")], key=natural_sort_key
    )

    st.write(pdf_files)

    if not pdf_files:
        st.warning("No PDF files found in './docs' directory.")
        return

    # Session state to track current file index
    if "current_file_index" not in st.session_state:
        st.session_state.current_file_index = 0

    # Get current file
    current_file = pdf_files[st.session_state.current_file_index]
    file_path = os.path.join("./docs", current_file)

    # Extract PDF content
    pdf_content = extract_pdf_content_by_page(file_path)

    # Convert PDF to images
    pdf_images = convert_pdf_to_images(file_path)

    # Display file details
    st.subheader(f"Current File: {current_file}")

    # Display PDF content and images side by side
    if pdf_content and pdf_images:
        for page, image in zip(pdf_content, pdf_images):
            col1, col2 = st.columns(2)

            with col1:
                st.text_area(f"Page {page['source']} Text", page["content"], height=300)

            with col2:
                st.image(
                    image, caption=f"Page {page['source']} Image", use_column_width=True
                )

    elif pdf_content:
        # If images couldn't be generated, show only text
        for page in pdf_content:
            st.text_area(f"Page {page['source']}", page["content"], height=200)
        st.warning("Could not generate page images.")
    else:
        st.warning("Could not extract content from the PDF.")

    # Move file buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Move to Correct Docs"):
            shutil.move(file_path, f"./correct_docs/{current_file}")
            st.success(f"Moved {current_file} to correct_docs")
            st.session_state.current_file_index += 1
            st.experimental_rerun()

    with col2:
        if st.button("Move to Image Docs"):
            shutil.move(file_path, f"./img_docs/{current_file}")
            st.success(f"Moved {current_file} to img_docs")
            st.session_state.current_file_index += 1
            st.experimental_rerun()

    with col3:
        if st.button("Move to Weird Docs"):
            shutil.move(file_path, f"./weird_docs/{current_file}")
            st.success(f"Moved {current_file} to weird_docs")
            st.session_state.current_file_index += 1
            st.experimental_rerun()

    # Progress tracking
    total_files = len(pdf_files)
    current_index = st.session_state.current_file_index

    st.write(f"Progress: {current_index}/{total_files} files processed")

    # Reset or stop when all files are processed
    if current_index >= total_files:
        st.success("All files have been processed!")


if __name__ == "__main__":
    main()
