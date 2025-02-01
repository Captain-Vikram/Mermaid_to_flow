import subprocess
import os

def mermaid_to_image(mermaid_code, output_filename="flowchart.png", scale=2):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the file paths in the same folder as the script
    diagram_path = os.path.join(script_dir, "diagram.mmd")
    output_path = os.path.join(script_dir, output_filename)
    
    # Save the mermaid code to the diagram file
    with open(diagram_path, "w") as file:
        file.write(mermaid_code)
    
    # Build the command string with the scale parameter for higher resolution
    command = f'mmdc -i "{diagram_path}" -o "{output_path}" --scale {scale}'
    
    try:
        # Use shell=True so that the command is resolved via the system PATH
        subprocess.run(command, shell=True, check=True)
        print(f"Diagram saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print("Error generating the image:", e)

# Example Mermaid Syntax
mermaid_code = """
graph TB
    subgraph Client
        A[User Browser/Extension]
        B[Video Conference]
    end

    subgraph Frontend["Frontend (Next.js)"]
        C[Authentication]
        D[Dashboard]
        E[Interview Interface]
        F[WebSocket Client]
    end

    subgraph Backend["Backend (FastAPI)"]
        G[API Gateway]
        H[WebSocket Server]
        I[AI Pipeline]
        J[Google API Manager]
    end

    subgraph AI["AI Services"]
        K[LLaMA 3.1]
        L[Pypaz Emotion]
        M[Whisper.cpp]
    end

    subgraph External["External Services"]
        N[Google Meet]
        O[Google Drive]
        P[Google OAuth]
    end

    subgraph Database
        Q[(PostgreSQL/MongoDB)]
    end

    %% Client Connections
    A -->|Auth| C
    A -->|Video Feed| B
    A -->|Stream to Backend| H
    B -->|Live Preview| E

    %% Frontend Flow
    C -->|Verify| P
    D -->|Fetch Data| G

    %% Backend Processing
    H -->|Process| I
    I -->|Questions| K
    I -->|Emotions| L
    I -->|Transcription| M

    %% External Integration
    J -->|Create Meeting| N
    J -->|Store Data| O
    J -->|Auth| P

    %% Data Storage
    G -->|CRUD| Q
    I -->|Store Analysis| Q
"""

print("Generating single mermaid chart")
mermaid_to_image(mermaid_code, "flowchart.png", scale=10)
