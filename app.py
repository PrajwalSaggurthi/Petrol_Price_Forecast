from flask import *
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')




@app.route('/result', methods=['GET'])
def result():
    data = request.args.get('data')
    data = str(data)
    data = data.split('-')
    string=''
    for i in data:
        string+=i
    model=pickle.load(open('/Users/prajwalsaggurthi/Desktop/Project/model3.pkl','rb'))
    res=str(model.predict([[int(string)]]))
    return render_template('base.html',result=res)

if __name__ == '__main__':
    app.run(debug=True)
