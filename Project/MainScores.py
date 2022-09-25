from flask import Flask, request, Response

from Utils import BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/score', methods=["POST"])
def score_server():
    try:
        input_json = request.get_json(force=True)
        SCORE = input_json["score"]
        return Response(f"<html> <head><title>Scores Game</title> </head><body> <body><h1>The score is <div id='score'>{SCORE}</div></h1> </body></html>", status=200)

    except:
        return Response(f"<html> <head><title>Scores Game</title> </head><body> <body><h1><div id='score' style='color: red'>{BAD_RETURN_CODE}</div></h1> </body></html>", status=400)
