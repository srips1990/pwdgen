# PWDGen


Generate strong passwords using a simple key phrase.
> _Note: The generated passwords are not stored anywhere. Just remember the key phrase._ 

## Installation

### Command-Line Utility

**Step 1.**  Download the Git repository through terminal using the following command:

`git clone https://github.com/srips1990/pwdgen.git`

**Step 2.**  Navigate to the project's root directory using the following command:

`cd pwdgen`

**Step 3.** Execute the following command to build the executable:

`python -m PyInstaller --onefile --name generator generator.py`

**Step 4.** Once the previous command finishes executing, check the `build` directory. 
You should be able to find the executable.
<br /><br />
### GUI

> _Prerequisite: Python3, PIP_

**Step 1.**  Download the Git repository through terminal using the following command:

`git clone https://github.com/srips1990/pwdgen.git`

**Step 2.**  Navigate to the project's root directory using the following command:

`cd pwdgen`

**Step 3.**  Install dependencies using the following command:

`pip install -r requirements.txt`

**Step 4.** Run the GUI application using the following command:

`python generator_app.py`
<br /><br />
## Contributors

[Sripathi Srinivasan](https://sripathi.co.in)