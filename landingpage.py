from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (You can replace this with your actual data)
blogs = [
    {"title": "How to Find and Attract Business Investors", "content": "Funding is crucial to starting a business and creating a thriving, growing entity. You may have initially self-funded your business with cash, relied on sweat equity, or used credit cards to finance your business. However, you’ll need to consider outside capital at some point if you want to continue growing your operations.With venture capital, traditional bank loans and online crowdsourcing, today’s entrepreneurs have more funding options than ever. However, choosing the right investor type is critical. Different investors bring unique benefits and assorted types of equity, control and repayment requirements. "},
    {"title": "How To Invest In A Startup", "content": "It can be challenging to offer a precise definition of a startup: It can be a business creating a new product or service under conditions of extreme uncertainty, or a company aiming to solve a problem where the solution is not obvious and success is not guaranteed.However you define a startup, it used to be that you needed both wealth and good connections to invest in them. This is no longer the case, however, and average investors can easily grab a piece of an exciting startup opportunity using crowdfunding sites.Startup investing is potentially lucrative, but it’s important to understand that it comes with big risks. The vast majority of startups fail—even if you do your research, you could end up with a pocket full of nothing. Here’s what you need to know to begin investing in startups."},
    
]

@app.route('/')
def index():
    return render_template('index.html', blogs=blogs)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here, you can process the form data (e.g., send an email or save it to a database)
        return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
