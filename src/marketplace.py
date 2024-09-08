import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

grpc_host = os.getenv("GRPC_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{grpc_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    print("recommendations_client")
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )


# This couple of lines below comment has been added up temporaly to fix
# an importation issue of the grpc when running FLASK_APP=marketplace.py flask run
# even hard installing it and also adding it up to this directory's requirements.txt
if __name__ == '__main__':
    app.run('localhost',50052, debug=True)
