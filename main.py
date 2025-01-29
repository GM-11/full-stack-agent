import os
import inquirer
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import shutil
import json
from dotenv import load_dotenv
import subprocess
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import Tool
import datetime

from constants import PROMPT, MODEL_NAME


class ProjectInitializer:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Initialize Groq with API key
        groq_api_key = os.getenv('GROQ_API_KEY')
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        tavily_api_key = os.getenv('TAVILY_API_KEY')
        if not tavily_api_key:
            raise ValueError("TAVILY_API_KEY not found in environment variables")

        self.model = ChatGroq(model=MODEL_NAME)
        self.project_type = None
        self.tech_stack = {}
        self.system_requirements = {}
        self.search_tool = TavilySearchResults(max_results=1)

    def get_operating_system(self):
        """Ask user for their operating system."""
        questions = [
                inquirer.List('os',
                             message="What operating system are you using?",
                             choices=['Linux', 'MacOS', 'Windows'],
                             ),
            ]
        answers = inquirer.prompt(questions)
        if answers is None:
            raise ValueError("Operating system must be selected")
        return answers['os']

    def get_latest_tech_info(self, tech_name):
        """Fetch latest initialization methods and best practices for a technology."""
        current_year = datetime.datetime.now().year
        query = f"latest way to initialize {tech_name} project {current_year} best practices setup guide"

        try:
            search_results = self.search_tool.invoke(query)
            print(search_results)

            # If search_results is a string, return it as a single item in a list
            if isinstance(search_results, str):
                return [search_results]

            # If it's a list of dictionaries
            formatted_results = []
            if isinstance(search_results, list):
                for result in search_results:
                    if isinstance(result, dict):
                        content = result.get('content', '') or result.get('snippet', '')
                        if content:
                            formatted_results.append(content)
                    elif isinstance(result, str):
                        formatted_results.append(result)

            return formatted_results if formatted_results else [f"No detailed information found for {tech_name}"]

        except Exception as e:
            print(f"Warning: Could not fetch latest info for {tech_name}: {str(e)}")
            return []

    def check_command_exists(self, command):
        """Check if a command exists in the system."""
        return shutil.which(command) is not None

    def get_project_name(self):
        """Ask user for project name."""
        questions = [
            inquirer.Text('name',
                         message="What is your project name?",
                         validate=lambda _, x: len(x) > 0)
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            raise ValueError("Project name cannot be empty")
        return answers['name']

    def get_project_type(self):
        """Ask user for project type."""
        questions = [
            inquirer.List('type',
                         message="What type of project do you want to create?",
                         choices=['Web Application', 'API Service'],
                         ),
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            raise ValueError("Project name cannot be empty")
        self.project_type = answers['type']

    def get_tech_stack(self):
        """Get technology stack based on project type."""
        questions = []  # Initialize questions list
        if self.project_type == 'Web Application':
            questions = [
                inquirer.List('frontend',
                             message="Choose frontend framework:",
                             choices=['React', 'Vue', 'Angular', 'Svelte'],
                             ),
                inquirer.List('backend',
                             message="Choose backend framework:",
                             choices=['Node.js/Express', 'Python3/Flask', 'Python3/Django', 'Python3/FastAPI', 'None'],
                             ),
                inquirer.List('database',
                             message="Choose database:",
                             choices=['MongoDB', 'PostgreSQL', 'MySQL', 'SQLite', 'None'],
                             ),
                inquirer.Checkbox('additional',
                                message="Select additional tools:",
                                choices=['Docker', 'TypeScript', 'Redux', 'GraphQL', 'None'],
                                ),
            ]
        elif self.project_type == 'API Service':
            questions = [
                inquirer.List('backend',
                             message="Choose backend framework:",
                             choices=['Node.js/Express', 'Python3/FastAPI', 'Python3/Django REST', 'Go/Gin'],
                             ),
                inquirer.List('database',
                             message="Choose database:",
                             choices=['MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'None'],
                             ),
                inquirer.Checkbox('features',
                                message="Select additional features:",
                                choices=['Authentication', 'Swagger/OpenAPI', 'Rate Limiting', 'Caching', 'None'],
                                ),
            ]

        answers = inquirer.prompt(questions)
        self.tech_stack = answers

        print("\n🔍 Fetching latest best practices and initialization methods...")

        self.tech_info = {}

        if self.tech_stack is None:
            return

        for key, value in self.tech_stack.items():
            if isinstance(value, str) and value != 'None':
                print(f"\nFetching information for {value}...")
                self.tech_info[value] = self.get_latest_tech_info(value)
            elif isinstance(value, list):
                for tech in value:
                    print(f"\nFetching information for {tech}...")
                    self.tech_info[tech] = self.get_latest_tech_info(tech)

    def check_system_requirements(self):
        """Check if required tools are installed."""
        requirements = {
            'React': ['node', 'npm'],
            'Vue': ['node', 'npm'],
            'Angular': ['node', 'npm', 'ng'],
            'Svelte': ['node', 'npm'],
            'Node.js/Express': ['node', 'npm'],
            'Python3/Flask': ['python3', 'pip'],
            'Python3/Django': ['python3', 'pip'],
            'Python3/FastAPI': ['python3', 'pip'],
            'Go/Gin': ['go'],
            'MongoDB': ['mongo'],
            'PostgreSQL': ['psql'],
            'MySQL': ['mysql'],
            'Docker': ['docker'],
        }

        missing_requirements = []
        if self.tech_stack is None:
            return missing_requirements

        for tech, tools in self.tech_stack.items():
            if isinstance(tools, list):  # For checkbox selections
                for tool in tools:
                    if tool in requirements:
                        for req in requirements[tool]:
                            if not self.check_command_exists(req):
                                missing_requirements.append(req)
            elif tools in requirements:  # For single selections
                for req in requirements[tools]:
                    if not self.check_command_exists(req):
                        missing_requirements.append(req)

        return list(set(missing_requirements))  # Remove duplicates

    def generate_bash_script(self, project_name, operating_system):
        """Generate script for project initialization based on OS."""
        tech_info_formatted = json.dumps(self.tech_info, indent=2) if hasattr(self, 'tech_info') else "{}"

        prompt = ChatPromptTemplate.from_template(PROMPT)

        chain = prompt | self.model
        if self.tech_stack is None:
            return
        response = chain.invoke({
            "project_type": self.project_type,
            "project_name": project_name,
            "tech_stack": json.dumps(self.tech_stack, indent=2),
            "tech_info": tech_info_formatted,
            "operating_system": operating_system,
            "name": project_name.lower(),
            "frontend_tech": self.tech_stack.get('frontend', '').lower(),
        })

        script = response if isinstance(response, str) else str(response.content) if hasattr(response, 'content') else str(response)
        script = script.replace("```bash", "").replace("```powershell", "").replace("```", "").strip()

        # Choose appropriate file extension based on OS
        file_extension = '.ps1' if operating_system == 'Windows' else '.sh'
        script_filename = f'initialize_project{file_extension}'

        with open(script_filename, 'w') as f:
            if operating_system != 'Windows':
                f.write("#!/bin/bash\n\n")  # Add shebang line for Unix-like systems
                f.write("set -e\n\n")  # Exit on error
            f.write(script)

        # Make the script executable on Unix-like systems
        if operating_system != 'Windows':
            os.chmod(script_filename, 0o755)

        return script_filename

    def run_script(self, script_filename, operating_system):
        """Execute the generated script based on OS."""
        try:
            print("\n🚀 Executing initialization script...")
            if operating_system == 'Windows':
                result = subprocess.run(['powershell', '-File', script_filename],
                                     check=True,
                                     text=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            else:
                result = subprocess.run([f'./{script_filename}'],
                                     check=True,
                                     text=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            print(result.stdout)
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error executing script: {e.stderr}")
            return False
        except Exception as e:
            print(f"\n❌ Unexpected error while executing script: {str(e)}")
            return False

def main():
    print("🚀 Welcome to Project Initializer!")

    try:
        initializer = ProjectInitializer()

        # Get project details
        project_name = initializer.get_project_name()
        operating_system = initializer.get_operating_system()
        initializer.get_project_type()
        initializer.get_tech_stack()

        # Check system requirements
        print("\n🔍 Checking system requirements...")
        missing_reqs = initializer.check_system_requirements()
        if missing_reqs:
            print("\n⚠️  Missing required tools:")
            for req in missing_reqs:
                print(f"- {req}")
            print("\nPlease install the missing requirements and try again.")
            return

        # Generate script
        print("\n📝 Generating initialization script...")
        script_filename = initializer.generate_bash_script(project_name, operating_system)

        success = initializer.run_script(script_filename, operating_system)
        if success:
            print(f"\n✅ Project initialization script has been generated and executed successfully!")
        else:
            print(f"\n❌ An error occurred while executing the script. Please check the output for more information.")

    except ValueError as e:
        print(f"\n❌ Error: {str(e)}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
