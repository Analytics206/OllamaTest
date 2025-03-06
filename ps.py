from ollama import ProcessResponse, chat, ps, pull

# Ensure at least one model is loaded
response = pull('llama3.2', stream=True)
progress_states = set()
for progress in response:
  if progress.get('status') in progress_states:
    continue
  progress_states.add(progress.get('status'))
  print(progress.get('status'))

print('\n')

print('Waiting for model to load... \n')
chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])


response: ProcessResponse = ps()
for model in response.models:
  print('Model: ', model.model)
  print('  Digest: ', model.digest)
  print('  Expires at: ', model.expires_at)
  print('  Size: ', f'{model.size / 1024 / 1024:.2f}', "MB")
  print('  Size vram: ', f'{model.size_vram / 1024 / 1024:.2f}', 'MB')
  print('  Details: ', model.details)
  print('\n')