# needs PyGithub
from github import Github

token = "my-token" # replace by actual token
g = Github(token)

repo = g.get_repo("DiegoFrnnds/cook-with-chatGPT-python")

commit_messages = ["Corrigindo um bug", "Adicionando uma nova funcionalidade",
                   "Atualizando a documentação", "Refatorando o código",
                   "Implementando um teste automatizado",
                   "Melhorando a performance"]

import random

num_commits = random.randint(1, 5)

for i in range(num_commits):
    message = random.choice(commit_messages)
    try:
      contents = repo.get_contents("empty_file")
      repo.update_file(contents.path, message, message, contents.sha)
    except:
      repo.create_file("empty_file", message, "")
