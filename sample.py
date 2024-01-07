from iamabot import solve

solved_response = solve.Solve(
    project_id=1077607249524,  # Google Project ID with vertex-ai endpoint enabled & access to gemini-vision-pro
    credential_file_path="credentials/valiant-hub-408607-7cf46f47b53d.json" # Service account JSON file with access to vertex-ai endpoints
).run(
    "sample_captchas/text_moderate.png",  # Path to captcha image to solve
)

print(solved_response)
