class CheckIfImageLooksLikeCaptchaAgent:
    """
    This is A1. Agent to decide if the image is a captcha or not.
    """
    base_prompt: str = """Directive: Read the image below and tell me if the image looks like a captcha or not.

Instruction: Analyze the image attached and tell me if the image looks like a captcha or not.

Response Structure if the image is a captcha: {\"content\": true}
Response Structure if the image is not a captcha: {\"content\": false}

Only return the JSON data. Do not include any JSON indicators such as ```json etc.

Prompt: Does the below image look like a captcha?"""
    max_output_tokens: int = 100
    temperature: float = 0.4
    top_p: int = 1
    top_k: int = 32


class DecideCaptchaTypeAgent:
    """
    This is A2. Agent to decide the type of captcha.
    """
    base_prompt: str = """Directive: Read the image and tell me what is expected of me. 

Instruction: Tell me what my expected action is. The possible outcomes that are expected of me are as follows: 

1) Read the given content. This kind of captcha is basically where we need to enter a series of text and numbers as is into a the provided box
2) Solve the mathematical equation. This kind of captcha is basically where we need to solve a mathematical equation and enter the answer into the provided box
3) Turn an image. This kind of captcha is basically where we need to turn an image to a certain degree and enter the degree into the provided box
4) Solve a puzzle. This kind of captcha is basically where we need to solve a puzzle and enter the answer into the provided box
5) Select Which Of. This kind of captcha is basically where we need to select all images that match a particular description
6) Other

Ensure to only return one of the above option\'s corresponding number. Only one option can be returned.

Do not include any hex content or such.

Response Structure: {\"content\": <option goes here>}

Only return the JSON data. Do not include any JSON indicators such as ```json etc."""
    max_output_tokens: int = 100
    temperature: float = 0.4
    top_p: int = 1
    top_k: int = 32


class TextSolveAgent:
    """
    This is A3. This agent is used to return the text in the image.
    """
    base_prompt: str = """Directive: Read the image and display the content below.

Instruction: Do not return any other text but what is inside the image. Return English text only of what is contained. Do not include any hex content or such.

Response Structure: {\"content\": <text goes here>}

Only return the JSON data. Do not include any json indicators such as ```json etc.

Prompt: Read the following image, and tell me the content in the box"""
    max_output_tokens: int = 100
    temperature: float = 0.4
    top_p: int = 1
    top_k: int = 32


class MathSolveAgent:
    """
    This is A4. This agent is used to return the mathematical equation to solve.
    """
    base_prompt: str = """Directive: Read the image and display the content below.

Instruction: The image_path contains a mathematical equation to evaluate. Read the image and return the math equation that is to be solved. This equation should be evaluatable using Python (programming language).

Response Structure: {\"content\": <equation goes here>}

Only return the JSON data. Do not include any JSON indicators such as ```json etc.

Prompt: Read the following image_path, and tell me the equation in the box"""
    max_output_tokens: int = 100
    temperature: float = 0.4
    top_p: int = 1
    top_k: int = 32
