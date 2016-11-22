#!/usr/bin/python
__version__ = '0.1'

##----PACKAGE------##
import argparse
import datetime
import time
import sys
import os
from argparse import RawTextHelpFormatter

##----MAIN---------#
def main():
	args = get_args()

	if len(sys.argv) < 2:
		print_ornament('   ABORT! No input! Try \'CTHub -h\'!', 100, ' ', 1, 0)
	
	else:
		run_mode_one(args)
	
##----CODA---------##
	print_ornament('> END', 100, ' ', 1, 1)
	print_ornament('', 100, '-', 0, 0)
	print '\n\n'

##----FUNCTION-----##
#--common--
class get_class_from_dict:
	def __init__(self, **entries): 
		self.__dict__.update(entries)

def add_thousand_separator(int_number):
	return str(format(int(int_number), ','))

def check_required_args(args_name):
	print_ornament('   ABORT! No \'{0}\'!'.format(args_name), 100, ' ', 1, 0)
	return False

def check_optional_args(args_item, args_name):
	if args_item == 'none':
		print_ornament(' WARNING! No \'{0}\', assigned \'none\'!'.format(args_name), 100, ' ', 1, 0)

def get_absolute_file(file):
	split_file = [x for x in file.split('/') if x != '']
	current_dir = os.getcwd()
	split_current_dir = [x for x in current_dir.split('/') if x != '']
	if len(set(split_file)&set(split_current_dir)) == 0:
		absolute_file = current_dir + '/' + file
	else:
		absolute_file = file
	if os.path.isfile(absolute_file):
		return absolute_file
	else:
		return 'WRONG file or directory!'

def get_file_size(file):
	file_size = os.path.getsize(file)
	unit = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
	unit_order = 0
	if not file_size == 0:
		while len(str(file_size)) >= 5:
#			former_file_size = file_size
#			former_unit_order = unit_order
			file_size = round(file_size/1024.0, 1)
			unit_order += 1
		return str(file_size) + ' ' + unit[unit_order]
	else:
		return 0

def get_group_order(group):
	group_order = []
	for group_one in group:
		group_one_flat = []
		for group_one_split in group_one.split(','):
			if len(group_one_split.split('-')) == 1:
				group_one_flat.append(int(group_one_split))
			else:
				group_one_flat = group_one_flat + range(int(group_one_split.split('-')[0]), int(group_one_split.split('-')[1]) + 1)
		group_order = group_order + [group_one_flat]
	return group_order

def get_md5_sum(file):
	md5_sum = run_shell('md5sum ' + file, 1).split()[0]
	return md5_sum

def print_process_time(function_name, is_finish=0, width=100, indent=16, split_sign=':'):
	function_name_indent = ' '*(indent - len(function_name.split(split_sign)[0])) + function_name
	if is_finish == 0:		
		print_ornament(function_name_indent + ' '*(width - 23 - len(function_name_indent)) + '  -running', width)
	else:
		print_ornament(function_name_indent + ' '*(width - 23 - len(function_name_indent)) + '  -done   ', width)

def make_dir(dir):
	dir = dir.strip().rstrip("\\")
	if not os.path.exists(dir):
		os.makedirs(dir)
	return dir

def make_initial_upper(word):
	initial_upper = word[0].upper() + word[1:].lower()
	return initial_upper

def print_ornament(title, width=100, ornament_type=' ', show_time=1, show_date = 0):
	if show_time == 1:
		if show_date == 0:
			ornament = '\t|' + title + ornament_type*(width - 13 - len(title)) + ' @ ' + time.strftime("%X", time.localtime()) + '|'
		else:
			ornament = '\t|' + title + ornament_type*(width - 24 - len(title)) + ' @ ' + time.strftime("%m-%d-%Y %X", time.localtime()) + '|'
	else:
		ornament = '\t|' + title + ornament_type*(width - 2 - len(title)) + '|'
	print ornament

def write_content(content_file, content):
	output = open(content_file, 'w')
	output.writelines(content)
	output.close()

def run_bash_command(log_dir, command_name, command):
	command_file = make_dir(log_dir) + command_name + '.sh'
	write_content(command_file, command)
	bash_command = 'bash "' + command_file + '" > ' + command_file.replace('.sh', '.log') + ' 2>&1'
	run_shell(bash_command)

