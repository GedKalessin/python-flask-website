from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Napoli, Italy',
  'salary': '€ 40k'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Roma, Italy',
  'salary': '€ 35k'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'Remote',
  'salary': '€ 45k'
}, {
  'id': 4,
  'title': 'Frontend Engineer',
  'location': 'Remote',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
