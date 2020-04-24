import os
import sys
import string
import re
from datetime import datetime
from datetime import timedelta

#global varible
admin_name = 'benliu'
pr_edit_cmd = '/volume/buildtools/bin/pr-edit '
pr_query_cmd = '/volume/buildtools/bin/query-pr'

#change ETA status if date is dued.
def change_eta(pr_num, scope_num):

  input_file = 'pr_content_1.txt'
  output_file = 'pr_content_2.txt'
  
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
            if (date_object < datetime.now() + timedelta(days=2)):
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
  query_file = 'query.txt'
  command_options = ' -x --expr \'Responsible~"' + dev_name + \
          '" | Dev-Owner~"' + dev_name + '"\''
  command = pr_query_cmd + command_options + ' -o '+ query_file
  os.system(command)

  #parser output file
  with open(query_file, "r") as f:
      paras = paragraphs(f)
      for para in paras:
          for line in para.split('\n'):
            if 'Number:' in line:
              pr_number = (line.split(": ")[1].strip())

            # parser the scope name and call change_eta
            pattern = re.compile(r'^>State{(\d+)}:')
            m = pattern.match(line)
            if m:
              scope_num = m.group(1)
              scope_state = (line.split(": ")[1].strip()) 
              if scope_state in ['awaiting-build', 'verify-resolution', 'closed']:
                  continue
              #update ETA of PR
              print('update ETA of PR' + pr_number + ' Scope ' + scope_num + \
                      ', State is ' + scope_state)
              change_eta(pr_number, scope_num)
  
  #swap out temp file
  command= 'rm -rf ' + query_file
  os.system(command)

def pr_eta_update():
  with open('dev_name_list', "r") as f:
      for line in f:
          dev_name = (line.split("@")[0].strip())
          if not len(dev_name):
              continue
          print('Dev_name: ' + dev_name)
          pr_number = query_pr(dev_name)

if __name__ == "__main__":
    pr_eta_update()
