#from flask import Flask, request
from quart import Quart, request
from flask_cors import CORS, cross_origin
from discord.ext import ipc


app = Quart(__name__, static_url_path='')
#ipc_client = ipc.Client(secret_key="aboba")
#app = Flask(__name__, static_url_path='')

app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={'*':{'origins': 'http://127.0.0.1:3000'}})


@app.route("/members")
@cross_origin()
async def members():
    return {"members": ["1", "2"]}


@app.route("/hello", methods=['POST', 'GET', 'OPTIONS'], strict_slashes=False)
@cross_origin()
async def hello():
    if request.method != 'POST':
        print("Not post")
        return {"members" : ["3", "4"]}
    #request_data = request.get_json(force=True)
    #guild_id = int(request_data['guild_id'])
    #channel_id = int(request_data['channel_id'])
    #message = request_data['message']
    guild_count = await ipc_client.request("get_guild_count")
    print(guild_count)
    print('Aboba')
    return {"members": ["5", "6"]}


if __name__ == "__main__":
    app.run(debug=True)
