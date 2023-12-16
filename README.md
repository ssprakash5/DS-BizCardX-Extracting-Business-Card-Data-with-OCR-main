# DS-BizCardX-Extracting-Business-Card-Data-with-OCR
EasyOCR is a Python library for Optical Character Recognition (OCR) that simplifies the process of extracting text from images and scanned documents. It is particularly useful in your project, BizCardX, which focuses on extracting information from business cards. Here's a revised overview of your project with the content presented in a different format:

Project Name: BizCardX - Business Card Data Extraction
![Bizcards](https://github.com/srisuryaprakash55/DS-BizCardX-Extracting-Business-Card-Data-with-OCR/assets/139371882/6d088e92-1abf-4b1d-b463-01ec83acac80)![Bizcards2](https://github.com/srisuryaprakash55/DS-BizCardX-Extracting-Business-Card-Data-with-OCR/assets/139371882/fa9752e2-a471-400c-bd22-058321d31712)


Project Description:
BizCardX is a user-friendly tool designed to extract information from business cards. The tool leverages EasyOCR, an OCR technology, to recognize text on business cards and then classifies and extracts the data into a MySQL database using regular expressions. Users can interact with the extracted information through a streamlined graphical user interface created using Streamlit.

Key Libraries and Modules Used:

Pandas: Used to create a structured DataFrame to manage the extracted data.
mysql.connector: Facilitates the storage and retrieval of data from a MySQL database.
Streamlit: Enables the creation of a user-friendly graphical interface for users.
EasyOCR: Empowers the extraction of text from images, particularly business cards.
Key Features:

Extracts text information from business card images using EasyOCR for accuracy.
Applies OpenCV for image preprocessing, including resizing, cropping, and enhancement.
Utilizes regular expressions (RegEx) to parse and extract specific fields such as name, designation, company, contact details, and more.
Stores the extracted information in a MySQL database, allowing for easy retrieval and analysis.
Offers a user-friendly interface built with Streamlit, allowing users to upload images, extract information, and interact with the database effortlessly.
Workflow:

Library Installation: Start by installing the required libraries using the pip install command: Streamlit, mysql.connector, pandas, and EasyOCR.

css
Copy code
pip install [Library Name]
User-Friendly Interface: The application features three main menu options:  "UPLOAD & EXTRACT," and "DISPLAY." Users can easily navigate and select the relevant functionality.




Image Upload: When a user uploads a business card, EasyOCR is employed to extract the text from the card.

Text Classification: Extracted text is sent to the "get_data()" function, which employs loops and regular expressions to classify the data into categories like company name, cardholder name, designation, contact details, and more.

User Interaction: The classified data is presented on the screen and can be further edited by the user as needed.

Database Integration: Clicking the "Upload to Database" button stores the data in the MySQL database. (Note: You need to provide the host, user, password, and database name in the relevant functions for database connection.)

Data Management: The "MODIFY" menu allows users to access and perform Read, Update, and Delete operations on the data stored in the SQL database.

This project streamlines the process of extracting and managing business card information, offering a convenient and efficient solution for users.
Approach:
1. Install the required packages: You will need to install Python, Streamlit,
easyOCR, and a database management system like SQLite or MySQL.
2. Design the user interface: Create a simple and intuitive user interface using
Streamlit that guides users through the process of uploading the business
card image and extracting its information. You can use widgets like file
uploader, buttons, and text boxes to make the interface more interactive.

3. Implement the image processing and OCR: Use easyOCR to extract the
relevant information from the uploaded business card image. You can use
image processing techniques like resizing, cropping, and thresholding to
enhance the image quality before passing it to the OCR engine.
4. Display the extracted information: Once the information has been extracted,
display it in a clean and organized manner in the Streamlit GUI. You can use
widgets like tables, text boxes, and labels to present the information.
5. Implement database integration: Use a database management system like
SQLite or MySQL to store the extracted information along with the uploaded
business card image. You can use SQL queries to create tables, insert data,
and retrieve data from the database, Update the data and Allow the user to
delete the data through the streamlit UI
6. Test the application: Test the application thoroughly to ensure that it works as
expected. You can run the application on your local machine by running the
command streamlit run app.py in the terminal, where app.py is the name of
your Streamlit application file.
7. Improve the application: Continuously improve the application by adding new
features, optimizing the code, and fixing bugs. You can also add user
authentication and authorization to make the application more secure.
