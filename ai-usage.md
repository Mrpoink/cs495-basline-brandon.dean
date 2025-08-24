Most often, I use Google's Gemini as a glorified Google Search since it can summarize and condense Google Search results within seconds. I do still usually look at program documentation as it is usually more specific to my use cases, plus I don't like being fed information unwillingly. 

I did use Gemini for two things, and these were the prompts and responses:
Input: 
"I want to make a python function that has two input variables, however i want the function to have the ability to be called with the option of not including the second var. For example:



def function(var1, var2)



function(var1) -> output

function(var1, var2) -> different output"

Output: 
"Of course. You can achieve this by setting a default value for the second variable. A common practice is to set the default value to None.

Here's how you can do it:

Python

def my_function(var1, var2=None):
  """
  This function provides different outputs based on whether
  one or two arguments are provided.
  """
  if var2 is None:
    # This code runs if only var1 is provided
    return f"You only provided one variable: {var1}"
  else:
    # This code runs if both var1 and var2 are provided
    return f"You provided two variables: {var1} and {var2}"

# --- Examples ---

# Calling with one variable
output1 = my_function(1068) 
print(output1)
# Expected Output: You only provided one variable: 1068

# Calling with two variables
output2 = my_function(10, 20)
print(output2)
# Expected Output: You provided two variables: 10 and 20
Explanation
By defining the function as def my_function(var1, var2=None):, you are telling Python that var2 is an optional argument. If the caller doesn't provide a value for var2, Python will automatically assign it the default value of None.

Inside the function, the if var2 is None: check allows you to determine which way the function was called and then execute the appropriate logic."


Second was actually a Google search; however, it did give me an AI response:

"how to have a python file run on github"
https://www.google.com/search?q=how+to+have+a+python+file+run+on+github&oq=how+to+have+a+python+file+run+on+github&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyCggGEAAYgAQYogQyCggHEAAYgAQYogTSAQg1NjE2ajBqNKgCA7ACAfEFAXvRVsYfVdLxBQF70VbGH1XS&sourceid=chrome&ie=UTF-8

Output:
Running a Python file on GitHub typically refers to executing it within the GitHub ecosystem, rather than simply storing it. There are several ways to achieve this:
1. Using GitHub Actions:
GitHub Actions provide a powerful way to automate workflows directly within your repository. You can configure a workflow to run your Python script under specific conditions (e.g., on a push to a branch, on a schedule).
Create a workflow file:
.
In your repository, create a directory .github/workflows and add a YAML file (e.g., main.yml) inside it.
Define the workflow:
.
In the YAML file, specify the trigger (e.g., on: push), the environment (e.g., runs-on: ubuntu-latest), and the steps to execute.
Run the Python script:
.
Use the actions/setup-python action to set up Python, install any necessary dependencies using pip, and then execute your Python script using a run step.
Example main.yml snippet:
Code

name: Run Python Script

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x' # Specify your Python version
    - name: Install dependencies
      run: pip install -r requirements.txt # If you have a requirements file
    - name: Run Python script
      run: python your_script.py
2. Using GitHub Codespaces:
GitHub Codespaces provide a cloud-based development environment directly within your browser. You can launch a codespace for your repository, which comes with a pre-configured environment including Python.
Open in Codespaces:
Navigate to your repository on GitHub and click the "Code" button, then select "Open with Codespaces".
Run your script:
Once the codespace is launched, you'll have a terminal where you can navigate to your project directory and run your Python script using python your_script.py.
3. Running Python Notebooks with Google Colab:
If your Python code is within a Jupyter Notebook (.ipynb file), you can directly open and run it in Google Colab from GitHub.
Open in Colab: Go to Google Colab, select "File" -> "Open notebook", then choose the "GitHub" tab and paste the URL of your GitHub repository or the specific notebook file.
Execute cells: Once opened in Colab, you can run individual cells or the entire notebook.
4. Local Execution after Cloning/Downloading:
While not "running on GitHub" directly, the most common way to run a Python file from GitHub is to first get it onto your local machine.
Clone or Download:
.
Clone the repository using git clone <repository_url> or download the repository as a ZIP file.
Install Python:
.
Ensure you have Python installed on your local machine.
Install Dependencies:
.
If the project has a requirements.txt file, install the dependencies using pip install -r requirements.txt.
Run the script:
.
Navigate to the project directory in your terminal or command prompt and run the Python script using python your_script.py."












Tools

"
