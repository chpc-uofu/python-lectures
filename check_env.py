import importlib
import sys

__author__ = "Wim R.M. Cardoen"
__version__ = "2020"
# Last update: 05/19/2020

# Dictionary with the comparaison operators
dictCmp={"==": '__eq__',
         "<=": '__le__',
         "<" : '__lt__',
         ">" : '__gt__',
         ">=": '__ge__',
         "!=": '__ne__',
        } 

def get_pyversion():
    """
    Retrieve:
      a.Version of Python 
      b.Installation prefix
    """
    version = sys.version_info[0:3]
    print("    Python {0}.{1}.{2} found".format(version[0],
                        version[1],version[2]))
    print("        --prefix={0}\n".format(sys.prefix))
    if int(version[0]) !=3 or int(version[1]) < 6:
        str_err= "    ERROR: Python >=3.6 is REQUIRED!"
        sys.exit(str_err)
    return

def check_package(pkg,op,req_version):
    """
    Function which checks:
       a. whether a package is installed
       b. if the package is installed it also checks 
          whether it fulfills the requirements.
    Return: isOK (boolean)
    """
    isOK = False
    try:
        mod = importlib.import_module(pkg)
        isOK = getattr(mod.__version__,dictCmp[op])(req_version) 
        if isOK:
            print("  {0:>15s}  inst.:{1:>10s}  {2:>2s} req.:{3:>10s} -> OK ".\
                     format(pkg,mod.__version__, op, req_version))
        else:
            print("  {0:>15s}  inst.:{1:>10s} !{2:>2s} req.:{3:>10s} -> FAIL ".\
                     format(pkg,mod.__version__, op, req_version))
    except ImportError:
        print("  {0:>15s}  can't be found                       -> FAIL ".\
              format(pkg))
    return isOK


if __name__ == "__main__":

    # --- Start Requirements SPECIFIC for the NumPy/SciPy tutorial
    #     which means:
    #       numpy>=1.12.0
    #       scipy>=0.19.0
    #       matplotlib>=1.5.0
    #       notebook>=4.2.0 
    REQUIRED_PKG = ['numpy','scipy','matplotlib','notebook']
    CMP_OP = ['>=', '>=','>=','>=']
    REQUIRED_VERSION = ['1.12.0','0.19.0','1.5.0','4.2.0']
    # --- End of the Tutorial Requirements 


    print("\n\n  Checking installation ...\n")

    get_pyversion() 
    
    statLst = []
    for ipkg in range(len(REQUIRED_PKG)):
        status = check_package(REQUIRED_PKG[ipkg],CMP_OP[ipkg],REQUIRED_VERSION[ipkg])
        statLst.append(int(status))

    if sum(statLst) == len(REQUIRED_PKG):
        print("\n    All required packages are installed")
        print("    Congratulations!")
    else:
        print("\n    Some of the required packages either " +
              "can't be found\n" +
              "          or don't have the required version.")
        print("    Please CHECK your installation!")         
    print("\n  End checking installation\n")
