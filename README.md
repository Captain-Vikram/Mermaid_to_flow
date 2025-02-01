# Mermaid Diagram Generator

This repository contains a Python script that converts Mermaid syntax into a high-resolution PNG image using the Mermaid CLI (`mmdc`). The script reads Mermaid code, saves it to a temporary file, and then generates a diagram image with a user-defined scale for the best possible resolution.

## Prerequisites

Before using this project, ensure you have the following installed on your system:

- **Python 3** (tested with Python 3.12)  
  Download from [Python.org](https://www.python.org/downloads/).

- **Node.js and npm**  
  Download the latest LTS version from [Node.js Official Website](https://nodejs.org/).  
  _Make sure npm is included and added to your system's PATH._

- **Mermaid CLI**  
  Install Mermaid CLI globally using npm:
  ```bash
  npm install -g @mermaid-js/mermaid-cli
