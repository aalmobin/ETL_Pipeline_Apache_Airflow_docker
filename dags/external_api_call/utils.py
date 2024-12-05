import requests


def fetch_todos(**kwargs):
    res = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos_data = res.json()
    kwargs["ti"].xcom_push(key="todos_data", value=todos_data)
    print(f"{len(todos_data)} todos data pushed to xcom")


def load_todos(**kwargs):
    ti = kwargs["ti"]
    data = ti.xcom_pull(key="todos_data")
    print(f"{len(data)} todos data pulled from xcom ")


def fetch_albums(**kwargs):
    res = requests.get("https://jsonplaceholder.typicode.com/albums/")
    albums_data = res.json()
    kwargs["ti"].xcom_push(key="albums_data", value=albums_data)
    print(f"{len(albums_data)} albums data pushed to xcom")


def load_albums(**kwargs):
    ti = kwargs["ti"]
    data = ti.xcom_pull(key="albums_data")
    print(f"{len(data)} albums data pulled from xcom ")


def fetch_posts(**kwargs):
    res = requests.get("https://jsonplaceholder.typicode.com/posts/")
    posts_data = res.json()
    kwargs["ti"].xcom_push(key="posts_data", value=posts_data)
    print(f"{len(posts_data)} posts data pushed to xcom")


def load_posts(**kwargs):
    ti = kwargs["ti"]
    data = ti.xcom_pull(key="posts_data")
    print(f"{len(data)} posts data pulled from xcom")
