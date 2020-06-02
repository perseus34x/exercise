import os
import sys
import string
import re
import time
from datetime import datetime
from datetime import timedelta
from os import path

#global varible
admin_name = 'benliu'
pr_edit_cmd = '/volume/buildtools/bin/pr-edit '
pr_query_cmd = '/volume/buildtools/bin/query-pr'
file_pr_in_veri = 'pr_in_verification.txt'

#record PRs under verification state
def record_pr_in_verification(dev_name, pr_num, scope_num):

  veri_file = os.path.join(sys.path[0], file_pr_in_veri)

  # open again the query_file.
  query_file = os.path.join(sys.path[0], 'query.txt')
  #parser output file
  with open(query_file, "r") as f:
      
      paras = paragraphs(f)
      for para in paras:
          for line in para.split('\n'):
            # parser pr number
            if 'Number:' in line:
              number = (line.split(": ")[1].strip())
            if number != pr_num:
              break

            # parser owner
            str = 'Responsible{' + scope_num + '}'
            if str in line:
              owner = (line.split(": ")[1].strip())
              if owner in [dev_name,'slt-builder']:
                with open(veri_file, "a") as f:
                  line = 'https://gnats.juniper.net/web/default/' + pr_num + '#scope_tab ' + scope_num + '\n'
                  f.write(line)

#change ETA status if date is dued.
def change_eta(pr_num, scope_num):

  input_file = os.path.join(sys.path[0], 'pr_content_1.txt')
  output_file = os.path.join(sys.path[0], 'pr_content_2.txt')
  
  # get the system date
  now = datetime.now()

  #dump PR content into temp file
  command = pr_edit_cmd + pr_num + ' -l ' + admin_name + ' > ' + input_file
  os.system(command)

  # parser the temp file
  with open(input_file,"rt") as fin:
    with open(output_file, "wt") as fout:
      for line in fin:
        # dev_owner parser
      #  dev_owner = 'Dev-Owner{' + scope_num + '}:'
      #  if dev_owner in line:
      #    dev_owner = (line.split(": ")[1].strip())
      #    print('Dev-Owner:' + dev_owner)

        # fix ETA update
        fix_eta_scope = 'Fix-ETA-Scope{' + scope_num + '}:'
        if fix_eta_scope in line:
          fix_eta = (line.split(": ")[1].strip())
          if not fix_eta:
            modified_eta = datetime.now() + timedelta(days=7)
            #write to file and print updated date here
            print('ETA is updated to ' + modified_eta.strftime("%Y-%m-%d"))
            fout.write(line.strip() + ' ' + (modified_eta.strftime("%Y-%m-%d")) + '\n')
          else:
            if (len(fix_eta.split(" ")) is not 6): 
                continue
            week,month,day,time,zone,year = fix_eta.split(" ")
            date_string= month + " " + day + " " + year
            date_object = datetime.strptime(date_string, "%b %d %Y")
            if (date_object < datetime.now() + timedelta(days=4)):
              modified_eta = datetime.now() + timedelta(days=7)
              #write to file and print updated date here
              print('ETA is updated to ' + modified_eta.strftime("%Y-%m-%d"))
              fout.write(line.replace(fix_eta, modified_eta.strftime("%Y-%m-%d")))
            else:
              fout.write(line)
        else:
          fout.write(line)

  #update PR content from modified file
  command = pr_edit_cmd + pr_num + ' < ' + output_file
  os.system(command)

  #unlock
  command = pr_edit_cmd + pr_num + ' -u'
  os.system(command)
  #swap out temp file
  command= 'rm -rf ' + input_file
  os.system(command)
  command= 'rm -rf ' + output_file
  os.system(command)

def paragraphs(fileobj):
  """Iterate a fileobject by paragraph"""
  ## Makes no assumptions about the encoding used in the file
  lines = []
  for line in fileobj:
    if len(line.strip()) == 0 and lines:
      yield ''.join(lines)
      lines = []
    else:
      lines.append(line)
  yield ''.join(lines)

#PRs query
def query_pr(dev_name):

  #query PRs under dev_name 
  query_file = os.path.join(sys.path[0], 'query.txt')
  command_options = ' -x --expr \'Responsible~"' + dev_name + \
          '" | Dev-Owner~"' + dev_name + '"\''
  command = pr_query_cmd + command_options + ' -o '+ query_file
  os.system(command)

  #parser output file
  with open(query_file, "r") as f:
      paras = paragraphs(f)
      for para in paras:
          for line in para.split('\n'):
            
            # parser pr number
            if 'Number:' in line:
              pr_number = (line.split(": ")[1].strip())
              continue

            # parser owner
#            if 'Responsible' in line:
#              owner = (line.split(": ")[1].strip())
            
            # parser the scope name and call change_eta
            pattern = re.compile(r'^>State{(\d+)}:')
            m = pattern.match(line)
            if m:
              scope_num = m.group(1)
              scope_state = (line.split(": ")[1].strip()) 
              if scope_state in ['awaiting-build', 'closed']:
                  continue
              #check the pr in "verify-resolution"state
              if scope_state in ['verify-resolution']:
    #            if dev_name is owner:
                record_pr_in_verification(dev_name, pr_number, scope_num)
                continue
              #update ETA of PR
              print('update ETA of PR' + pr_number + ' Scope ' + scope_num + \
                      ', State is ' + scope_state)
              change_eta(pr_number, scope_num)
  
  #swap out temp file
  command= 'rm -rf ' + query_file
  os.system(command)

def pr_eta_update():
  dev_name_file = os.path.join(sys.path[0],'dev_name_list')
  with open(dev_name_file, "r") as f:
      for line in f:
          dev_name = (line.split("@")[0].strip())
          if not len(dev_name):
              continue
          print('Dev_name: ' + dev_name)
          pr_number = query_pr(dev_name)

  # mail pr in verification information, then delete the temp file
  veri_file = os.path.join(sys.path[0], file_pr_in_veri)
  if path.exists(veri_file):
    time.sleep(5)
    os.system('/usr/bin/mail -t benliu@juniper.net -s pr_in_verificaton < ' + veri_file)
    command= 'rm -rf ' + veri_file
    os.system(command)

if __name__ == "__main__":
    pr_eta_update()
