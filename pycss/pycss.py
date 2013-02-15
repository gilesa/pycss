'''
Created on 2013-02-12

@author: giles
'''
import argparse
import os
from time import sleep
import cssparse


def ispycss( f ):
    if f.endswith( '.pycss' ):
        return True
    else:
        return False


def parsefiles( files, filecache ):
    for i, f in enumerate( files ):       
        modtime = os.path.getmtime( f ) 
        if modtime > filecache[i]:
            filecache[i] = modtime
            
            pycssfile = open( f, 'r' )
            output = cssparse.parse( pycssfile )        
            cssfile = open( f.replace( '.pycss', '.css' ), 'w' )
            cssfile.write( output.lstrip() )
            cssfile.close()
            pycssfile.close()
        
            print "Successfully converted '{0}'".format( f ) 
    

def main( path, watch ):
    
    files = []
    
    # Check if valid file or directory specified
    if os.path.isfile( path ) and ispycss( path ):
        print "Loading file:", path
        
        files.append( path );
    elif os.path.isdir( path ):
        # Make sure there is a trailing slash
        if not path.endswith( '/' ):
            path = path + '/'
        
        print "Loading directory:", path
        
        # Load all pycss files and prepend the path 
        dirfiles = filter( ispycss, os.listdir( path ) )
        files[:] = [path + f for f in dirfiles]
    else:
        print "Not a valid file or directory."
         
    filecache = [0] * len( files )
    
    if watch:
        while True:
            parsefiles( files, filecache )
            sleep( 5 )
    else:
        parsefiles( files, filecache )
             
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='Convert pycss files to valid CSS files.' )
    parser.add_argument( 'input', nargs='?', default='.',
                        help='file to convert or directory in which to convert all pycss files (default: the current directory)' )
    parser.add_argument( '-w', '--watch', action='store_true',
                        help='if included, the input is continuously polled for changes and updated' )
    args = parser.parse_args()
    
    main( args.input, args.watch )