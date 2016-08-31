# Testing GitHub - rstanev@gmail.com

import numpy as np
import pandas as pd
import quandl
import requests
import simplejson
import bokeh

from flask import Flask, render_template, request, redirect
from bokeh.plotting import show, output_file
from bokeh.charts import TimeSeries
from bokeh.embed import components

bv = bokeh.__version__

app = Flask(__name__)

app.vars={}

#quandl.ApiConfig.api_key = 'HWZYrHmanku_oE1Ydh5g'

@app.route('/')
def main():
  return redirect('/index')
  
@app.route('/index',methods=['GET','POST'])
def index():
    #nquestions=app.nquestions
    if request.method == 'GET':
        return render_template('userinfo_lulu.html',num=1,question='Which daily price value do you want?',ans1='Open',\
            ans2='High',ans3='Low',ans4='Close')
    else:
        # request was a POST
        app.vars['name'] = request.form['name_lulu']
        app.vars['option'] = request.form['option_lulu']
        '''
        f = open('%s.txt'%(app.vars['name']),'w')
        f.write('Symbol: %s\n'%(app.vars['name']))
        f.write('Option: %s\n'%(app.vars['option']))
        f.close()
		'''
        return redirect('/finish')

@app.route('/finish')
def finish_():
	
	req_='https://www.quandl.com/api/v3/datasets/WIKI/%s.json?&collapse=daily'%(app.vars['name'])

	r = requests.get(req_)
	
	cols = r.json()['dataset']['column_names'][0:5]
	df = pd.DataFrame(np.array(r.json()['dataset']['data'])[:,0:5],columns=cols)
	df.Date = pd.to_datetime(df.Date)
	df[['Open','High','Low','Close']] = df[['Open','High','Low','Close']].astype(float)

	d = dict(
    	Option=df[app.vars['option']],
    	Date=df['Date'],
	)

	_plot = TimeSeries(d, x='Date', y='Option', color='blue', \
	title='%s Stock Price'%(app.vars['name']), legend='top_left')
	
	_plot.xaxis.axis_label = 'Date'
	_plot.yaxis.axis_label = '(%s) Price'%(app.vars['option'])

	#show(_plot)

	script, div = components(_plot)
	return render_template('graph.html',bv=bv,name=app.vars['name'],script=script,div=div)
							
	#data = quandl.get('WIKI/%s'%(app.vars['name']))

	#data[app.vars['option']].plot()
	#plt.show()
	#plt.savefig('%s.png'%(app.vars['name']))
		
	#output_notebook()
	'''
	_plot = TimeSeries(data[app.vars['option']], color='blue', legend=True, title='%s Stock Price'%(app.vars['name']))
	_plot.xaxis.axis_label = 'Date'
	_plot.yaxis.axis_label = 'Price'
	'''
	'''
	output_file('%s.html'%(app.vars['name']))
	show(_plot)
	'''
	#return render_template('end_lulu.html')
	return redirect('/index')
	
if __name__ == "__main__":
    app.run(port=33507, debug=True)