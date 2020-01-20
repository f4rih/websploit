import cmd
import sys
from modules import all_modules, module_list
from core.utils import CPrint

completions = [
    'target',
    'ip',
    'gateway',
    'mac',
    'iface',
    'gateway_mac',
    'target_mac'
]

class Module(cmd.Cmd):
    parameters = {}
    cp = CPrint()


    def do_execute(self):
        """Execute current module"""
        pass

    def do_back(self, *args):
        """go back one level"""
        return True

    def do_exit(self, line):
        """exit websploit"""
        sys.exit(0)

    def do_set(self, line):
        """set options"""
        try:
            key, value = line.split(' ')
            print(key, value)
            self.parameters.update({key: value})
        except KeyError:
            # print(f"*** Unknown Option! option not has value!")
            self.cp.warning(text="*** Unknown Option! option not has value!")
        except ValueError:
            # print(f"*** Option not has value!")
            # print(f"*** Example : set host 127.0.0.1")
            self.cp.warning(text="*** Option not has value!")
            self.cp.info(text="*** Example : set host 127.0.0.1")

    def do_options(self, line):
        """Show options of current module"""
        print("\n")
        print(f"{'Option':20}\t{'Value':20}")
        print(f"{'='*20:20}\t{'='*20:20}")
        for k,v in self.parameters.items():
            print(f"{k:20}\t{v:20}")
        print("\n")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]






