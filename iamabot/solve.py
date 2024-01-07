from .agents import (CheckIfImageLooksLikeCaptchaAgent,
                    DecideCaptchaTypeAgent,
                    TextSolveAgent,
                    MathSolveAgent)
from .gemini_core import Generate
import json

art = """
=================================================================================================
 __          ___      .___  ___.         ___         .______     ______   .___________.
|  |        /   \     |   \/   |        /   \        |   _  \   /  __  \  |           |
|  |       /  ^  \    |  \  /  |       /  ^  \       |  |_)  | |  |  |  | `---|  |----`
|  |      /  /_\  \   |  |\/|  |      /  /_\  \      |   _  <  |  |  |  |     |  |     
|  |     /  _____  \  |  |  |  |     /  _____  \     |  |_)  | |  `--'  |     |  |     
|__|    /__/     \__\ |__|  |__|    /__/     \__\    |______/   \______/      |__|     
                                                                                       
Multi-modal LLM Agent Powered Captcha Solver
=================================================================================================
"""
class Solve:
    def __init__(
            self,
            credential_file_path: str,
            project_id: str
    ):
        print(art)
        self.credential_file_path = credential_file_path
        self.project_id = project_id
        self.gemini = Generate(
            project_id=project_id,
            credentials_file_path=credential_file_path
        )

    def load_json(self, response):
        response_str = response[0].content.parts[0].text
        return json.loads(response_str)

    def run(self, image_path: str):
        # Load agents
        agent_1 = CheckIfImageLooksLikeCaptchaAgent()
        agent_2 = DecideCaptchaTypeAgent()
        agent_3 = TextSolveAgent()
        agent_4 = MathSolveAgent()

        print("INFO :: Loaded Agents. Agents Loaded: CheckIfImageLooksLikeCaptchaAgent, DecideCaptchaTypeAgent, "
              "TextSolveAgent, MathSolveAgent")

        print("INFO :: Attempting to decide if image looks like a captcha...")

        agent_1_response = self.gemini.generate(
            prompt=agent_1.base_prompt,
            image_path=image_path,
            max_output_tokens=agent_1.max_output_tokens,
            temperature=agent_1.temperature,
            top_p=agent_1.top_p,
            top_k=agent_1.top_k
        )
        agent_1_response = self.load_json(response=agent_1_response)

        if agent_1_response["content"] is not True:
            raise ValueError("ERROR :: Image does not look like a captcha")

        print("INFO :: Image looks like a captcha. Attempting to decide captcha type...")

        agent_2_response = self.gemini.generate(
            prompt=agent_2.base_prompt,
            image_path=image_path,
            max_output_tokens=agent_2.max_output_tokens,
            temperature=agent_2.temperature,
            top_p=agent_2.top_p,
            top_k=agent_2.top_k
        )
        agent_2_response = self.load_json(response=agent_2_response)

        captcha_type = agent_2_response["content"]

        if captcha_type == 1:
            print("INFO :: Captcha type is text captcha. Proceeding to solve...")
            agent_3_response = self.gemini.generate(
                prompt=agent_3.base_prompt,
                image_path=image_path,
                max_output_tokens=agent_3.max_output_tokens,
                temperature=agent_3.temperature,
                top_p=agent_3.top_p,
                top_k=agent_3.top_k
            )
            solved_response = self.load_json(response=agent_3_response)

        elif captcha_type == 2:
            print("INFO :: Captcha type is math captcha. Proceeding to solve...")
            agent_4_response = self.gemini.generate(
                prompt=agent_4.base_prompt,
                image_path=image_path,
                max_output_tokens=agent_4.max_output_tokens,
                temperature=agent_4.temperature,
                top_p=agent_4.top_p,
                top_k=agent_4.top_k
            )
            math_equation = self.load_json(response=agent_4_response)
            math_equation = math_equation["content"]

            print(f"INFO :: Math equation identified is `{math_equation}`. Attempting to solve this equation...")

            solved_equation = eval(math_equation)
            solved_response = {
                "content": solved_equation
            }
        else:
            raise ValueError("ERROR :: Captcha type not supported. Please try again with a different captcha.")

        return solved_response


if __name__ == '__main__':
    credential_file_path = "credentials/valiant-hub-408607-7cf46f47b53d.json"
    project_id = 1077607249524
    image_path = "sample_captchas/easy_math.jpg"
    run = Solve(
        credential_file_path=credential_file_path,
        project_id=project_id
    )
    response = run.run(image_path=image_path)
    print(response)
