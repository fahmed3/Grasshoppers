
from flask import Flask, render_template
import occupations

jobsite = Flask(__name__)

@jobsite.route('/occupations')
def occupy() :
    return render_template('jobs.html',
                           j = occupations.JOBS,
                           one = occupations.randomJob())

if __name__ == "__main__" :
    jobsite.debug = True
    jobsite.run()
