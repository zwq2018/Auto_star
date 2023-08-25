from auto_star import *
import gradio as gr

def auto_star(repos, token):
    urls_list = extract_github_urls(repos)
    results = []
    for url in urls_list:
        owner, repo = parse(url)
        try:
            star_github_repo(token, owner, repo)
            results.append(f"Successfully starred {owner}/{repo}")
        except Exception as e:
            results.append(str(e))
    return "\n".join(results)

def check_stars(repos, your_token, user_id):
    urls_list = extract_github_urls(repos)
    starred_count = 0
    for url in urls_list:
        owner, repo = parse(url)
        if check_star_for_repo(owner, repo, your_token, user_id):
            starred_count += 1
    return f"User {user_id} has starred {starred_count} out of {len(urls_list)} repos."

# Gradio interfaces
def main(action, repos, token, user_id=''):
    if action == "Auto Star Repos":
        return auto_star(repos, token)
    elif action == "Check Starred Repos":
        return check_stars(repos, token, user_id)
    else:
        return "Invalid Action!"

# Custom CSS to make the token input behave like a password field
css = """
input[type="text"].gr-text {
    -webkit-text-security: disc;
}
"""

iface = gr.Interface(
    fn=main,
    inputs=[
        gr.inputs.Dropdown(label="Action", choices=["Auto Star Repos", "Check Starred Repos"]),
        gr.inputs.Textbox(label="Repo List (URLs)", type="text"),
        gr.inputs.Textbox(label="Your token", type="password"),
        gr.inputs.Textbox(label="The User ID your want to check", type="text")
    ],
    outputs="text",
    live=False,  # Turn off live updates
    submit_button=True,  # Add a submit button
    title="GitHub Actions",
    description="Star repositories or check if a user has starred them.",
    css=css
)

iface.launch()