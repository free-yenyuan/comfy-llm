import __main__
import filecmp
import json
import os
import shutil
import sys


python = sys.executable


extentions_folder = os.path.join(os.path.dirname(os.path.realpath(__main__.__file__)),
                                 "web" + os.sep + "extensions" + os.sep + "Comfy_LLM")
javascript_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")

if not os.path.exists(extentions_folder):
    print('Making the "web\extensions\Comfy_LLM" folder')
    os.mkdir(extentions_folder)

result = filecmp.dircmp(javascript_folder, extentions_folder)

if result.left_only or result.diff_files:
    print('Update to javascripts files detected')
    file_list = list(result.left_only)
    file_list.extend(x for x in result.diff_files if x not in file_list)

    for file in file_list:
        print(f'Copying {file} to extensions folder')
        src_file = os.path.join(javascript_folder, file)
        dst_file = os.path.join(extentions_folder, file)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        #print("disabled")
        shutil.copy(src_file, dst_file)
    
if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json")):
    config = {
        "AuthToken": "your key",
        "TeamID":"your TeamID"
    }
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "w") as f:
        json.dump(config, f, indent=4)

#load config
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "r") as f:
    config = json.load(f)

# Combine the dictionaries
#NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS_G}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
