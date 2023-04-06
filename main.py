from flask import Flask, render_template

# Create a flask app
app = Flask(
  __name__,
  template_folder='template',
  static_folder='static'
)

JOBS = [
  {
    'id' : 1,
    'Role' : 'Andriod Devloper',
    'Location' : 'Mumbai',
    'Salary' : 'RS. 10,00,000'
  },
  {
    'id' : 2,
    'Role' : 'Frontend Devloper',
    'Location' : 'Bengluru',
    'Salary' : 'RS. 15,00,000'
  },
  {
    'id' : 3,
    'Role' : 'Backend Devloper',
    'Location' : 'Remote',
    # 'Salary' : 'RS. 20,00,000'
  },
  {
    'id' : 4,
    'Role' : 'Data Analyst',
    'Location' : 'San Fansisco',
    'Salary' : '$. 100,000'
  }
]

# Index page (now using the index.html file)
@app.route('/')
def index():
  return render_template('index.html', jobs=JOBS, conpany_name= 'Bright')

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )