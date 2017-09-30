#Fabiha Ahmed, Kristin Lin
#SoftDev Pd 9
#Work05 - Occupational Jinja Training
#2017-09-27

from flask import Flask, render_template
from utils import occupations

jobsite = Flask(__name__)

@jobsite.route('/')
@jobsite.route('/occupations')
def occupy() :
    return render_template('jobs.html',
                           j = occupations.JOBS,
                           one = occupations.randomJob())

if __name__ == "__main__" :
    jobsite.debug = True
    jobsite.run()
