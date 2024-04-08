# NL3WangLab Behavioral Questionnaires

### Installation

- Clone the repository

  ```bash
  git clone <repo link>
  ```
- Install the requirements

  ```bash
  # CD (Change Directory) into the Installed Folder (You can type 'cd' then drag and drop the folder into terminal)
    cd {folder_location}
  # Create your virtual environment.
    python3 -m venv .venv
  # Activate your virtual environment.
    source .venv/bin/activate
  # Install the requirements into your virtual environment.
    pip install -r requirements.txt
  ```
- Run the app

  Ensure you're in the project directory. If not, use the cd (change directory) command to move into the Survey Application folder you previously installed. 
- ```bash
  cd {folder_location}
  ```
  Activate the python environment that you installed the requirements to earlier.
- ```bash
  source .venv/bin/activate
  ```
  Run the command below to launch the program.
- ```bash
  python app.py
  ```

  Locate the text similar to what is shown below within your terminal after running the command above. Paste this link into your web browser to load the webpage.
- ```bash
  Running on http://127.0.0.1:5000
  ```

### Result calculation

The logic for the result calculation is implemented in the `app.py` file. The raw submission data as well as calculated results are saved in an excel file in the `static/saves` directory.
