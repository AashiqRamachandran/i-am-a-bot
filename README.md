# Multi Modal LLM Powered Captcha Solver

![Demo Gif](https://raw.githubusercontent.com/AashiqRamachandran/i-am-a-bot/main/demo.gif)

This project provides a solution for automatically solving various types of CAPTCHAs using a multi-modal Large Language Model (LLM). It leverages the capabilities of Google's Vertex AI and a custom set of agents to interpret and solve CAPTCHA challenges.

## Features

- Identification of whether an image is a CAPTCHA.
- Determination of CAPTCHA type (text, math equation, image rotation, puzzle, image selection, etc.).
- Solving text and mathematical CAPTCHAs.
- Integration with Google Cloud's Vertex AI for model inference (Using gemini-vision-pro).

## Installation

Before you can use the CAPTCHA solver, you need to install the required dependencies:

```bash
pip install --upgrade google-cloud-aiplatform
```


## Usage

To use the CAPTCHA solver, you need to have a Google Cloud project with Vertex AI enabled and a service account with access to Vertex AI endpoints.

### Example
```python
from iamabot import solve
# Initialize the solver with your Google Cloud project ID and service account credentials
solver = solve.Solve(
project_id=1077607249524,
credential_file_path="google-service-account-credential-file.json"
)
# Run the solver on a CAPTCHA image
solved_response = solver.run("sample_captchas/text_moderate.png")
# Print the solution
print(solved_response)
```


## Project Structure

- `agents.py`: Contains the definitions of the agents used to identify and solve CAPTCHAs.
- `gemini_core.py`: Handles the interaction with Google Cloud's Vertex AI to process the CAPTCHA images.
- `solve.py`: The main entry point for the CAPTCHA solver. It orchestrates the process of solving a CAPTCHA using the defined agents.
- `sample.py`: An example script demonstrating how to use the CAPTCHA solver.

## Agents

The project defines four agents, each with a specific role in the CAPTCHA solving process:

1. `CheckIfImageLooksLikeCaptchaAgent`: Determines if an image is a CAPTCHA.
2. `DecideCaptchaTypeAgent`: Identifies the type of CAPTCHA presented.
3. `TextSolveAgent`: Solves CAPTCHAs that require text recognition.
4. `MathSolveAgent`: Solves CAPTCHAs that present a mathematical equation.

## Configuration

To configure the CAPTCHA solver, you must provide your Google Cloud project ID and the path to your service account JSON file. These are used to authenticate with Google Cloud's Vertex AI service.

## Flow Of The Tool

```
+-----------------------------------+
| Start run function                |
+-----------------------------------+
          |
          v
+-----------------------------------+
| Load Agents                       |
+-----------------------------------+
          |
          v
+-----------------------------------+
| Generate prompt for image check   |
+-----------------------------------+
          |
          v
+-----------------------------------+
| Check if image looks like captcha |
+-----------------------------------+
          |
          +--------------------------+ No
          |                          |
         Yes                         v
          |                  +-------------------+
          v                  | Raise ValueError  |
+-----------------------------------+            |
| Generate prompt for captcha type  |            |
+-----------------------------------+            |
          |                                      |
          v                                      |
+-----------------------------------+            |
| Determine captcha type            |            |
+-----------------------------------+            |
          |                                      |
          +----------+------------+              |
          |          |            |              |
          v          v            |              |
+---------+--+   +---+---------+  |              |
| Text captcha|  | Math captcha|  |              |
+---------+--+   +---+---------+  |              |
          |          |            |              |
          v          v            |              |
+---------+--+   +---+---------+  |              |
| Solve text |   | Solve math  |  |              |
| captcha    |   | captcha     |  |              |
+---------+--+   +---+---------+  |              |
          |          |            |              |
          v          v            |              |
+---------+--+   +---+---------+  |              |
| Return text |  | Return math |  |              |
| captcha     |  | captcha     |  |              |
| solution    |  | solution    |  |              |
+---------+--+   +---+---------+  |              |
          |          |            |              |
          +----------+------------+              |
                     |                           |
                     +---------------------------+
                     |
+--------------------v-----------------------------+
| Raise ValueError if captcha type is unsupported  |
+--------------------------------------------------+
                    |
                    v
+-----------------------------------+
|           End run function        |
+-----------------------------------+
```

## Limitations

The current implementation supports text and mathematical CAPTCHAs. Other types of CAPTCHAs, such as image rotation, puzzles, and image selection, are recognized but not solved in this version.

## Contributing

Contributions to the project are welcome. Please ensure that any pull requests or issues are clear and concise for efficient collaboration.

## License

This project is licensed under the MIT License - see the LICENSE file for details.