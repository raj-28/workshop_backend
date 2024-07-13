from flask import Flask
import psycopg2

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
  
@app.route('/')
def hello_cloud():
  return 'Service is Running!!'
  
@app.route('/members', methods=['GET'])
def get_members():
# Connect to the database 
    conn = psycopg2.connect(database="database_name", 
                            user="username", 
                            password="password", 
                            host="hostname", port="5432")
  
    # create a cursor 
    cur = conn.cursor() 
  
    # Select all products from the table 
    cur.execute('''SELECT * FROM members''') 
  
    # Fetch the data 
    data = cur.fetchall() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    #return render_template('index.html', data=data) 
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
