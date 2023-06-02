from sys import platform
from scripts import tool_handling

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

if platform == "linux" or platform == "linux2":
    print("[+] Supported OS: Linux")
else:
    print("[-] Unsupported OS: " + platform)
    exit(1)

target = "192.168.0.1"


tools = tool_handling.get_tool_list(True)
print(f"[+] Tools found:{tools}")
print(f"[+] Running tools on {target}")


@app.route("/scan")
def startup():
    result = tool_handling.run_tool("nmap", target)
    return render_template("scan.html", result=result)