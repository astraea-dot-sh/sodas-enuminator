from subprocess import run as subrun


def execute(tool_name, target, args):
    command = [tool_name]
    for i in args:
        command.append(i)
    command.append(target)
        
    output = subrun(command, capture_output=True).stdout
    return (str(output).replace("\\n", "\n")) # we replace the fake \n with real ones

def run(tool_name, target, options):
    """run the programs and get the output"""
    if tool_name == "nmap":
        options = ["-sP"]
        return execute(tool_name, target, options)
    else:
        return ("NOT WORKING")
    
