# Testing GitHub - rstanev@gmail.com

import numpy as np
import pandas as pd
import quandl

from flask import Flask, render_template, request, redirect
from bokeh.plotting import show, output_file, output_notebook
from bokeh.charts import TimeSeries

app = Flask(__name__)

app.vars={}

quandl.ApiConfig.api_key = 'HWZYrHmanku_oE1Ydh5g'

@app.route('/')
def main():
  return redirect('/index')
  
@app.route('/index',methods=['GET','POST'])
def index():
    #nquestions=app.nquestions
    if request.method == 'GET':
        return render_template('userinfo_lulu.html',num=1,question='Which daily price value do you want?',ans1='Open',\
            ans2='Close',ans3='High')
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
	
	data = quandl.get('WIKI/%s'%(app.vars['name']))

	data[app.vars['option']].plot()
	print 'Got data and plot'
	#plt.show()
	#plt.savefig('%s.png'%(app.vars['name']))
		
	#output_notebook()
	
	_plot = TimeSeries(data[app.vars['option']], color='blue', legend=True, title='%s Stock Price'%(app.vars['name']))
	_plot.xaxis.axis_label = 'Date'
	_plot.yaxis.axis_label = 'Price'
	print 'Set plot now about to output file'
	output_file('%s.html'%(app.vars['name']))
	print 'output file'
	show(_plot)
	print 'show plot'
	
	#return render_template('end_lulu.html')
	return redirect('/index')
	
if __name__ == "__main__":
    app.run(port=33507, debug=True)