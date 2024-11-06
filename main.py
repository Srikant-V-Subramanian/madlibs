from flask import Flask,render_template,request
app=Flask(__name__)
GOOGLE_API_KEY="AIzaSyDHwUe9wt4l2XQvYfVrQV6JoAUzIeiN4k4"
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro-001",
  generation_config=generation_config,
)

@app.route("/",methods=["GET","POST"])
def k():
    if request.method=="POST":
        a = request.form.get("verb-1")
        b = request.form.get("verb-2")
        c = request.form.get("adjective-1")
        d = request.form.get("noun-1")
        a1 = model.generate_content(f"generate a story based on four words {a}, {b}, {c}, and emotion {d}, generate an apt title for the story too, insert baclslash before every apostrophe")
        print(a1.text)
        return render_template("index2.html",data=a1.text)


    return render_template("index.html")


app.run(port=9995)
