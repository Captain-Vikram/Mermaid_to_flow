import subprocess
import os
import argparse

def mermaid_to_image(mermaid_code, output_filename, scale, diagram_path, mmdc_path):
    """Saves Mermaid code to a file and generates an image using mmdc."""
    with open(diagram_path, "w", encoding="utf-8") as file:
        file.write(mermaid_code)
    
    command = f'"{mmdc_path}" -i "{diagram_path}" -o "{output_filename}" --scale {scale}'
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ Diagram saved as {output_filename}")
    except subprocess.CalledProcessError as e:
        print("❌ Error generating the image:", e)

def main():
    parser = argparse.ArgumentParser(description="Generate a high-resolution Mermaid diagram image.")
    parser.add_argument("--input", "-i", type=str, help="Path to a Mermaid code file. If not provided, you can enter manually.")
    parser.add_argument("--output", "-o", type=str, default="flowchart.png", help="Output image file name (default: flowchart.png)")
    parser.add_argument("--scale", "-s", type=int, default=2, help="Scale factor for image resolution (default: 2)")
    parser.add_argument("--mmdc-path", "-m", type=str, default="mmdc", help="Path to the mmdc executable (default: mmdc, assuming it's in your PATH)")
    args = parser.parse_args()

    # Determine Mermaid Code Source (File or Manual Input)
    if args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as file:
                mermaid_code = file.read()
        except FileNotFoundError:
            print(f"❌ Input file '{args.input}' not found. Please check the path.")
            return
    else:
        print("\n🔹 No input file provided. Please enter your Mermaid code below:\n")
        print("Example Mermaid code format:\n")
        print("""
graph TB
    A[Start] --> B[End]
        """)
        
        # Here we take multi-line input correctly
        print("\nEnter your Mermaid diagram (multi-line):")
        mermaid_code = ""
        while True:
            try:
                # Use input() to take multiple lines of input
                line = input()
                if line == "END":
                    break
                mermaid_code += line + "\n"
            except EOFError:
                break

    # Ask for other details interactively if they are not provided as arguments
    output_filename = args.output if args.output else input("Enter output filename (default: flowchart.png): ") or "flowchart.png"
    scale = args.scale if args.scale else int(input("Enter scale factor (default: 10): ") or 10)
    mmdc_path = args.mmdc_path if args.mmdc_path else input("Enter mmdc path (default: mmdc): ") or "mmdc"

    # Define the working directory and paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    diagram_path = os.path.join(script_dir, "diagram.mmd")

    print("\n🔄 Generating Mermaid chart...")
    mermaid_to_image(mermaid_code, output_filename, scale, diagram_path, mmdc_path)

if __name__ == "__main__":
    main()
