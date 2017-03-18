from flask import Flask
import sys
from github import Github
import base64
app = Flask(__name__)
#g = Github("983f0e8038995ca6293f9411c754156510e45e07")
g = Github()

 #github = Github(sys.argv[1])
part =  str(sys.argv[1]).split('/')
@app.route("/v1/<filename>")
def get_config(filename):
 f = filename.split('.')
 if (f[1] == 'yml' or f[1] == 'json'):
   n=g.get_user(part[3])
   repo = n.get_repo(part[4]) 
   h = repo.get_file_contents(filename).content
   return base64.b64decode(h)
  
 else:
    return 'file not accepted' 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    #"cdbf95dea14ff687e257a10d2e8872d371b5ff71"
