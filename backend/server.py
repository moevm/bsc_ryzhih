from quart import Quart, request
from quart_cors import cors
from nextcord.ext import ipc


app = Quart(__name__)
app = cors(app, allow_origin="*")
ipc_client = ipc.Client(secret_key="secret1234", port=8760)  # secret_key must be the same as your server


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
        return {"members" : ["3", "4"]}

    #Ошибка
    guild_count = await ipc_client.request("get_guild_count")

    print(guild_count)
    return {"members": ["5", "6"]}

@app.route("/chat_history", methods=['POST', 'GET', 'OPTIONS'], strict_slashes=False)
async def chat_history():
    if request.method != 'POST':
        print("Not post")
        return {"members" : ["3", "4"]}

    # Ошибка
    guild_count = await ipc_client.request("get_guild_count")

    print(guild_count)
    return {"members": ["5", "6"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)