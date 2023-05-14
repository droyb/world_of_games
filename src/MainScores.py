from flask import Flask, render_template
import Utils

app = Flask(__name__)


@app.get("/score")
def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME, 'r') as f:
            score = int(f.read())
        return render_template('score.html', score=score)
    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8000)
