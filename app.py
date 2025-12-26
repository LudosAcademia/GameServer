from flask import Flask, request, jsonify, abort
import jwt
import data
from config import Config

app = Flask(__name__)

@app.route("/")
def main_route():
    return "<p>None</p>"


@app.route("/gate_data", methods=["POST"])    
def recieve_data():
    print("REQUEST RECEIVED")
    if request.method == 'POST':
        header = request.headers.get("Authorization")
        if not header:
            abort(401, "Missing Authorization header")    
        #split the header into 2 elements put into an array and get the index 1 of that array
        encoded_jwt = header.split(" ",1)[1]
        print(encoded_jwt)
        try:
            valid = verify_jwt(encoded_jwt)
            print("JWT verification result:", valid)
        except Exception as e:
            print("JWT verification crashed:", type(e), e)
            return {"error": str(e)}, 401
        if not valid:
            abort(401, "Authorization Failed")

        payload = request.get_json()
        key = Config.SECRET_KEY

        decoded_jwt = jwt.decode(encoded_jwt, key, algorithms="HS256")

        user_data = data.UserData()
        user_data.user_id = decoded_jwt["sub"]
        user_data.playgrounds = payload.get("playgrounds")
        print(user_data.user_id)
        print(user_data.playgrounds)   
        return jsonify(payload), 200
    else:
        return 'Method Not Allowed', 405
    


def verify_jwt(encoded_jwt):
    try:
        key = Config.SECRET_KEY
        decoded_jwt = jwt.decode(encoded_jwt, key, algorithms="HS256")
        json = jsonify(decoded_jwt)
        return True
    except jwt.exceptions.InvalidSignatureError:
        print("Signature is invalid")
        return False
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)



""" Comment Section



@app.route("/get_user_id", methods=["GET"])    
def recieve_user_id_request():
    import data
    user_id = data.UserData.user_id
    username = data.UserData.username
    payload = {"user_id":user_id, "username":username}
    return jsonify(payload)

@app.route("/get_plygrd_id", methods=["GET"])    
def recieve_plygrd_id_request():
    import data
    p_name = data.PlaygroundData.p_name
    p_desc = data.PlaygroundData.p_desc
    payload = {"p_name":p_name, "p_desc":p_desc}
    return jsonify(payload)



@app.route("/send_id", methods=["POST"])    
def recieve_id():
    if request.method == 'POST':
        import main
        main.Main.confirm_php_connect(request.form.get("user_id"))
        #print(request.data.decode())
        return 'ID received successfully!', 200
    else:
        return 'Method Not Allowed', 405

        #id,data,len


        #import data
        #my_sql = [data.Tiles.from_dict(t) for t in payload["tiles"]]

       

        #tiles_data = request.json
        #sql_data = data.Tiles.from_dict(tiles_data)
        #print('Received JSON data:', payload)
        #main.send_data_mysql(sql_data,100,17)


        if(payload["tile_index"] != None):
            tiles = data.PlaygroundData()
            tiles.tiles_index = payload["tile_index"]
            tiles.tiles_content = payload["tile_contain"]
            main.Main.send_tiles_mysql(payload["playground_id"], tiles, 100)


        if(payload["p_name"] != None):   
            data.PlaygroundData.p_name = payload["p_name"]
            data.PlaygroundData.p_desc = payload["p_desc"]




"""
