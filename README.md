
# <img src="common/playwright-logo.svg" alt="Playwright Logo" width="50" height="50"> Playwright with <img src="common/py_logo.jpg" alt="Python logo" width="50" height="50"> Python and <img src="common/js_logo.jpg" alt="Python logo" width="50" height="50"> JavaScript

## Steps to get this project set up using VS Code
### Pre-requisites:
- [VS Code installed](https://code.visualstudio.com/download)
- [Latest Python installed](https://www.python.org/downloads/)
- [Git installed](https://git-scm.com/downloads), for Mac [install Homebrew](https://brew.sh/)

### Procedure:
1. Create a folder for the repository
2. Launch VS Code and open folder
3. Clone project and add origin:
    - In VS Code, open new terminal
    - Clone the repository: `git clone https://github.com/MrPRDeltoid/ComeHome_pw_py.git`
    - Switch to directory: `cd ComeHome_pw_py`
    - In terminal, initialize directory for git: `git init -b main`
    - In terminal, connect to origin: `git remote add origin https://github.com/MrPRDeltoid/ComeHome_pw_py.git`
4. Create a new [virtual environment for python](https://code.visualstudio.com/docs/python/environments):
    - Press **Ctrl+Shift+P**/**Cmd+Shift+P** to show Command Palette
    - Search for *Python: Create Environment*
    - Select *Venv* and select version on python
    - A '.venv' folder will be created
5. Install Python extension in VS Code:
    - In VS Code side menu, select Extensions
    - Search for Python
    - Select the **Python** extension and click **install**
6. [Install Playwright for Python](https://playwright.dev/python/docs/intro):
    - Install Playwright pytest: `pip install pytest-playwright` NOTE: May need to use pip3 in Mac
    - Install Playwright browsers: `playwright install`
7. [Install node.js](https://nodejs.org/en/download/package-manager)
8. Install Playwright Test for VSCode extension:
    - In VS Code side menu, select Extensions
    - Search for Playwright
    - Select the **Playwright Test for VSCode** extension and click **install**
9. Install Playwright and browsers for JavaScript:
    - Press **Ctrl+Shift+P**/**Cmd+Shift+P** to show Command Palette
    - Search for *Install Playwright*
    - Select *Test: Install Playwright*
    - Check all the browsers and check **Use JavaScript**
    - Click **OK** and npm will install required packages
10. Add requirements file: `pip freeze > requirements.txt`
11. Run the Tests:
    - Run functional(python) ui tests: `pytest tests_ui/ –headed`
    - Run visual(javascript) tests:
        + In VS Code side menu, select Testing to show list of visual tests
        + At the bottom of the Test Explorer, check Show browser in Settings
        + Click any play button to execute visual tests
        + **NOTE**: The first run of tests will *FAIL*, as that run establishes a base image. Running a second time will perform an image compare to base.
