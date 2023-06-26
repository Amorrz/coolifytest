from flask import Flask, render_template, request
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    prompt = request.form['prompt']
    response = llm_chain.run(prompt)
    return render_template('index.html', prompt=prompt, response=response)




PATH = os.environ.get("LLAMA_MODEL_PATH")

llm = GPT4All(model=PATH, verbose=True)

prompt = PromptTemplate(input_variables=['question'], template="""
    Question: {question}
    
    Answer:
    """)

llm_chain = LLMChain(prompt=prompt, llm=llm)


if __name__ == '__main__':
    app.run()
