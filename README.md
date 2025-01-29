# Full Stack Agent

An interactive command-line tool that streamlines the process of setting up new web applications and API services with modern tech stacks. It automatically generates and executes initialization scripts based on your chosen technologies and system requirements.

## Features ✨

- Interactive project setup wizard
- Support for multiple project types:
  - Web Applications
  - API Services
- Comprehensive tech stack selection
- Real-time system requirement checks
- Automated script generation
- Cross-platform support (Windows, MacOS, Linux)
- Latest best practices integration through Tavily Search
- Smart error handling and validation

## Prerequisites 📋

Before using the Project Initializer, ensure you have:

1. Python 3.7 or higher installed
2. Required API keys:
   - GROQ_API_KEY
   - TAVILY_API_KEY

## Installation 🔧

1. Clone the repository:
```bash
git clone [repository-url]
cd project-initializer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage 💻

1. Run the initializer:
```bash
python main.py
```

2. Follow the interactive prompts to:
   - Enter your project name
   - Select your operating system
   - Choose project type
   - Select desired tech stack
   - Configure additional features

The tool will then:
- Verify system requirements
- Generate appropriate initialization scripts
- Execute the scripts to set up your project

## Supported Technologies 🛠️

### Web Applications
- Frontend:
  - React
  - Vue
  - Angular
  - Svelte
- Backend:
  - Node.js/Express
  - Python3/Flask
  - Python3/Django
  - Python3/FastAPI
- Databases:
  - MongoDB
  - PostgreSQL
  - MySQL
  - SQLite
- Additional Tools:
  - Docker
  - TypeScript
  - Redux
  - GraphQL

### API Services
- Backend:
  - Node.js/Express
  - Python3/FastAPI
  - Python3/Django REST
  - Go/Gin
- Databases:
  - MongoDB
  - PostgreSQL
  - MySQL
  - Redis
- Features:
  - Authentication
  - Swagger/OpenAPI
  - Rate Limiting
  - Caching

## Error Handling 🔍

The tool includes comprehensive error handling for:
- Missing system requirements
- Invalid configurations
- Script execution failures
- API communication issues

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.
