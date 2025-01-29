PROMPT = '''
"""Generate an initialization script for a {project_type} project named {project_name}

Tech Stack: {tech_stack}
Target OS: {operating_system}
Best Practices Info: {tech_info}

Script Requirements:
1. Create project structure
2. Install dependencies
3. Set up config files
4. Add boilerplate code
5. Include error handling

Project-specific guidelines:
- For web projects: Separate backend/frontend dirs, use yarn/vite for frontend
- For API projects: Use appropriate SDK/commands with basic boilerplate

OS-specific requirements:
- Windows: Use PowerShell commands
- Linux/MacOS: Use bash commands

Notes:
- Check prerequisites first
- Initialize backend first if applicable
- Use `yarn create vite frontend --template {frontend_tech}` for web frontend
- Ensure script runs without errors
- Provide script only, no explanations

Output script should be ready to execute assuming all dependencies are installed"""

'''

MODEL_NAME = "gemma2-9b-it"
