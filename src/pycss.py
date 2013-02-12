'''
Created on 2013-02-12

@author: giles
'''
import argparse
import os


def main( _input ):
    
    files = []
    
    if os.path.isfile( _input ):
        print "File!"
        files.append( _input );
    elif os.path.isdir( _input ):
        print "Directory!"
         
        if not _input.endswith( '/' ):
            prefix = _input + '/'
        else:
            prefix = _input

        files[:] = [prefix + f for f in os.listdir( _input )]
            
    print files
    
    for f in files:
        pass
   
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='Convert pycss files to valid CSS files.' )
    parser.add_argument( 'input', nargs='?', default='.',
                        help='file to convert or directory in which to convert all pycss files (default: the current directory)' )
    args = parser.parse_args()
    
    main( args.input )