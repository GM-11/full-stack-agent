PROMPT = '''
Generate an initialization script for a {project_type} project named {project_name}

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
- For web projects: Separate backend/frontend dirs, use npm/vite for frontend
- For API projects: Use appropriate SDK/commands with basic boilerplate

OS-specific requirements:
- Windows: Use PowerShell commands
- Linux/MacOS: Use bash commands

Notes:
- Check prerequisites first
- Initialize backend first if applicable
- Use `npx create-vite frontend --template {frontend_tech} --y` for web frontend
- Ensure script runs without errors
- Use npm/npx only for Javascript projects
- Do not setup eslint or prettier
- Provide script only, no explanations


Output script should be ready to execute assuming all dependencies are installed
'''

MODEL_NAME = "llama-3.3-70b-versatile"
