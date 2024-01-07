from google.oauth2 import service_account
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, Image


class Generate:
    def __init__(self,
                 project_id: int,
                 credentials_file_path: str = None,
                 credentials_file_content: str = None
                 ):

        self.project_id = project_id

        if not credentials_file_path and not credentials_file_content:
            raise ValueError("Either credentials_file_path or credentials_file_content must be provided")

        if credentials_file_path and credentials_file_content:
            raise ValueError("Only one of credentials_file_path or credentials_file_content must be provided")

        if credentials_file_path:
            credentials = service_account.Credentials.from_service_account_file(
                credentials_file_path
            )

        elif credentials_file_content:
            credentials = service_account.Credentials.from_service_account_info(
                credentials_file_content
            )
        vertexai.init(
            project=project_id,
            credentials=credentials
        )

    def generate(
            self,
            prompt: str,
            image_path: str = None,
            max_output_tokens: int = 2048,
            temperature: float = 0.4,
            top_p: int = 1,
            top_k: int = 32
    ):
        model = GenerativeModel("gemini-pro-vision")
        contents = [
            prompt
        ]
        if image_path:
            image = Image.load_from_file(image_path)
            contents.append(image)

        generation_config = {
            "max_output_tokens": max_output_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k
        }
        responses = model.generate_content(
            contents,
            generation_config=generation_config,
            # stream=True, # Commenting out stream since the application runs synchronously.
        )
        return responses.candidates


if __name__ == '__main__':
    prompt = """Directive: Read the image_path and display the content below.
    
    Instruction: The image_path contains a mathematical equation to evaluate. Read the image_path and return the math equation that is to be solved. This equation should be evaluatable using Python (programming language).
    
    Response Structure: {\"content\": <equation goes here>}
    
    Only return the JSON data. Do not include any JSON indicators such as ```json etc.
    
    Prompt: Read the following image_path, and tell me the equation in the box"""

    z = Generate(
        project_id=1077607249524,
        credentials_file_path="valiant-hub-408607-7cf46f47b53d.json"
    ).generate(
        prompt=prompt, image_path="Okta-Captcha.png"
    )
    print(z)
