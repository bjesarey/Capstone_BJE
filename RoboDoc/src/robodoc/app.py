from flask import Flask, request, jsonify
from flask_cors import CORS
from robodoc.crew import Robodoc

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    symptoms = data.get("symptoms", "")

    try:
        
        result = Robodoc().crew().kickoff(inputs={
            "symptoms": symptoms
        })

        return jsonify({
            "response": str(result)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
    
#Note 1: Crew must run once before server can start(crewai run).
#Note 2: Press control + c to stop running the server.