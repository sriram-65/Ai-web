
from flask import Flask , request , jsonify , render_template , url_for
import google.generativeai as genai

app = Flask(__name__)


genai.configure(api_key="AIzaSyAvyLEzkIaibw5BFF4ZCISLljZNbLKd2Cg")
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-ai-website" , methods=["POST"])
def get_ai():
    title = request.form.get("title")
    if not title:
        return jsonify({"ERROR" : "TITLE IS MUST..."})
    gen_web = model.generate_content(f'''Generate a modern, sleek, and interactive website about this title {title} UI design that follows the latest web design trends with full and fully bootsrap.and pop-up animations must and dark and normal theme you can select randomly (wheather Dark or normal theme) and responsive web app and  don't add the image you can icons from the fontaswome . add home , about , contact , feauters add in the about sections in the left side don't add image insted of adding image you can add icon in the navbar The design should include: Modren ui and more acccording to the title which i described The website should be visually stunning, highly engaging, and perfect for a modern tech startup Use a futuristic yet professional color palette, including gradients, neon accents, and modern UI components. Avoid cluttered layouts and unnecessary distractions GIVE ONLY CODE DONt GIVE ANY ANOTHER TEXT EVEN DON't GIVE TEST LIKE ''html like this GIVE ALL THE CODE IN SINGLE FILE ''' )
    res = gen_web.text.replace("```html" , "").replace("```" , "").strip()
    return render_template("ai.html" , res=str(res) , title=title)
    
    


if __name__ == "__main__":
    app.run(debug=True)

