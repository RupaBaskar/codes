# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, jsonify
import pickle
import pygal
app = Flask(__name__)


@app.route('/', methods = ['GET'])
def graph():

    
    num = request.args.get('Info')
    if num == None:
        num= '1'
    
    
    
    filename = 'final_model.pkl'

    loaded_model = pickle.load(open(filename, 'rb'))
    
    abn = int(num)
    pred_uc = loaded_model.get_forecast(steps=abn)


    pred_ci = pred_uc.conf_int()

    lower = list(pred_ci.iloc[:, 0])

    pred_ci.iloc[:, 1] = pred_ci.iloc[:, 1] - 5

    upper =list(pred_ci.iloc[:, 1])

    mean = (pred_ci.iloc[:, 0] + pred_ci.iloc[:, 1])
    avg = list(mean/2)
    lower = [int(a) for a in lower]
    upper = [int(a) for a in upper]
    avg = [int(a) for a in avg]

 
    if num == '1':
        year = ['JUNE 2021']
        
  
    if num == '2':
        year = ['JUNE 2021','JULY 2021'] 
    if num == '3':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021']  
    if num == '4':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021']  
    if num == '5':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021']   
    if num == '6':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021']   
    if num == '7':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021']      
    if num == '8':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2021']
    if num == '9':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2021','FEBRUARY 2022']
    if num == '10':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2021','FEBRUARY 2022','MARCH 2022']
    if num == '11':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2021','FEBRUARY 2022','MARCH 2022','APRIL 2022']   
    if num == '12':
        year = ['JUNE 2021','JULY 2021','AUGUST 2021','SEPTEMBER 2021','OCTOBER 2021','NOVEMBER 2021','DECEMBER 2021','JANUARY 2021','FEBRUARY 2022','MARCH 2022','APRIL 2022','MAY 2022']      
    
    coll = ['$100k','$200k','$300k','$400k','$500k','$600k','$700k']   
    num = 1000
    lower1 = [int(i/num) for i in lower]
    num = 1000
    upper1 = [int(i/num) for i in upper]


    finallist = []
    for i in range(abn):
        vm = (year[i],lower[i],upper[i],avg[i])
        finallist.append(vm)
    graph = pygal.Line()
    graph.title = 'collection prediction'
    graph.x_labels = year
    graph.y_labels = [
  {'label': '$100k', 'value': 100},
  {'label': '$300k', 'value': 300},
  {'label': '$500k', 'value': 500},
  {'label': '$700k', 'value': 700},
  {'label': '$900k', 'value': 900},
  {'label': '$1100k', 'value': 1100},
  {'label': '$1300k', 'value': 1300},
  {'label': '$1500k', 'value': 1500},
  {'label': '$1700k', 'value': 1700},
  {'label': '$1900k', 'value': 1900}]
    graph.add('upper',  upper1)
    graph.add('lower',    lower1)
    
    graph_data = graph.render_data_uri()
    
    
    


   
    return render_template('graph.html', labels=year, ca=lower, charge=upper,values = finallist,graph_data = graph_data)
    #return jsonify(labels=labels, ca=ca, charge=charge, ecart=ecart, info=info)



        
        


if __name__ == '__main__':

    app.run(debug=True,port=3000)
    
#TODO: 