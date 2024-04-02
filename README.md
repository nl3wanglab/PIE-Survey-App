# NL3WangLab Behavioral Questionnaires

### Installation

- Clone the repository

  ```bash
  git clone <repo link>
  ```
- Install the requirements

  ```bash
  # Create your virtual environment.
    python3 -m venv .venv
  # Activate your virtual environment.
    source .venv/bin/activate
  # Install the requirements into your virtual environment.
    pip install -r requirements.txt
  ```
- Run the app

  Be in the root directory of the project and run the following command after activating your virtual environment to start the Flask server.
- ```bash
  python app.py
  ```

  Locate the text similar to what is shown below within your terminal after running the command above. Paste this link into your web browser to utilize this application.
- ```bash
  Running on http://127.0.0.1:5000
  ```

### Result calculation

The logic for the result calculation is implemented in the `app.py` file. The raw and calculated results are saved as an excel file in the `static/saves` directory.
