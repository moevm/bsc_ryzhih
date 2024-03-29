from quart import Quart, request
from quart_cors import cors
from nextcord.ext import ipc

app = Quart(__name__)
app = cors(app, allow_origin="*")
ipc_client = ipc.Client(secret_key="secret1234", host="bot", port=8760)  # secret_key must be the same as your server

@app.route('/')
async def hello():
    return "Hello"


@app.route("/members")
async def members():
    member_count = await ipc_client.request("get_member_count", guild_id=1001473537451761664)
    return str(member_count)


@app.route("/generate_message", methods=['POST', 'GET', 'OPTIONS'], strict_slashes=False)
async def generate_message():
    if request.method != 'POST':
        print("Not post")
        return {"members": ["3", "4"]}
    req = await request.json
    channel_name, message_type, repo_name, work = req.values()
    if not work:
        work = None

    response = await ipc_client.request("generate_message", channel_name=channel_name, message_type=message_type,
                                        repo_name=repo_name, work=work)
    print(response)
    return {'ok': [response]}


@app.route("/chat_history", methods=['POST', 'GET', 'OPTIONS'], strict_slashes=False)
async def chat_history():
    if request.method != 'POST':
        print("Not post")
        return {"members": ["3", "4"]}

    req = await request.json
    channel_name, email = req.values()
    # Ошибка
    response = await ipc_client.request("chat_history", channel_name=channel_name, email=email)

    print(response)
    return {'ok': [response]}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
