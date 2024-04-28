# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses_dict = {
"hello": ["Hi there! How can I help you?", "Hello! What's up?", "Hey!"],
"how are you ?": ["I'm good, thanks!", "I'm just a bot, but I'm doing well!"],
"how are you": ["I'm good, thanks!", "I'm just a bot, but I'm doing well!"],
"bye": ["Goodbye! Take care.", "See you later!", "Farewell!"],
"hey": ["Hi there! How can I help you?", "Hello! What's up?", "Hey!"],
"hi": ["Hi there! How can I help you?", "Hello! What's up?", "Hey!"],
"i need your service": ["There are variety of services we offer, kindly navigate to services to see what we do.", "I'm just a bot, kindly navigate to services to see all we do."],
"What service do you offer": ["I'm just a chatbot, and I can help you find the services we offer by telling you to navigate to our service page, click on services above."],
"which services do you provide":["I'm just a chatbot, and I can help you find the services we offer by telling you to navigate to our service page, click on services above."],
"which service do you offer": ["There are variety of services we offer, kindly navigate to services to see what we do.", "I'm just a bot, kindly navigate to services to see all we do."],
"computer vision": ["Sure, Computer Vision solutions is one of the services we offer, kindly navigate to the Contact Us web page to request for a call from one of the company's representatives."],
"chatbot": ["Sure, Chatbot Development is one of the services we offer, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representatives."],
"chatbot development": ["Sure, Chatbot Development is one of the services we offer, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representatives."],
"website chatbot": ["Sure, Chatbot Development is one of the services we offer, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representatives."],
"i need a website": ["Sure, Web Development is one of the services we offer, kindly navigate to the Contact Us web page to book a discovery call with one of the company's representatives."],
"i need a predictive model": ["Sure, we can fix you with a trained model, kindly navigate to the Contact Us web page to request a call from the company's representative."],
"i need a generative model": ["Sure, we can fix you with a trained model, kindly navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need a model": ["Sure, we can fix you with a trained model, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"artificial intelligence service": ["Sure, we provide AI/ML solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"machine learning service": ["Sure, we provide AI/ML solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"ai/ml service": ["Sure, we provide AI/ML solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need artificial intelligence service": ["Sure, we provide AI/ML solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need machine learning service": ["Sure, we provide AI/ML solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"ai/ml service": ["Sure, we provide AI/ML solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need ai/ml service": ["Sure, we provide AI/ML solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need azure cloud service": ["Sure, we provide cloud service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need aws cloud service": ["Sure, we provide Cloud srvice solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"azure cloud service": ["Sure, we provide cloud service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"aws cloud service": ["Sure, we provide Cloud service solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need azure ml studio service": ["Sure, we provide Azure ML Studio service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"azure ml studio service": ["Sure, we provide Azure ML Studio service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need azure ai vision service": ["Sure, we provide Azure AI Vision service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"azure ai vision service": ["Sure, we provide Azure AI Vision service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need computer vision service": ["Sure, we provide Computer Vision service, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"computer vision service": ["Sure, we provide Computer Vision service, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"ai and ml service": ["Sure, we provide AI & ML solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need ai and ml service": ["Sure, we provide AI & ML solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need ai automation service": ["Sure, we provide ai automation service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"ai automation service": ["Sure, we provide ai automation service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need azure and aws cloud service": ["Sure, we provide Cloud srvice solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"azure and aws cloud service": ["Sure, we provide Cloud srvice solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need deep learning service": ["Sure, we provide Deep Learning/Reinforcement service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"deep learning service": ["Sure, we provide Deep Learning/Reinforcement service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need deep learning and reinforcement learning service and solutions": ["Sure, we provide Deep Learning/Reinforcement service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need deep learning and reinforcement learning service": ["Sure, we provide Deep Learning/Reinforcement service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"reinforment learning service": ["Sure, we provide Deep Learning/Reinforcement service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need reinforcement learning service solutions": ["Sure, we provide Deep Learning/Reinforcement service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"ai cloud integration": ["Sure, we provide seemless Cloud service experience, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need ai cloud service integration": ["Sure, we provide seemless Cloud service experience, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need azure and aws cloud integrations": ["Sure, we provide seemless Cloud service experience, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need azure cloud integration": ["Sure, we provide seemless Cloud service experience, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need aws cloud integration": ["Sure, we provide seemless Cloud service experience, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"i need azure service": ["Sure, we provide cloud service solutions, kindly navigate to the Contact Us web page to request a discovery call with one of the company's representative."],
"i need aws service": ["Sure, we provide Cloud srvice solutions, Please! navigate to the Contact Us web page to request a discovery call with the company's representative."],
"how can i collaborate or work with you on a project?": ["I'm open to collaboration opportunities, whether it's through employment, freelance work, or joint projects, you can navigate to Request for Discovery Call page to reach me."],
"can you provide mentorship or consulting services for ai and ml projects?": ["Sure, I'm open to providing mentorship or consulting services and you can reach out to me by heading to the Request for Discovery Call page."],
"can you explain a complex ai/ml concept in simple terms?": ["Sure, I understand the need to communicate undastandably with non-technical stakeholders."],
"what is your approach to problem-solving in ai and ml?": ["I establish what the problem is, I consider what type of data is suitable for my experiment, I clean my data and verify for anomalies in the data,and I conduct the experiment suitable for my dataset, and I continue to work on my inference models to improve and make my models smarter."],
"what industries have you applied ai and ml solutions to?": ["I created a preditive model to help a Microfinance bank verify if the bank customer has the means to pay back granted loan."],
"can you share some of your notable projects?": ["I've worked using computer vision library, flask library, predictive models, and conversational chatbot to help improve my clients service delivery and customer satisfaction."],
"what programming languages do you specialize in for ai and ml?": ["I work with languages such as Python, js, css, and html."],
"what is your background in ai and ml?": ["I have worked on diverse projects ranging from natural language processing to computer vision. My expertise includes python, website development, NLP, conversational AI, preditive and generative models, data engineer, Azure and AWS ML Studio."],
"what is artificial intelligence (ai)?": ["Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans."],
"what is machine learning (ml)?": ["Machine Learning is a subset of AI that provides systems the ability to automatically learn and improve from experience without being explicitly programmed."],

}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})

def get_chatbot_response(user_input):
    # Lookup user input in the dictionary and return a random response from the list
    if user_input.lower() in responses_dict:
        return responses_dict[user_input.lower()][0]
    else:
        return "I'm sorry, I didn't understand that."
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