def run_shell(shell_command, is_get_output=0):
	shell_output = subprocess.Popen(shell_command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.read()
	if is_get_output:
		return shell_output

#---get args---
def get_args():
	tool = os.path.basename(sys.argv[0])
	author = 'Yingxiang Li'
	email = 'xlccalyx@gmail.com'
	date = 'Nov 21, 2016'
	update_date = '112116'
	home = 'http://www.calyx.biz'

	parser = argparse.ArgumentParser(description='\ttool:   ' + tool + ' v' + __version__ + '\n\tdate:   ' + date + '(' + update_date + ')\n\tauthor: ' + author + ' (' + email + ')\n\thome:   ' + home + '\n', prog=tool, formatter_class=RawTextHelpFormatter)

	parser.add_argument('-V', '--version', action='version', version='%(prog)s v' + __version__)

#---parser for mode one
	parser.add_argument('-G', '--genomes', help='genome name. (eg: mm10)', default='none')
	parser.add_argument('-H', '--hub', help='hub name. (eg: my_sample)', default='none')
	parser.add_argument('-O', '--output', help='output directory. (eg: my_output/)', default='none')
	parser.add_argument('-TT', '--tracktype', help='track type. (eg: bigWig/)', default='none')	
	parser.add_argument('-TN', '--trackname', help='track name, separated by \',\'. (eg: track_name1,track_name2)', default='none')
	parser.add_argument('-TF', '--trackfile', help='track file, separated by \',\'. (eg: track_file1.bw,track_file2.bw)', default='none')

	parser.add_argument('-SL', '--shortlabel', help='short label.', default='none')
	parser.add_argument('-LL', '--longlabel', help='long label.', default='none')
	parser.add_argument('-E', '--email', help='user email.', default='none')

#---head
	args = parser.parse_args()

	print '\n\n\t' + ' '.join(sys.argv[:]) + '\n'
	print_ornament('', 100, '-', 0, 0)
	print_ornament('tool:   ' + tool + ' v' + __version__, 100, ' ', 0, 0)
	print_ornament('author: ' + author + ' (' + email + ')', 100, ' ', 0, 0)
	print_ornament('', 100, '-', 0, 0)
	print_ornament('> BEGIN', 100, ' ', 1, 1)

	return args

#---run mode one---
def run_mode_one(args):
	start_time = datetime.datetime.now()
	preset_one = run_preset_one(args)

	if not preset_one:
		print_ornament('  Fix the problems above and re-try!', 100, ' ', 0, 0)

	else:
		output_dir = make_dir(os.path.normpath(args.output) + '/')
		output_hub_dir = make_dir(output_dir + args.hub + '/')
		output_genome_dir = make_dir(output_hub_dir + args.genomes + '/')

		create_genomes_txt(output_hub_dir, args)
		create_hub_txt(output_hub_dir, args)
		create_trackDB_txt(output_genome_dir, args)

		print_ornament('CONGRATS! CTHub was finished!', 100, ' ', 1, 0)

#---run preset one--
def run_preset_one(args):
	if args.genomes == 'none':
		check_required_args('-G/--genome')

	elif args.hub == 'none':
		check_required_args('-H/--hub')

	elif args.output == 'none':
		check_required_args('-O/--output')

	elif args.tracktype == 'none':
		check_required_args('-TT/--tracktype')

	elif args.trackname == 'none':
		check_required_args('-TN/--trackname')

	elif args.trackfile == 'none':
		check_required_args('-TF/--trackfile')

	elif len(args.trackname.split(',')) != len(args.trackfile.split(',')):
		print_ornament('   ABORT! \'track name\' number != \'track file\' number!', 100, ' ', 1, 0)
		return False

	else:
		check_optional_args(args.shortlabel, '-SL/--shortlabel')
		check_optional_args(args.longlabel, '-LL/--longlabel')
		check_optional_args(args.email, '-E/--email')

		return True

#---create genomes txt--
def create_genomes_txt(output_hub_dir, args):
	genomes_txt_file = output_hub_dir + 'genomes.txt'

	if not os.path.isfile(genomes_txt_file):
		genomes_txt = 'genome {0}\ntrackDb {0}/trackDb.txt'.format(args.genomes)
		write_content(genomes_txt_file, genomes_txt)

	else:
		print_ornament(' WARNING! \'genomes.txt\' existed! Skipped.', 100, ' ', 1, 0)

#---create hub txt--
def create_hub_txt(output_hub_dir, args):
	hub_txt_file = output_hub_dir + 'hub.txt'

	if not os.path.isfile(hub_txt_file):
		hub_txt = 'hub {0}\nshortLabel {1}\nlongLabel {2}\ngenomesFile genomes.txt\nemail {3}'.format(args.hub, args.shortlabel, args.longlabel, args.email)
		write_content(hub_txt_file, hub_txt)

	else:
		print_ornament(' WARNING! \'hub.txt\' existed! Skipped.', 100, ' ', 1, 0)

#---create trackDB txt-- zhe
def create_trackDB_txt(output_genome_dir, args):
	trackDB_txt_file = output_genome_dir + 'trackDb.txt'

	if not os.path.isfile(trackDB_txt_file):
		trackDB_txt = ''
		track_number = len(args.trackname.split(','))

		for i in range(track_number):
			track_name = args.trackname.split(',')[i]
			track_file = args.trackfile.split(',')[i]
			trackDB_txt += 'track {0}\nbigDataUrl {1}\nshortLabel {0}\nlongLabel {0}\ntype {2}\n\n'.format(track_name, track_file, args.tracktype)

		write_content(trackDB_txt_file, trackDB_txt)

	else:
		print_ornament(' WARNING! \'trackDb.txt\' existed! Skipped.', 100, ' ', 1, 0)

##----PROCESS------##
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write('\t|ABORT! User interrupted me! ;-) Bye!' + ' '*62 + '|\n\t|' + '~'*98 + '|\n')
        sys.exit(0)

##----TEST--------##
