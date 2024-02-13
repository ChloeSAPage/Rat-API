from flask import Flask, send_file

app = Flask(__name__)


@app.route("/get-rat/<rat_id>")
def get_rat(rat_id):
    
    rat_pic_path = f"resources/rat{rat_id}.jpg" 

    return send_file(rat_pic_path, mimetype="image/jpeg"), 200



if __name__ == "__main__":
    app.run(debug=True)