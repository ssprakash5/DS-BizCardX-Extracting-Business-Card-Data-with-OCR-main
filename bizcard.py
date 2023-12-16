import streamlit as st
from PIL import Image
import easyocr
import mysql.connector
import numpy as np
import re

# Title and Description
st.title("BizCardX: Business Card Data Extraction")
st.write("Upload a business card image to extract information.")

# File Upload
uploaded_file = st.file_uploader("Upload a Business Card Image", type=["jpg", "png", "jpeg"])
image = None  # Initialize image here

# Initialize dictionaries to store extracted data
data = {
    "website": [],
    "email": [],
    "mobile_number": [],
    "company_name": [],
    "card_holder": [],
    "designation": [],
    "area": [],
    "city": [],
    "state": [],
    "pin_code": []
}

# Establish a database connection
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="bizcards"
    )
    return conn

# Create the business cards table if it doesn't exist
def create_table(conn):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS business_cards (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        role VARCHAR(255),
        mobile_number VARCHAR(255),
        email VARCHAR(255),
        website VARCHAR(255),
        company_name VARCHAR(255),
        address VARCHAR(255),
        city VARCHAR(255),   -- Add city column
        state VARCHAR(255),  -- Add state column
        pin_code VARCHAR(255) -- Add pin_code column
    )
    """
    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()

# Insert business card data into the database
def insert_business_card(conn, data):
    insert_query = """
    INSERT INTO business_cards (name, role, mobile_number, email, website, company_name, address, city, state, pin_code)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = conn.cursor()

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        st.success("Data inserted successfully!")
    except Exception as e:
        st.error(f"Error inserting data: {str(e)}")

# Define the display_business_cards function to retrieve and display business card data
def display_business_cards(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM business_cards"
    cursor.execute(query)
    data = cursor.fetchall()

    if data:
        st.header("Business Cards")
        st.table(data)

# Function to extract data from the uploaded image
def extract_data_from_image(image):
    # Create an easyOCR reader
    reader = easyocr.Reader(['en'], gpu=False)

    # Convert PIL image to NumPy array
    img_np = np.array(image)

    # OCR extraction
    extracted_data = reader.readtext(img_np)

    return extracted_data

# Initialize extracted_data outside the button click event
extracted_data = []

# Streamlit UI
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.resize((800, 600))
    st.image(image, use_column_width=True)

    # Button to Extract Information
    if st.button("Extract Information"):
        # Extract data from the image
        extracted_data = extract_data_from_image(image)

        if extracted_data:
            st.header("Extracted Information")

            def get_data(res):
                mobile_numbers = []  # To store all mobile numbers found in the text

                for i in res:
                    text = i[1]  # Get the text from the extraction result

                    # To get MOBILE NUMBER
                    # Regular expression to match mobile numbers in the specified format
                    mobile_matches = re.findall(r'\+\d{2,3}-\d{3}-\d{4}', text)

                    if mobile_matches:
                        mobile_numbers.extend(mobile_matches)

                    # To get EMAIL ID
                    if "@" in text:
                        data["email"].append(text)

                    # To get WEBSITE
                    if "www" in text.lower() or "http" in text.lower():
                        data["website"].append(text)

                    # You can also include any other logic you need for email and website here

                    # To get COMPANY NAME
                    elif i == res[-1]:
                        data["company_name"].append(text)

                    # To get CARD HOLDER NAME
                    elif i == res[0]:
                        data["card_holder"].append(text)

                    # To get DESIGNATION
                    elif i == res[1]:
                        data["designation"].append(text)

                    # To get AREA
                    if re.search(r'^\d+.+, [a-zA-Z]+', text):
                        data["area"].append(text.split(',')[0])
                    elif re.search(r'\d+ [a-zA-Z]+', text):
                        data["area"].append(text)

                    # To get CITY NAME
                    match1 = re.search(r'.+St, ([a-zA-Z]+).+', text)
                    match2 = re.search(r'.+St,, ([a-zA-Z]+).+', text)
                    match3 = re.search(r'^[E].*', text)
                    if match1:
                        data["city"].append(match1.group(1))
                    elif match2:
                        data["city"].append(match2.group(1))
                    elif match3:
                        data["city"].append(match3.group(0))

                    # To get STATE
                    state_match = re.search(r'[a-zA-Z]{9} \d', text)
                    if state_match:
                        data["state"].append(text[:9])
                    elif re.search(r'^\d+.+, ([a-zA-Z]+);', text):
                        data["state"].append(text.split()[-1])
                    if len(data["state"]) == 2:
                        data["state"].pop(0)

                    # To get PINCODE
                    if len(text) >= 6 and text.isdigit():
                        data["pin_code"].append(text)
                    elif re.search(r'[a-zA-Z]{9} \d', text):
                        data["pin_code"].append(text[10:])

                # Combine mobile numbers into a single string with comma separation
                if mobile_numbers:
                    data["mobile_number"] = ",".join(mobile_numbers)

            get_data(extracted_data)

            # Insert the extracted data into the database
            conn = create_connection()
            create_table(conn)

            # Replace this with the actual extracted data from the business card
            sample_data = [
                data["card_holder"][0] if data["card_holder"] else "",
                data["designation"][0] if data["designation"] else "",
                data["mobile_number"] if data["mobile_number"] else "",
                data["email"][0] if data["email"] else "",
                data["website"][0] if data["website"] else "",
                data["company_name"][0] if data["company_name"] else "",
                data["area"][0] if data["area"] else "",
                data["city"][0] if data["city"] else "",
                data["state"][0] if data["state"] else "",
                data["pin_code"][0] if data["pin_code"] else ""
            ]

            insert_business_card(conn, sample_data)

# Button to display extracted data
if st.button("Show Extracted Data"):
    st.header("Extracted Information")

    def get_data(res):
        for i in res:
            st.write(i)

    get_data(extracted_data)

# Footer or additional information
st.write("BizCardX - Your Business Card Information Extractor")

# Display the business card data from the database
if st.button("Display Business Cards"):
    conn = create_connection()
    display_business_cards(conn)
