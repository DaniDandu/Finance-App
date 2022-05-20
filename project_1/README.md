# Git Clone

Take a git clone by writing the text below in your terminal:
    git clone https://github.com/DaniDandu/ItSchool_myFinance.git
    cd project_1

# Create a Virtual Environment (venv):

    python -m venv venv\Scripts\activate.bat

# Install Packages

To install all the packages by using the requirements file:
    pip install -r requirements.txt

# Start the Server

To start the server:
    go to my_finance file: cd my_finance
    uvicorn index:app --reload --port 7777
