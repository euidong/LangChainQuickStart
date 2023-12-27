from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/category_chain/")
completion = remote_chain.invoke({"text": "colors"})
print(completion)
