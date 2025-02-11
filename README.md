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

Install directly from PyPI:

```bash
pip install full-stack-agent
```

## Configuration ⚙️

Before first use, set up your API keys:

1. Export as environment variables:
```bash
export GROQ_API_KEY=your_groq_api_key
export TAVILY_API_KEY=your_tavily_api_key
```

OR

2. Create a `.env` file in your working directory:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage 💻

Simply run:
```bash
full-stack-agent
```

Follow the interactive prompts to:
1. Enter your project name
2. Select your operating system
3. Choose project type
4. Select desired tech stack
5. Configure additional features

The tool will automatically:
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

## Troubleshooting 🔧

### Common Issues:

1. **Missing Requirements**
   - Ensure all required tools are installed for your chosen tech stack
   - Verify API keys are properly set in environment or `.env` file

2. **Script Execution Failures**
   - Check system permissions
   - Verify network connectivity for package downloads
   - Ensure no conflicting processes are running

3. **API Related Issues**
   - Verify API key validity
   - Check network connectivity
   - Ensure API service status

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.
