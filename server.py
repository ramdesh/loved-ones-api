from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from interact import sample_sequence
from interact import run
import torch

from log_config import get_logger

logger = get_logger()
API_BASE = "/v1"

loved_ones = Flask(__name__)
cors = CORS(loved_ones)
history = []

tokenizer, personality, model, args = run()


@loved_ones.route(API_BASE + "/")
def server_hello():
    return "This is the Loved Ones Model Execution API"


@loved_ones.route(API_BASE + "/messages", methods=["POST"])
def send_message():
    raw_text = request.get_json().get("message")
    history.append(tokenizer.encode(raw_text))
    with torch.no_grad():
        out_ids = sample_sequence(personality, history, tokenizer, model, args)
    history.append(out_ids)
    # history = history[-(2 * args.max_history + 1):]
    out_text = tokenizer.decode(out_ids, skip_special_tokens=True)
    return jsonify({"message": raw_text, "response": out_text})


@loved_ones.route(API_BASE + "/info")
def get_info():
    return jsonify({"modelName": args.model})
